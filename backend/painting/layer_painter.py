"""
Base painter for all flat image categories (food, verbs).
Paints shapes in layers onto one transparent canvas, with smooth edges through supersampling.
Dependencies: pip install numpy pillow scipy
"""
import numpy as np
from PIL import Image, ImageChops, ImageDraw
from scipy.ndimage import distance_transform_edt

CANVAS_SIZE = 1024   # Final size in pixels
SUPERSAMPLING = 4    # Render larger, then scale down for smooth edges


class LayerPainter:
    """Paints gradient-filled shapes onto one transparent canvas. All coordinates are final pixels."""

    def __init__(self):
        self._resolution = CANVAS_SIZE * SUPERSAMPLING
        self._canvas = Image.new("RGBA", (self._resolution, self._resolution), (0, 0, 0, 0))

    def build_polygon_mask(self, points):
        mask = self._create_empty_mask()
        ImageDraw.Draw(mask).polygon(xy=self._scale_points(points), fill=255)

        return mask

    def build_rounded_rect_mask(
        self,
        box,
        radius,
    ):
        """box = (left, top, right, bottom)"""
        mask = self._create_empty_mask()
        ImageDraw.Draw(mask).rounded_rectangle(
            xy=self._scale_points([(box[0], box[1]), (box[2], box[3])]),
            radius=radius * SUPERSAMPLING,
            fill=255,
        )

        return mask

    def build_ellipse_mask(
        self,
        center,
        radius_x,
        radius_y,
    ):
        mask = self._create_empty_mask()
        left_top = (center[0] - radius_x, center[1] - radius_y)
        right_bottom = (center[0] + radius_x, center[1] + radius_y)
        ImageDraw.Draw(mask).ellipse(xy=self._scale_points([left_top, right_bottom]), fill=255)

        return mask

    def build_stroke_mask(
        self,
        start,
        end,
        width,
    ):
        """A thick line with round ends."""
        mask = self._create_empty_mask()
        draw = ImageDraw.Draw(mask)
        draw.line(xy=self._scale_points([start, end]), fill=255, width=round(width * SUPERSAMPLING))

        for end_point in (start, end):
            left_top = (end_point[0] - width / 2, end_point[1] - width / 2)
            right_bottom = (end_point[0] + width / 2, end_point[1] + width / 2)
            draw.ellipse(xy=self._scale_points([left_top, right_bottom]), fill=255)

        return mask

    def round_corners(
        self,
        mask,
        radius,
    ):
        """Rounds convex corners with an opening and concave corners with a closing."""
        radius_pixels = radius * SUPERSAMPLING
        inside = np.asarray(mask) > 0

        opened = self._grow(mask=self._shrink(mask=inside, radius_pixels=radius_pixels), radius_pixels=radius_pixels)
        closed = self._shrink(mask=self._grow(mask=opened, radius_pixels=radius_pixels), radius_pixels=radius_pixels)

        return Image.fromarray((closed * 255).astype(np.uint8), "L")

    def union_masks(
        self,
        first_mask,
        second_mask,
    ):
        return ImageChops.lighter(first_mask, second_mask)

    def intersect_masks(
        self,
        first_mask,
        second_mask,
    ):
        return ImageChops.multiply(first_mask, second_mask)

    def paint(
        self,
        mask,
        color_stops,
        top,
        bottom,
    ):
        """
        Fills the mask with a vertical gradient.
        color_stops = [(position, (r, g, b)), ...] where 0.0 is at `top` and 1.0 at `bottom`.
        """
        layer = self._build_vertical_gradient(color_stops=color_stops, top=top, bottom=bottom)
        layer.putalpha(mask)

        # alpha_composite keeps the edge colors clean, a masked paste would darken them
        self._canvas.alpha_composite(layer)

    def save(self, out_file):
        out_file.parent.mkdir(parents=True, exist_ok=True)
        self._canvas.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS).save(out_file)
        print(f"Saved: {out_file}")

    def _create_empty_mask(self):
        return Image.new("L", (self._resolution, self._resolution), 0)

    def _grow(
        self,
        mask,
        radius_pixels,
    ):
        return distance_transform_edt(~mask) <= radius_pixels

    def _shrink(
        self,
        mask,
        radius_pixels,
    ):
        return distance_transform_edt(mask) > radius_pixels

    def _scale_points(self, points):
        return [(x * SUPERSAMPLING, y * SUPERSAMPLING) for x, y in points]

    def _build_vertical_gradient(
        self,
        color_stops,
        top,
        bottom,
    ):
        pixel_rows = np.arange(self._resolution) / SUPERSAMPLING
        progress = (pixel_rows - top) / (bottom - top)
        positions = [stop[0] for stop in color_stops]
        row_colors = np.stack(
            [np.interp(progress, positions, [stop[1][channel] for stop in color_stops]) for channel in range(3)],
            axis=-1,
        ).astype(np.uint8)
        gradient = np.broadcast_to(row_colors[:, None, :], (self._resolution, self._resolution, 3))

        return Image.fromarray(np.ascontiguousarray(gradient), "RGB").convert("RGBA")
