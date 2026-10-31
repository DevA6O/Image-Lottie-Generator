"""
Shortcuts on top of LayerPainter for the flat icon look (used by the food and the verb images).
Every fill_* method builds a shape and paints it in one solid color with a darker crescent.
A shade is a pair of colors: (top_color, bottom_color). The painter blends it into one color.
"""
import math

import numpy as np
from PIL import ImageChops, ImageDraw
from scipy.interpolate import PchipInterpolator
from scipy.ndimage import distance_transform_edt

from painting.layer_painter import SUPERSAMPLING, LayerPainter

ELLIPSE_POINT_COUNT = 120
CURVE_POINT_COUNT = 160
ARC_POINT_COUNT = 40
POLYLINE_STEPS_PER_SEGMENT = 12

CRESCENT_RADIUS_RATIO = 0.22      # Crescent width compared to the thickest radius of the shape
CRESCENT_MAX_SHIFT = 40           # In final pixels, so huge shapes do not get a huge crescent
CRESCENT_VERTICAL_RATIO = 0.6     # The light comes more from the left than from the top
CRESCENT_MEASURE_DOWNSCALE = 8    # The thickness is measured on a small mask to stay fast
CRESCENT_DARKEN_FACTOR = 0.82


def _blend_shade(shade):
    """Middle color of a (top_color, bottom_color) pair."""
    return tuple(round((top + bottom) / 2) for top, bottom in zip(shade[0], shade[1]))


def _darken(color):
    return tuple(round(channel * CRESCENT_DARKEN_FACTOR) for channel in color)


def rotate_point(
    point,
    center,
    angle_degrees,
):
    angle = math.radians(angle_degrees)
    offset_x = point[0] - center[0]
    offset_y = point[1] - center[1]

    return (
        center[0] + offset_x * math.cos(angle) - offset_y * math.sin(angle),
        center[1] + offset_x * math.sin(angle) + offset_y * math.cos(angle),
    )


def sample_curve(
    start,
    first_control,
    second_control,
    end,
):
    """Points on a cubic bezier curve."""
    points = []

    for step in range(CURVE_POINT_COUNT + 1):
        t = step / CURVE_POINT_COUNT
        weights = ((1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t ** 2 * (1 - t), t ** 3)
        anchors = (start, first_control, second_control, end)
        points.append((
            sum(weight * anchor[0] for weight, anchor in zip(weights, anchors)),
            sum(weight * anchor[1] for weight, anchor in zip(weights, anchors)),
        ))

    return points


def build_normal(
    points,
    index,
):
    """Unit vector that is perpendicular to the curve at one of its points."""
    previous_point = points[max(index - 1, 0)]
    following_point = points[min(index + 1, len(points) - 1)]
    direction_x = following_point[0] - previous_point[0]
    direction_y = following_point[1] - previous_point[1]
    length = math.hypot(direction_x, direction_y)

    return (-direction_y / length, direction_x / length)


def build_width_profile(
    stops,
    point_count=CURVE_POINT_COUNT + 1,
):
    """Widths along a curve. stops = [(position from 0 to 1, width), ...]. The outline between the stops is smooth."""
    positions = [stop[0] for stop in stops]
    widths = [stop[1] for stop in stops]
    smooth_widths = PchipInterpolator(positions, widths)

    return [float(smooth_widths(step / (point_count - 1))) for step in range(point_count)]


def build_star_points(
    center,
    outer_radius,
    inner_radius,
    tip_count,
    rotation=0,
):
    points = []

    for index in range(tip_count * 2):
        radius = outer_radius if index % 2 == 0 else inner_radius
        angle = math.radians(rotation - 90 + index * 180 / tip_count)
        points.append((center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)))

    return points


def solid(color):
    """A shade that has the same color on top and at the bottom."""
    return (color, color)


def build_direction(angle_degrees):
    """Unit vector for body angles: 0 points down, 90 points right, 180 points up."""
    angle = math.radians(angle_degrees)

    return (math.sin(angle), math.cos(angle))


def build_arc_points(
    center,
    radius,
    start_angle,
    end_angle,
):
    """Points on a circle arc. Angles in degrees: 0 is right, 90 is down, -90 is up."""
    points = []

    for step in range(ARC_POINT_COUNT + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * step / ARC_POINT_COUNT)
        points.append((center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle)))

    return points


def build_polyline_points(corners):
    """Many points along straight segments, so a curve mask draws round joints."""
    points = []

    for start, end in zip(corners, corners[1:]):
        for step in range(POLYLINE_STEPS_PER_SEGMENT):
            progress = step / POLYLINE_STEPS_PER_SEGMENT
            points.append((start[0] + (end[0] - start[0]) * progress, start[1] + (end[1] - start[1]) * progress))

    points.append(corners[-1])

    return points


