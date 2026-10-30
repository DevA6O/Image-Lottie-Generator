"""
Peanut in its shell, drawn from scratch.
Output: peanut.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

SHELL = ((236, 200, 138), (196, 148, 84))
DOT = ((176, 126, 66), (176, 126, 66))

TILT_DEGREES = -35
# (x, y) of the texture dots
DOTS = [
    (330, 640), (400, 700), (300, 560), (430, 600), (480, 520), (520, 440), (590, 560),
    (640, 420), (560, 360), (700, 330), (660, 500), (440, 650),
]


def paint_peanut(painter):
    lower_lobe = painter.build_rotated_ellipse_mask(center=(380, 640), radius_x=200, radius_y=170, angle=TILT_DEGREES)
    upper_lobe = painter.build_rotated_ellipse_mask(center=(640, 390), radius_x=210, radius_y=180, angle=TILT_DEGREES)
    waist = painter.build_rotated_ellipse_mask(center=(510, 515), radius_x=130, radius_y=100, angle=TILT_DEGREES)
    peanut_mask = painter.round_corners(mask=painter.union_all(masks=[lower_lobe, upper_lobe, waist]), radius=40)
    painter.fill(mask=peanut_mask, shade=SHELL)

    for center in DOTS:
        painter.fill_circle(center=center, radius=7, shade=DOT, clip=peanut_mask)


def render_peanut_image():
    painter = FoodPainter()
    paint_peanut(painter)
    painter.save_image(name="peanut")


if __name__ == "__main__":
    render_peanut_image()
