"""
Toast slice image, drawn from scratch.
Output: toast.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

CRUST = ((206, 134, 62), (166, 92, 38))
CRUMB = ((252, 214, 140), (236, 174, 88))
SPOT = ((222, 160, 80), (210, 140, 66))

BODY_LEFT, BODY_RIGHT = 200, 824
BODY_TOP, BODY_BOTTOM = 380, 840
CRUST_THICKNESS = 42


def build_toast_mask(
    painter,
    inset,
):
    """Two bumps on top of a body. inset shrinks the shape evenly."""
    left_bump = painter.build_rotated_ellipse_mask(center=(372, 390), radius_x=175 - inset, radius_y=150 - inset)
    right_bump = painter.build_rotated_ellipse_mask(center=(652, 390), radius_x=175 - inset, radius_y=150 - inset)
    body = painter.build_rounded_rect_mask(
        box=(BODY_LEFT + inset, BODY_TOP, BODY_RIGHT - inset, BODY_BOTTOM - inset),
        radius=70 - inset // 2,
    )
    outline = painter.union_all(masks=[left_bump, right_bump, body])

    return painter.round_corners(mask=outline, radius=34)


def paint_toast(painter):
    painter.fill(mask=build_toast_mask(painter=painter, inset=0), shade=CRUST)
    crumb_mask = build_toast_mask(painter=painter, inset=CRUST_THICKNESS)
    painter.fill(mask=crumb_mask, shade=CRUMB)

    for center in [(400, 560), (610, 500), (520, 700), (330, 720), (690, 690)]:
        painter.fill_ellipse(center=center, radius_x=22, radius_y=14, shade=SPOT, clip=crumb_mask)


def render_toast_image():
    painter = FoodPainter()
    paint_toast(painter)
    painter.save_image(name="toast")


if __name__ == "__main__":
    render_toast_image()