def move_point(
    point,
    angle,
    distance,
):
    """Moves a point. Angle in degrees: 0 is right, 90 is down, -90 is up."""
    radians = math.radians(angle)

    return (point[0] + distance * math.cos(radians), point[1] + distance * math.sin(radians))


class FlatPainter(LayerPainter):
    """Flat shapes with a darker crescent. All coordinates are final pixels."""

    def fill(
        self,
        mask,
        shade,
        clip=None,
    ):
        """
        Flat icon look: one solid color and a darker crescent on the lower right side.
        The shade pair is blended into its middle color. Clipped shapes (highlights, spots) get no crescent.
        """
        bounds = mask.getbbox()

        if bounds is None:
            return

        visible_mask = mask if clip is None else self.intersect_masks(first_mask=mask, second_mask=clip)
        self._paint_flat(mask=visible_mask, color=_blend_shade(shade=shade), bounds=bounds)

        if clip is None:
            self._paint_crescent(mask=mask, color=_darken(color=_blend_shade(shade=shade)), bounds=bounds)

    def fill_flat(
        self,
        mask,
        shade,
    ):
        """One solid color without a crescent, for faces that already have their own darker neighbor."""
        bounds = mask.getbbox()

        if bounds is None:
            return

        self._paint_flat(mask=mask, color=_blend_shade(shade=shade), bounds=bounds)

    def _paint_flat(
        self,
        mask,
        color,
        bounds,
    ):
        self.paint(
            mask=mask,
            color_stops=[(0.0, color), (1.0, color)],
            top=bounds[1] / SUPERSAMPLING,
            bottom=bounds[3] / SUPERSAMPLING,
        )

    def _paint_crescent(
        self,
        mask,
        color,
        bounds,
    ):
        """The part of the shape that is not covered when the shape is moved to the upper left."""
        shift = self._measure_crescent_shift(mask=mask)

        if shift < 1:
            return

        lit_mask = ImageChops.offset(mask, -shift, -round(shift * CRESCENT_VERTICAL_RATIO))
        crescent_mask = ImageChops.subtract(mask, lit_mask)
        self._paint_flat(mask=crescent_mask, color=color, bounds=bounds)

    def _measure_crescent_shift(self, mask):
        """Shift in supersampled pixels. Based on the thickest part, so thin stems keep a thin crescent."""
        small_mask = np.asarray(mask.resize((mask.width // CRESCENT_MEASURE_DOWNSCALE, mask.height // CRESCENT_MEASURE_DOWNSCALE))) > 127
        distances = np.asarray(distance_transform_edt(small_mask))
        thickest_radius = distances.max() * CRESCENT_MEASURE_DOWNSCALE

        return round(min(thickest_radius * CRESCENT_RADIUS_RATIO, CRESCENT_MAX_SHIFT * SUPERSAMPLING))

    def fill_ellipse(
        self,
        center,
        radius_x,
        radius_y,
        shade,
        angle=0,
        clip=None,
    ):
        mask = self.build_rotated_ellipse_mask(center=center, radius_x=radius_x, radius_y=radius_y, angle=angle)
        self.fill(mask=mask, shade=shade, clip=clip)

    def fill_circle(
        self,
        center,
        radius,
        shade,
        clip=None,
    ):
        self.fill_ellipse(center=center, radius_x=radius, radius_y=radius, shade=shade, clip=clip)

    def fill_polygon(
        self,
        points,
        shade,
        clip=None,
    ):
        self.fill(mask=self.build_polygon_mask(points=points), shade=shade, clip=clip)

    def fill_rounded_rect(
        self,
        box,
        radius,
        shade,
        clip=None,
    ):
        self.fill(mask=self.build_rounded_rect_mask(box=box, radius=radius), shade=shade, clip=clip)

    def fill_stroke(
        self,
        start,
        end,
        width,
        shade,
        clip=None,
    ):
        self.fill(mask=self.build_stroke_mask(start=start, end=end, width=width), shade=shade, clip=clip)

    def fill_curve(
        self,
        points,
        width,
        shade,
        clip=None,
    ):
        self.fill(mask=self.build_curve_mask(points=points, width=width), shade=shade, clip=clip)

    def fill_tapered_curve(
        self,
        points,
        widths,
        shade,
        clip=None,
        round_ends=True,
    ):
        mask = self.build_tapered_curve_mask(points=points, widths=widths, round_ends=round_ends)
        self.fill(mask=mask, shade=shade, clip=clip)

    def build_tapered_curve_mask(
        self,
        points,
        widths,
        round_ends=True,
    ):
        """A shape that follows a curve and has its own width at every point (carrots, bananas, leaves)."""
        left_side = []
        right_side = []

        for index, point in enumerate(points):
            normal_x, normal_y = build_normal(points=points, index=index)
            half_width = widths[index] / 2
            left_side.append((point[0] + normal_x * half_width, point[1] + normal_y * half_width))
            right_side.append((point[0] - normal_x * half_width, point[1] - normal_y * half_width))

        mask = self.build_polygon_mask(points=left_side + right_side[::-1])

        if round_ends:
            for index in (0, len(points) - 1):
                radius = widths[index] / 2
                end_mask = self.build_rotated_ellipse_mask(center=points[index], radius_x=radius, radius_y=radius)
                mask = self.union_masks(first_mask=mask, second_mask=end_mask)

        return mask

    def build_rotated_ellipse_mask(
        self,
        center,
        radius_x,
        radius_y,
        angle=0,
    ):
        points = []

        for step in range(ELLIPSE_POINT_COUNT):
            theta = 2 * math.pi * step / ELLIPSE_POINT_COUNT
            point = (center[0] + radius_x * math.cos(theta), center[1] + radius_y * math.sin(theta))
            points.append(rotate_point(point=point, center=center, angle_degrees=angle))

        return self.build_polygon_mask(points=points)

    def build_box_mask(
        self,
        left,
        top,
        right,
        bottom,
    ):
        return self.build_polygon_mask(points=[(left, top), (right, top), (right, bottom), (left, bottom)])

    def build_curve_mask(
        self,
        points,
        width,
    ):
        """A thick line through many points, with round ends and joints."""
        mask = self._create_empty_mask()
        draw = ImageDraw.Draw(mask)
        draw.line(xy=self._scale_points(points), fill=255, width=round(width * SUPERSAMPLING), joint="curve")

        for point in points[::3] + [points[-1]]:
            left_top = (point[0] - width / 2, point[1] - width / 2)
            right_bottom = (point[0] + width / 2, point[1] + width / 2)
            draw.ellipse(xy=self._scale_points([left_top, right_bottom]), fill=255)

        return mask

    def build_pear_mask(
        self,
        center_x,
        top_center_y,
        top_radius,
        bottom_center_y,
        bottom_radius,
    ):
        """A small circle on a big circle, joined smoothly. Used for pears, avocados and eggs."""
        top_mask = self.build_rotated_ellipse_mask(center=(center_x, top_center_y), radius_x=top_radius, radius_y=top_radius)
        bottom_mask = self.build_rotated_ellipse_mask(
            center=(center_x, bottom_center_y),
            radius_x=bottom_radius,
            radius_y=bottom_radius,
        )
        neck_mask = self.build_polygon_mask(points=[
            (center_x - top_radius, top_center_y),
            (center_x + top_radius, top_center_y),
            (center_x + bottom_radius, bottom_center_y),
            (center_x - bottom_radius, bottom_center_y),
        ])

        return self.round_corners(mask=self.union_all(masks=[top_mask, bottom_mask, neck_mask]), radius=60)

    def union_all(self, masks):
        combined_mask = masks[0]

        for mask in masks[1:]:
            combined_mask = self.union_masks(first_mask=combined_mask, second_mask=mask)

        return combined_mask

    def subtract_masks(
        self,
        base_mask,
        cut_mask,
    ):
        return ImageChops.subtract(base_mask, cut_mask)

    def flat_ellipse(
        self,
        center,
        radius_x,
        radius_y,
        color,
        angle=0,
    ):
        mask = self.build_rotated_ellipse_mask(center=center, radius_x=radius_x, radius_y=radius_y, angle=angle)
        self.fill_flat(mask=mask, shade=solid(color))

    def flat_circle(
        self,
        center,
        radius,
        color,
    ):
        self.flat_ellipse(center=center, radius_x=radius, radius_y=radius, color=color)

    def flat_stroke(
        self,
        start,
        end,
        width,
        color,
    ):
        self.fill_flat(mask=self.build_stroke_mask(start=start, end=end, width=width), shade=solid(color))

    def flat_curve(
        self,
        points,
        width,
        color,
    ):
        self.fill_flat(mask=self.build_curve_mask(points=points, width=width), shade=solid(color))

    def flat_polygon(
        self,
        points,
        color,
    ):
        self.fill_flat(mask=self.build_polygon_mask(points=points), shade=solid(color))

    def fill_ring(
        self,
        center,
        outer_radius,
        inner_radius,
        color,
    ):
        outer_mask = self.build_rotated_ellipse_mask(center=center, radius_x=outer_radius, radius_y=outer_radius)
        inner_mask = self.build_rotated_ellipse_mask(center=center, radius_x=inner_radius, radius_y=inner_radius)
        self.fill(mask=self.subtract_masks(base_mask=outer_mask, cut_mask=inner_mask), shade=solid(color))
