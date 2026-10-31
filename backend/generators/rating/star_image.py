"""
Draws a full or a half-filled star as a transparent image (used by full_star.py and half_star.py).
Dependencies: pip install numpy pillow (star_shape.py must be in the same folder)
"""
import numpy as np
from PIL import Image, ImageDraw

from star_shape import (
    CANVAS_SIZE,
    EMPTY_STAR_COLOR,
    STAR_CENTER_X,
    STAR_CENTER_Y,
    STAR_COLOR_STOPS,
    STAR_RADIUS,
    build_star_outline,
    clip_to_left_half,
)

SUPERSAMPLING = 4    # Render larger, then scale down for smooth edges


class StarPainter:
    """Paints stars onto one transparent canvas."""

    def __init__(self):
        self._resolution = CANVAS_SIZE * SUPERSAMPLING
        self._canvas = Image.new("RGBA", (self._resolution, self._resolution), (0, 0, 0, 0))
        self._gold_gradient = self._build_gold_gradient()

    def paint_full_star(self):
        self._paint_gold(mask=self._build_polygon_mask(outline=build_star_outline()))

    def paint_half_star(self):
        outline = build_star_outline()
        self._paint_empty(mask=self._build_polygon_mask(outline=outline))
        self._paint_gold(mask=self._build_polygon_mask(outline=clip_to_left_half(outline)))

    def to_image(self):
        return self._canvas.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS)

    def _build_gold_gradient(self):
        """Vertical gold gradient. It spans the star from its top tip to its bottom."""
        pixel_rows = np.arange(self._resolution) / SUPERSAMPLING
        progress = (pixel_rows - (STAR_CENTER_Y - STAR_RADIUS)) / (2 * STAR_RADIUS)
        positions = [stop[0] for stop in STAR_COLOR_STOPS]
        row_colors = np.stack(
            [np.interp(progress, positions, [stop[1][channel] for stop in STAR_COLOR_STOPS]) for channel in range(3)],
            axis=-1,
        ).astype(np.uint8)
        gradient = np.broadcast_to(row_colors[:, None, :], (self._resolution, self._resolution, 3))

        return Image.fromarray(np.ascontiguousarray(gradient), "RGB").convert("RGBA")

    def _build_polygon_mask(self, outline):
        mask = Image.new("L", (self._resolution, self._resolution), 0)
        points = [
            ((STAR_CENTER_X + x) * SUPERSAMPLING, (STAR_CENTER_Y + y) * SUPERSAMPLING)
            for x, y in outline
        ]
        ImageDraw.Draw(mask).polygon(xy=points, fill=255)

        return mask

    def _paint_gold(self, mask):
        self._paint_layer(layer=self._gold_gradient.copy(), mask=mask)

    def _paint_empty(self, mask):
        empty_layer = Image.new("RGBA", (self._resolution, self._resolution), (*EMPTY_STAR_COLOR, 255))
        self._paint_layer(layer=empty_layer, mask=mask)

    def _paint_layer(
        self,
        layer,
        mask,
    ):
        # alpha_composite keeps the edge colors clean, a masked paste would darken them
        layer.putalpha(mask)
        self._canvas.alpha_composite(layer)


def save_star_image(
    paint_star,
    out_file,
):
    """paint_star is a StarPainter method, e.g. StarPainter.paint_full_star."""
    painter = StarPainter()
    paint_star(painter)

    out_file.parent.mkdir(parents=True, exist_ok=True)
    painter.to_image().save(out_file)
    print(f"Saved: {out_file}")
