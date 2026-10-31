"""
Crocodile image, drawn from scratch.
Output: crocodile.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (92, 156, 90)
SKIN_DARK = (62, 118, 74)
BELLY = (206, 218, 142)
TOOTH = (255, 252, 240)
MOUTH = (150, 62, 70)


def build_body_points():
    return sample_curve(start=(950, 700), first_control=(700, 700), second_control=(500, 520), end=(130, 560))


def paint_legs(painter):
    for leg_x in (500, 680):
        painter.blob(center=(leg_x, 720), radius_x=62, radius_y=110, color=SKIN_DARK, angle=-14)
        painter.blob(center=(leg_x - 40, 810), radius_x=52, radius_y=26, color=SKIN_DARK)


def paint_body(painter):
    points = build_body_points()
    widths = build_width_profile(stops=[(0.0, 30), (0.35, 160), (0.6, 210), (0.8, 140), (1.0, 120)])
    body_mask = painter.build_tapered_curve_mask(points=points, widths=widths)
    painter.fill(mask=body_mask, shade=solid(SKIN))

    belly_points = [(x, y + 80) for x, y in points[40:150]]
    painter.fill_curve(points=belly_points, width=44, shade=solid(BELLY), clip=body_mask)

    for ridge_index in range(25, 110, 12):
        x, y = points[ridge_index]
        painter.soft_polygon(points=[(x - 28, y - 85), (x, y - 130), (x + 28, y - 85)], color=SKIN_DARK, softness=12)


def paint_head_details(painter):
    painter.blob(center=(300, 470), radius_x=48, radius_y=46, color=SKIN)
    painter.spot(center=(296, 472), radius_x=18, radius_y=18, color=EYE)
    painter.line(points=[(130, 580), (230, 590), (400, 600)], width=12, color=MOUTH)

    for tooth_x in (160, 215, 270):
        painter.flat_soft_polygon(points=[(tooth_x - 14, 580), (tooth_x + 14, 584), (tooth_x, 618)], color=TOOTH, softness=6)


def render_crocodile_image():
    painter = AnimalPainter()
    paint_legs(painter)
    paint_body(painter)
    paint_head_details(painter)
    painter.save_image(name="crocodile")


if __name__ == "__main__":
    render_crocodile_image()
