"""
Butterfly image, drawn from scratch.
Output: butterfly.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from painting.flat_painter import solid

UPPER_WING = (250, 132, 52)
LOWER_WING = (255, 184, 66)
WING_TIP = (92, 56, 60)
SPOT = (255, 248, 236)
BODY = (80, 56, 64)


def paint_wings(painter):
    for side in (-1, 1):
        lower_mask = painter.build_rotated_ellipse_mask(center=(512 + side * 150, 670), radius_x=165, radius_y=125, angle=side * 22)
        painter.fill(mask=lower_mask, shade=solid(LOWER_WING))
        painter.fill_ellipse(center=(512 + side * 215, 740), radius_x=90, radius_y=70, shade=solid(UPPER_WING), clip=lower_mask)

        upper_mask = painter.build_rotated_ellipse_mask(center=(512 + side * 205, 400), radius_x=225, radius_y=160, angle=-side * 28)
        painter.fill(mask=upper_mask, shade=solid(UPPER_WING))
        painter.fill_ellipse(center=(512 + side * 330, 310), radius_x=130, radius_y=100, shade=solid(WING_TIP), clip=upper_mask, angle=-side * 28)

        for spot_x, spot_y, spot_radius in ((340, 285, 24), (385, 345, 18), (300, 350, 14)):
            painter.spot(center=(512 + side * spot_x - side * 20, spot_y), radius_x=spot_radius, radius_y=spot_radius, color=SPOT)


def paint_body(painter):
    for side in (-1, 1):
        painter.line(points=[(512 + side * 18, 300), (512 + side * 70, 190), (512 + side * 150, 130)], width=12, color=BODY)
        painter.blob(center=(512 + side * 155, 125), radius_x=20, radius_y=20, color=BODY)

    painter.blob(center=(512, 560), radius_x=40, radius_y=235, color=BODY)
    painter.blob(center=(512, 330), radius_x=52, radius_y=52, color=BODY)


def render_butterfly_image():
    painter = AnimalPainter()
    paint_wings(painter)
    paint_body(painter)
    painter.save_image(name="butterfly")


if __name__ == "__main__":
    render_butterfly_image()
