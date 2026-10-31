"""
Harbor seal image, drawn from scratch.
Output: harbor_seal.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from painting.flat_painter import build_width_profile, sample_curve, solid

SKIN = (176, 160, 142)
BELLY = (238, 228, 212)
SPOT = (112, 98, 90)
FLIPPER = (140, 126, 114)
WHISKER = (252, 250, 244)
BODY_WIDTHS = [(0.0, 40), (0.3, 230), (0.7, 250), (1.0, 150)]
SPOT_POSITIONS = ((520, 700), (600, 640), (680, 730), (440, 760), (560, 780), (760, 700), (640, 800))


def paint_flippers(painter):
    painter.blob(center=(900, 800), radius_x=70, radius_y=130, color=FLIPPER, angle=-70)
    painter.blob(center=(880, 700), radius_x=60, radius_y=120, color=FLIPPER, angle=-95)


def paint_body(painter):
    points = sample_curve(start=(880, 780), first_control=(700, 800), second_control=(500, 800), end=(330, 640))
    body_mask = painter.build_tapered_curve_mask(points=points, widths=build_width_profile(stops=BODY_WIDTHS))
    painter.fill(mask=body_mask, shade=solid(SKIN))
    painter.fill_curve(points=[(x - 10, y + 100) for x, y in points[40:140]], width=90, shade=solid(BELLY), clip=body_mask)

    for spot_center in SPOT_POSITIONS:
        painter.fill_ellipse(center=spot_center, radius_x=26, radius_y=20, shade=solid(SPOT), clip=body_mask)

    painter.blob(center=(470, 840), radius_x=40, radius_y=100, color=FLIPPER, angle=-25)


def paint_head(painter):
    painter.blob(center=(300, 470), radius_x=145, radius_y=140, color=SKIN)
    painter.blob(center=(215, 520), radius_x=95, radius_y=70, color=BELLY, angle=15)
    painter.blob(center=(150, 505), radius_x=34, radius_y=26, color=NOSE)

    painter.spot(center=(290, 420), radius_x=28, radius_y=28, color=EYE)
    painter.spot(center=(283, 411), radius_x=9, radius_y=9, color=(255, 255, 255))

    for whisker_end in (-20, 30):
        painter.line(points=[(185, 525), (110, 525 + whisker_end)], width=8, color=WHISKER)


def render_harbor_seal_image():
    painter = AnimalPainter()
    paint_flippers(painter)
    paint_body(painter)
    paint_head(painter)
    painter.save_image(name="harbor_seal")


if __name__ == "__main__":
    render_harbor_seal_image()
