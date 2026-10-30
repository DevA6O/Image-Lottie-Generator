"""
Eggplant image, drawn from scratch.
Output: eggplant.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, build_width_profile, sample_curve

EGGPLANT = ((156, 84, 176), (58, 24, 90))
SHINE = ((214, 168, 230), (200, 148, 220))
CAP = ((128, 196, 84), (62, 132, 52))
CAP_DARK = ((92, 164, 70), (48, 112, 44))

CENTER_X = 512
SEPAL_WIDTHS = [(0.0, 56), (0.5, 48), (1.0, 6)]

# Each sepal: start, first control, second control, end. They hang down over the body.
SEPALS = [
    ((CENTER_X - 76, 285), (CENTER_X - 82, 330), (CENTER_X - 92, 370), (CENTER_X - 110, 415)),
    ((CENTER_X + 76, 285), (CENTER_X + 82, 330), (CENTER_X + 92, 370), (CENTER_X + 110, 415)),
    ((CENTER_X, 300), (CENTER_X, 350), (CENTER_X, 400), (CENTER_X, 445)),
]


def paint_body(painter):
    body_mask = painter.build_pear_mask(
        center_x=CENTER_X,
        top_center_y=340,
        top_radius=88,
        bottom_center_y=690,
        bottom_radius=170,
    )
    painter.fill(mask=body_mask, shade=EGGPLANT)

    shine_points = sample_curve(
        start=(CENTER_X - 105, 560),
        first_control=(CENTER_X - 125, 620),
        second_control=(CENTER_X - 125, 690),
        end=(CENTER_X - 100, 750),
    )
    painter.fill_curve(points=shine_points, width=24, shade=SHINE, clip=body_mask)


def paint_cap(painter):
    sepal_widths = build_width_profile(stops=SEPAL_WIDTHS)

    for start, first_control, second_control, end in SEPALS:
        points = sample_curve(start=start, first_control=first_control, second_control=second_control, end=end)
        painter.fill_tapered_curve(points=points, widths=sepal_widths, shade=CAP_DARK, round_ends=False)

    painter.fill_ellipse(center=(CENTER_X, 272), radius_x=124, radius_y=50, shade=CAP)
    painter.fill_stroke(start=(CENTER_X, 262), end=(CENTER_X + 18, 150), width=46, shade=CAP_DARK)


def render_eggplant_image():
    painter = FoodPainter()
    paint_body(painter)
    paint_cap(painter)
    painter.save_image(name="eggplant")


if __name__ == "__main__":
    render_eggplant_image()
