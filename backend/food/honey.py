"""
Honey jar image, drawn from scratch.
Output: honey.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter, build_star_points

JAR = ((255, 200, 70), (226, 142, 22))
LID = ((176, 112, 60), (130, 78, 40))
LABEL = ((255, 246, 220), (240, 224, 186))
COMB = ((255, 200, 60), (240, 160, 24))
SHINE = ((255, 232, 150), (255, 224, 130))


def paint_jar(painter):
    jar_mask = painter.build_rounded_rect_mask(box=(280, 380, 744, 870), radius=90)
    painter.fill(mask=jar_mask, shade=JAR)
    painter.fill_ellipse(center=(350, 560), radius_x=22, radius_y=100, shade=SHINE, clip=jar_mask)


def paint_lid(painter):
    painter.fill_rounded_rect(box=(310, 290, 714, 410), radius=34, shade=LID)


def paint_label(painter):
    painter.fill_rounded_rect(box=(350, 520, 674, 760), radius=36, shade=LABEL)
    hexagon_points = build_star_points(center=(512, 640), outer_radius=70, inner_radius=70, tip_count=3)
    painter.fill_polygon(points=hexagon_points, shade=COMB)


def render_honey_image():
    painter = FoodPainter()
    paint_jar(painter)
    paint_lid(painter)
    paint_label(painter)
    painter.save_image(name="honey")


if __name__ == "__main__":
    render_honey_image()
