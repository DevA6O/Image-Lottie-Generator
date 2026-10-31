"""
Lizard image, drawn from scratch.
Output: lizard.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (132, 192, 76)
STRIPE = (86, 146, 64)
LEG_WIDTH = 42


def paint_legs(painter, points):
    for point_index, spread in ((55, 150), (115, 160)):
        x, y = points[point_index]

        for side in (-1, 1):
            knee = (x + side * spread, y - 30)
            foot = (x + side * (spread + 50), y + 50)
            painter.line(points=[(x, y), knee, foot], width=LEG_WIDTH, color=SKIN)
            painter.blob(center=(foot[0] + side * 15, foot[1] + 20), radius_x=36, radius_y=30, color=SKIN)


def paint_body(painter, points):
    widths = build_width_profile(stops=[(0.0, 60), (0.08, 120), (0.2, 110), (0.35, 170), (0.6, 150), (0.8, 70), (1.0, 12)])
    body_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=body_mask, shade=solid(SKIN))
    painter.fill_curve(points=points[10:150], width=32, shade=solid(STRIPE), clip=body_mask)


def paint_eyes(painter, points):
    x, y = points[16]

    for side in (-1, 1):
        painter.blob(center=(x + side * 48, y - 6), radius_x=30, radius_y=30, color=SKIN)
        painter.spot(center=(x + side * 48, y - 6), radius_x=14, radius_y=14, color=EYE)


def render_lizard_image():
    painter = AnimalPainter()
    points = sample_curve(start=(450, 130), first_control=(430, 480), second_control=(660, 620), end=(540, 960))
    paint_legs(painter, points=points)
    paint_body(painter, points=points)
    paint_eyes(painter, points=points)
    painter.save_image(name="lizard")


if __name__ == "__main__":
    render_lizard_image()
