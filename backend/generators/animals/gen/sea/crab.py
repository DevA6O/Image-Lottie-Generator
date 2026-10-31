"""
Crab image, drawn from scratch.
Output: crab.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import solid

SHELL = (236, 84, 62)
LEG = (206, 62, 52)
CLAW = (246, 104, 72)
EYE_WHITE = (255, 255, 255)


def paint_legs_and_arms(painter):
    for side in (-1, 1):
        for leg_index in range(3):
            start = (512 + side * (170 + leg_index * 40), 640 + leg_index * 20)
            end = (512 + side * (400 + leg_index * 20), 700 + leg_index * 70)
            painter.line(points=[start, (start[0] + side * 110, start[1] - 40), end], width=34, color=LEG)

        painter.line(points=[(512 + side * 190, 560), (512 + side * 300, 470), (512 + side * 310, 380)], width=48, color=LEG)


def paint_claws(painter):
    for side in (-1, 1):
        claw_center = (512 + side * 320, 300)
        notch_points = [(claw_center[0], claw_center[1] - 10), (claw_center[0] - side * 30, claw_center[1] - 140), (claw_center[0] + side * 60, claw_center[1] - 110)]
        claw_mask = painter.subtract_masks(
            base_mask=painter.build_rotated_ellipse_mask(center=claw_center, radius_x=100, radius_y=90),
            cut_mask=painter.build_polygon_mask(points=notch_points),
        )
        painter.fill(mask=claw_mask, shade=solid(CLAW))


def paint_body(painter):
    for side in (-1, 1):
        painter.line(points=[(512 + side * 75, 470), (512 + side * 85, 400)], width=26, color=LEG)
        painter.spot(center=(512 + side * 85, 385), radius_x=38, radius_y=38, color=EYE_WHITE)
        painter.spot(center=(512 + side * 85, 390), radius_x=20, radius_y=20, color=EYE)

    painter.blob(center=(512, 620), radius_x=270, radius_y=180, color=SHELL)
    painter.arc_line(center=(512, 660), radius=90, start_angle=30, end_angle=150, width=14, color=EYE)


def render_crab_image():
    painter = AnimalPainter()
    paint_legs_and_arms(painter)
    paint_body(painter)
    paint_claws(painter)
    painter.save_image(name="crab")


if __name__ == "__main__":
    render_crab_image()
