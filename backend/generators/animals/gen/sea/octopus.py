"""
Octopus image, drawn from scratch.
Output: octopus.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, paint_eye_pair
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (178, 96, 200)
SUCKER = (236, 190, 244)
TENTACLE_OFFSETS = (-210, -125, -42, 42, 125, 210)


def build_tentacle_points(offset):
    side = -1 if offset < 0 else 1

    return sample_curve(
        start=(512 + offset * 0.8, 600),
        first_control=(512 + offset * 1.5, 800),
        second_control=(512 + offset * 2.0 - side * 60, 960),
        end=(512 + offset * 1.9 + side * 20, 840),
    )


def paint_tentacles(painter):
    widths = build_width_profile(stops=[(0.0, 100), (1.0, 26)])

    for offset in TENTACLE_OFFSETS:
        points = build_tentacle_points(offset=offset)
        painter.fill_tapered_curve(points=points, widths=widths, shade=solid(SKIN))

        for sucker_index in (45, 85, 125):
            painter.spot(center=points[sucker_index], radius_x=9, radius_y=9, color=SUCKER)


def paint_head(painter):
    painter.blob(center=(512, 400), radius_x=270, radius_y=290, color=SKIN)
    painter.spot(center=(380, 260), radius_x=34, radius_y=62, color=SUCKER, angle=25)
    paint_eye_pair(painter=painter, center_x=512, y=450, spread=125, radius=36)
    painter.arc_line(center=(512, 520), radius=60, start_angle=35, end_angle=145, width=13, color=EYE)


def render_octopus_image():
    painter = AnimalPainter()
    paint_tentacles(painter)
    paint_head(painter)
    painter.save_image(name="octopus")


if __name__ == "__main__":
    render_octopus_image()
