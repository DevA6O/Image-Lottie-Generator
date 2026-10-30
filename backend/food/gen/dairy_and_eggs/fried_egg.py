"""
Fried egg image, drawn from scratch.
Output: fried_egg.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

WHITE = ((255, 255, 255), (232, 232, 238))
YOLK = ((255, 208, 52), (244, 148, 20))
YOLK_SHINE = ((255, 246, 190), (255, 240, 170))

# (x, y, radius): overlapping circles make the uneven shape of the egg white
WHITE_BLOBS = [(380, 480, 210), (620, 420, 200), (660, 640, 190), (400, 680, 190), (520, 550, 250)]


def paint_egg_white(painter):
    blobs = [
        painter.build_rotated_ellipse_mask(center=(x, y), radius_x=radius, radius_y=radius)
        for x, y, radius in WHITE_BLOBS
    ]
    painter.fill(mask=painter.round_corners(mask=painter.union_all(masks=blobs), radius=40), shade=WHITE)


def paint_yolk(painter):
    painter.fill_circle(center=(500, 540), radius=140, shade=YOLK)
    painter.fill_ellipse(center=(450, 480), radius_x=44, radius_y=24, shade=YOLK_SHINE, angle=-35)


def render_fried_egg_image():
    painter = FoodPainter()
    paint_egg_white(painter)
    paint_yolk(painter)
    painter.save_image(name="fried_egg")


if __name__ == "__main__":
    render_fried_egg_image()
