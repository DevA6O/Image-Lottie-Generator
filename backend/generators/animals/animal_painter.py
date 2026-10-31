"""
Painter for the animal images: the flat painter, plus short helpers for animal shapes
and the place where the finished PNGs go. Colors are plain (r, g, b) tuples here.
"""
from PIL import Image, ImageOps

from painting.flat_painter import FlatPainter, build_arc_points, build_polyline_points, solid
from painting.results_dir import RESULTS_DIR

ANIMAL_OUT_DIR = RESULTS_DIR / "animals"

# Longest side of the animal on the canvas (fraction), so every animal has the same margin like the other icons
SUBJECT_FILL = 0.76


class AnimalPainter(FlatPainter):
    """
    The scripts draw every animal looking to the left. The painter mirrors each shape right before
    it is painted, so the animals look to the right and the crescent stays on the lower right.
    """

    def fill(
        self,
        mask,
        shade,
        clip=None,
    ):
        super().fill(mask=ImageOps.mirror(mask), shade=shade, clip=None if clip is None else ImageOps.mirror(clip))

    def fill_flat(
        self,
        mask,
        shade,
    ):
        super().fill_flat(mask=ImageOps.mirror(mask), shade=shade)

    def save_image(self, name):
        self._center_and_fit_subject()
        self.save(out_file=ANIMAL_OUT_DIR / f"{name}.png")

    def _center_and_fit_subject(self):
        """Scales the finished animal to a common size and centers it, so all icons sit alike in the gallery."""
        canvas = self._canvas
        bounds = canvas.getchannel("A").getbbox()

        if bounds is None:
            return

        subject = canvas.crop(bounds)
        scale = canvas.width * SUBJECT_FILL / max(subject.size)
        subject = subject.resize(
            (round(subject.width * scale), round(subject.height * scale)),
            Image.Resampling.LANCZOS,
        )
        centered = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        centered.paste(subject, ((canvas.width - subject.width) // 2, (canvas.height - subject.height) // 2))
        self._canvas = centered

    def blob(
        self,
        center,
        radius_x,
        radius_y,
        color,
        angle=0,
        clip=None,
    ):
        """A solid ellipse with a crescent (without crescent when it is clipped)."""
        self.fill_ellipse(center=center, radius_x=radius_x, radius_y=radius_y, shade=solid(color), angle=angle, clip=clip)

    def spot(
        self,
        center,
        radius_x,
        radius_y,
        color,
        angle=0,
    ):
        """A small flat ellipse without crescent: spots, cheeks, inner parts."""
        self.flat_ellipse(center=center, radius_x=radius_x, radius_y=radius_y, color=color, angle=angle)

    def body_curve(
        self,
        points,
        width,
        color,
        clip=None,
    ):
        self.fill_curve(points=points, width=width, shade=solid(color), clip=clip)

    def soft_polygon(
        self,
        points,
        color,
        softness=40,
        clip=None,
    ):
        """A polygon with rounded corners. The shape grows by half of the softness on every side."""
        self.fill(mask=self.build_soft_polygon_mask(points=points, softness=softness), shade=solid(color), clip=clip)

    def flat_soft_polygon(
        self,
        points,
        color,
        softness=30,
    ):
        self.fill_flat(mask=self.build_soft_polygon_mask(points=points, softness=softness), shade=solid(color))

    def build_soft_polygon_mask(
        self,
        points,
        softness,
    ):
        polygon_mask = self.build_polygon_mask(points=points)
        outline_mask = self.build_curve_mask(points=build_polyline_points(corners=[*points, points[0]]), width=softness)

        return self.union_masks(first_mask=polygon_mask, second_mask=outline_mask)

    def line(
        self,
        points,
        width,
        color,
    ):
        """A flat round-ended line through the points (no crescent)."""
        self.flat_curve(points=points, width=width, color=color)

    def arc_line(
        self,
        center,
        radius,
        start_angle,
        end_angle,
        width,
        color,
    ):
        """Angles in degrees: 0 is right, 90 is down, -90 is up."""
        points = build_arc_points(center=center, radius=radius, start_angle=start_angle, end_angle=end_angle)
        self.flat_curve(points=points, width=width, color=color)
