"""
Lobster image, drawn from scratch.
Output: lobster.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import solid

SHELL = (210, 62, 54)
SHELL_LIGHT = (232, 96, 78)
LEG = (180, 48, 46)
SEGMENT_CENTERS = (480, 575, 670, 765)


def paint_legs_and_antennae(painter):
    for side in (-1, 1):
        for leg_y in (330, 390, 450):
            painter.line(points=[(512 + side * 80, leg_y), (512 + side * 190, leg_y + 30)], width=20, color=LEG)

        painter.line(points=[(512 + side * 40, 250), (512 + side * 160, 130), (512 + side * 120, 40)], width=12, color=LEG)


def paint_claws(painter):
    for side in (-1, 1):
        painter.line(points=[(512 + side * 100, 360), (512 + side * 240, 270)], width=60, color=SHELL)
        claw_center = (512 + side * 270, 200)
        notch_points = [(claw_center[0], claw_center[1] - 20), (claw_center[0] - side * 20, claw_center[1] - 150), (claw_center[0] + side * 50, claw_center[1] - 110)]
        claw_mask = painter.subtract_masks(
            base_mask=painter.build_rotated_ellipse_mask(center=claw_center, radius_x=70, radius_y=120, angle=side * 28),
            cut_mask=painter.build_polygon_mask(points=notch_points),
        )
        painter.fill(mask=claw_mask, shade=solid(SHELL_LIGHT))


def paint_body(painter):
    for center_y in SEGMENT_CENTERS:
        painter.blob(center=(512, center_y), radius_x=118 - (center_y - 480) * 0.12, radius_y=62, color=SHELL)

    painter.blob(center=(512, 400), radius_x=100, radius_y=170, color=SHELL_LIGHT)

    for fan_angle in (-34, 0, 34):
        painter.blob(center=(512 + fan_angle * 2.6, 880), radius_x=44, radius_y=88, color=SHELL_LIGHT, angle=fan_angle)

    for side in (-1, 1):
        painter.spot(center=(512 + side * 38, 305), radius_x=18, radius_y=18, color=EYE)


def render_lobster_image():
    painter = AnimalPainter()
    paint_legs_and_antennae(painter)
    paint_claws(painter)
    paint_body(painter)
    painter.save_image(name="lobster")


if __name__ == "__main__":
    render_lobster_image()
