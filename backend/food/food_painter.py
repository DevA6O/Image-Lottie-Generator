"""
Shortcuts on top of LayerPainter for the food images.
Every fill_* method builds a shape and paints it with a vertical gradient over the shape's height.
A shade is a pair of colors: (top_color, bottom_color).
"""
import math

from PIL import ImageChops, ImageDraw
from scipy.interpolate import PchipInterpolator

from layer_painter import OUT_DIR, SUPERSAMPLING, LayerPainter

ELLIPSE_POINT_COUNT = 120
CURVE_POINT_COUNT = 160


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


class FoodPainter(LayerPainter):
    """Gradient shapes for the food images. All coordinates are final pixels."""

    def save_image(self, name):
        self.save(out_file=OUT_DIR / f"{name}.png")

    def fill(
        self,
        mask,
        shade,
        clip=None,
    ):
        """The gradient spans the whole mask, even when a clip shows only a part of it."""
        bounds = mask.getbbox()

        if bounds is None:
            return

        visible_mask = mask if clip is None else self.intersect_masks(first_mask=mask, second_mask=clip)
        self.paint(
            mask=visible_mask,
            color_stops=[(0.0, shade[0]), (1.0, shade[1])],
            top=bounds[1] / SUPERSAMPLING,
            bottom=bounds[3] / SUPERSAMPLING,
        )

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
