"""
Potato image, drawn from scratch.
Output: potato.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

POTATO = ((226, 184, 116), (178, 128, 68))
SHINE = ((244, 214, 160), (238, 204, 146))
EYE = ((140, 94, 50), (140, 94, 50))

# (x, y, half width, half height, angle in degrees): overlapping lumps make the uneven shape
LUMPS = [(500, 540, 330, 230, -15), (330, 520, 200, 190, 20), (690, 620, 200, 180, -30), (520, 680, 260, 160, 10)]
EYES = [(380, 480), (620, 560), (500, 700), (700, 700), (330, 640)]


def paint_potato(painter):
    lump_masks = [
        painter.build_rotated_ellipse_mask(center=(x, y), radius_x=radius_x, radius_y=radius_y, angle=angle)
        for x, y, radius_x, radius_y, angle in LUMPS
    ]
    potato_mask = painter.round_corners(mask=painter.union_all(masks=lump_masks), radius=40)
    painter.fill(mask=potato_mask, shade=POTATO)
    painter.fill_ellipse(center=(420, 400), radius_x=100, radius_y=28, shade=SHINE, angle=-15, clip=potato_mask)

    for center in EYES:
        painter.fill_ellipse(center=center, radius_x=18, radius_y=11, shade=EYE, angle=center[0] % 60, clip=potato_mask)


def render_potato_image():
    painter = FoodPainter()
    paint_potato(painter)
    painter.save_image(name="potato")


if __name__ == "__main__":
    render_potato_image()
