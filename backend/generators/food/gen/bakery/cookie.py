"""
Chocolate chip cookie with a bite taken out, drawn from scratch.
Output: cookie.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

DOUGH = ((236, 184, 112), (194, 138, 70))
EDGE = ((206, 150, 82), (176, 120, 58))
CHIP = ((104, 62, 40), (60, 32, 22))

# (x, y, half width, half height, angle in degrees)
CHIPS = [
    (400, 360, 52, 38, 20), (600, 520, 58, 40, -30), (330, 600, 50, 36, 50),
    (520, 700, 56, 38, 10), (680, 700, 40, 30, -40), (480, 480, 34, 24, 70),
    (250, 440, 34, 26, -20), (690, 360, 34, 26, 30),
]


def build_cookie_mask(painter):
    whole_cookie = painter.build_rotated_ellipse_mask(center=(512, 520), radius_x=340, radius_y=330)
    bite = painter.build_rotated_ellipse_mask(center=(800, 250), radius_x=140, radius_y=130)

    return painter.subtract_masks(base_mask=whole_cookie, cut_mask=bite)


def paint_cookie(painter):
    cookie_mask = build_cookie_mask(painter)
    painter.fill(mask=cookie_mask, shade=EDGE)

    # Slightly smaller and lighter inside: gives the baked edge
    inner = painter.build_rotated_ellipse_mask(center=(512, 510), radius_x=306, radius_y=296)
    painter.fill(mask=inner, shade=DOUGH, clip=cookie_mask)

    for x, y, radius_x, radius_y, angle in CHIPS:
        painter.fill_ellipse(center=(x, y), radius_x=radius_x, radius_y=radius_y, shade=CHIP, angle=angle, clip=cookie_mask)


def render_cookie_image():
    painter = FoodPainter()
    paint_cookie(painter)
    painter.save_image(name="cookie")


if __name__ == "__main__":
    render_cookie_image()
