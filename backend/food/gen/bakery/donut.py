"""
Donut with pink icing and sprinkles, drawn from scratch.
Output: donut.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

DOUGH = ((236, 178, 106), (200, 136, 70))
ICING = ((252, 150, 188), (232, 100, 152))
SPRINKLE_COLORS = [
    ((255, 255, 255), (240, 240, 240)),
    ((255, 224, 80), (240, 190, 40)),
    ((90, 200, 240), (50, 150, 210)),
    ((140, 220, 120), (80, 180, 80)),
]

# (x, y, angle in degrees)
SPRINKLES = [
    (330, 400, 20), (440, 330, -40), (590, 320, 60), (700, 400, 10), (260, 520, 70),
    (760, 520, -30), (350, 640, -60), (690, 650, 40), (500, 700, 0), (420, 440, 80),
    (620, 440, -20), (560, 700, 50),
]


def build_hole_mask(painter):
    return painter.build_rotated_ellipse_mask(center=(512, 530), radius_x=100, radius_y=78)


def paint_dough(painter):
    outer_mask = painter.build_rotated_ellipse_mask(center=(512, 540), radius_x=340, radius_y=310)
    painter.fill(mask=painter.subtract_masks(base_mask=outer_mask, cut_mask=build_hole_mask(painter)), shade=DOUGH)


def paint_icing(painter):
    outer_mask = painter.build_rotated_ellipse_mask(center=(512, 510), radius_x=310, radius_y=268)
    icing_mask = painter.subtract_masks(base_mask=outer_mask, cut_mask=build_hole_mask(painter))
    painter.fill(mask=icing_mask, shade=ICING)

    return icing_mask


def paint_sprinkles(
    painter,
    icing_mask,
):
    for index, (x, y, angle) in enumerate(SPRINKLES):
        painter.fill_ellipse(
            center=(x, y),
            radius_x=28,
            radius_y=9,
            shade=SPRINKLE_COLORS[index % len(SPRINKLE_COLORS)],
            angle=angle,
            clip=icing_mask,
        )


def render_donut_image():
    painter = FoodPainter()
    paint_dough(painter)
    icing_mask = paint_icing(painter)
    paint_sprinkles(painter=painter, icing_mask=icing_mask)
    painter.save_image(name="donut")


if __name__ == "__main__":
    render_donut_image()
