"""
Streak flame - generated procedurally from scratch (no SVG, pure raster image).
Dependencies: pip install numpy pillow scipy
Output: streak_flame.png (1024x1024, transparent background) in frontend/results/streak
"""
import numpy as np
from PIL import Image
from scipy.ndimage import distance_transform_edt

from painting.results_dir import RESULTS_DIR

SIZE = 1024          # Final size in pixels
SUPERSAMPLING = 4    # Render larger, then scale down for smooth edges

OUT_DIR = RESULTS_DIR / "streak"
OUT_FILE = OUT_DIR / "streak_flame.png"

# Color gradients from the bottom (0.0) to the tip (1.0) of each layer
OUTER_COLORS = [(0.0, (214, 40, 20)), (0.5, (240, 80, 25)), (1.0, (255, 120, 30))]
MIDDLE_COLORS = [(0.0, (255, 120, 20)), (1.0, (255, 170, 40))]
CORE_COLORS = [(0.0, (255, 245, 200)), (0.6, (255, 220, 90)), (1.0, (255, 200, 60))]


class FlameRenderer:
    """Draws the three flame layers (outer, middle, core) as transparent images."""

    def __init__(self):
        self._resolution = SIZE * SUPERSAMPLING
        grid_y, grid_x = np.mgrid[0:self._resolution, 0:self._resolution].astype(np.float32)
        self._grid_y = grid_y / self._resolution
        self._grid_x = grid_x / self._resolution

    def render_layers(self):
        """Returns the layers separately as (outer, middle, core) RGBA images."""
        return self._render_outer_layer(), self._render_middle_layer(), self._render_core_layer()

    def render_composite(self):
        """Returns all layers stacked into one finished image."""
        composite = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))

        for layer in self.render_layers():
            composite.alpha_composite(layer)

        return composite

    def _build_flame_mask(
        self,
        center_x,
        base,
        height,
        radius,
        lean,
        power,
        sharpness=1.6,
    ):
        """
        Builds one flame shape as a boolean mask.
        progress = 0 at the bottom, 1 at the tip.
        Half width: radius * sin(pi * progress^power), tapering concavely
                    to the tip (exponent sharpness) behind the widest point.
        Center line: center_x + lean * progress^2, so the tip bends sideways.
        """
        progress = (base - self._grid_y) / height
        inside_flame = (progress >= 0) & (progress <= 1)
        clipped_progress = np.clip(progress, 0, 1)

        width_curve = np.clip(np.sin(np.pi * clipped_progress ** power), 0, 1)
        widest_point = 0.5 ** (1 / power)
        half_width = radius * np.where(
            clipped_progress > widest_point,
            width_curve ** sharpness,
            width_curve,
        )

        center_line = center_x + lean * clipped_progress ** 2
        mask = inside_flame & (np.abs(self._grid_x - center_line) < half_width)

        return mask, clipped_progress

    def _round_inner_corners(self, mask, radius):
        """Rounds concave corners with a closing. Tips stay sharp."""
        radius_pixels = radius * self._resolution
        dilated = distance_transform_edt(~mask) < radius_pixels

        return distance_transform_edt(dilated) > radius_pixels

    def _build_vertical_gradient(self, progress, color_stops):
        """Linear color gradient along progress. color_stops = [(position, (r, g, b)), ...]"""
        positions = np.array([stop[0] for stop in color_stops])
        colors = np.array([stop[1] for stop in color_stops], dtype=np.float32)
        gradient = np.zeros(progress.shape + (3,), dtype=np.float32)

        for channel in range(3):
            gradient[..., channel] = np.interp(progress, positions, colors[:, channel])

        return gradient

    def _to_layer_image(self, mask, colors):
        """Paints the masked area opaque and scales down to the final size."""
        canvas = np.zeros((self._resolution, self._resolution, 4), dtype=np.uint8)
        canvas[..., :3][mask] = colors[mask].astype(np.uint8)
        canvas[..., 3][mask] = 255

        return Image.fromarray(canvas, "RGBA").resize((SIZE, SIZE), Image.Resampling.LANCZOS)

    def _render_outer_layer(self):
        body_mask, _ = self._build_flame_mask(
            center_x=0.50,
            base=0.92,
            height=0.84,
            radius=0.29,
            lean=-0.10,
            power=0.45,
            sharpness=1.9,
        )
        # The tongue grows out of the body at the bottom and runs tangent into its flank
        tongue_mask, _ = self._build_flame_mask(
            center_x=0.62,
            base=0.895,
            height=0.64,
            radius=0.17,
            lean=0.13,
            power=0.45,
            sharpness=2.2,
        )
        outer_mask = self._round_inner_corners(mask=body_mask | tongue_mask, radius=0.03)

        # One gradient over the full height, so body and tongue have no visible seam
        height_progress = np.clip((0.92 - self._grid_y) / 0.84, 0, 1)
        colors = self._build_vertical_gradient(progress=height_progress, color_stops=OUTER_COLORS)

        return self._to_layer_image(mask=outer_mask, colors=colors)

    def _render_middle_layer(self):
        mask, progress = self._build_flame_mask(
            center_x=0.51,
            base=0.895,
            height=0.62,
            radius=0.20,
            lean=-0.06,
            power=0.45,
            sharpness=1.8,
        )
        colors = self._build_vertical_gradient(progress=progress, color_stops=MIDDLE_COLORS)

        return self._to_layer_image(mask=mask, colors=colors)

    def _render_core_layer(self):
        mask, progress = self._build_flame_mask(
            center_x=0.51,
            base=0.865,
            height=0.40,
            radius=0.115,
            lean=-0.03,
            power=0.45,
            sharpness=1.7,
        )
        colors = self._build_vertical_gradient(progress=progress, color_stops=CORE_COLORS)

        return self._to_layer_image(mask=mask, colors=colors)


def render_flame_image():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FlameRenderer().render_composite().save(OUT_FILE)
    print(f"Saved: {OUT_FILE}")


if __name__ == "__main__":
    render_flame_image()
