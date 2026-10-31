"""
Popcorn bucket image, drawn from scratch.
Output: popcorn.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

BUCKET_RED = ((236, 66, 66), (180, 30, 44))
BUCKET_WHITE = ((255, 255, 255), (236, 232, 236))
KERNEL = ((255, 248, 226), (244, 222, 160))
KERNEL_SHADOW = ((236, 196, 120), (236, 196, 120))

BUCKET_TOP = 520
STRIPE_CENTERS = [330, 512, 694]
# (x, y, radius)
KERNELS = [
    (330, 440, 74), (450, 380, 82), (580, 380, 82), (700, 440, 74), (280, 520, 56),
    (740, 520, 56), (390, 480, 66), (520, 470, 70), (640, 490, 64), (500, 300, 60),
]


def paint_kernels(painter):
    for x, y, radius in KERNELS:
        painter.fill_circle(center=(x, y), radius=radius + 8, shade=KERNEL_SHADOW)
        painter.fill_circle(center=(x, y), radius=radius, shade=KERNEL)


def paint_bucket(painter):
    bucket_mask = painter.build_polygon_mask(points=[(260, BUCKET_TOP), (764, BUCKET_TOP), (690, 890), (334, 890)])
    painter.fill(mask=bucket_mask, shade=BUCKET_RED)

    for center_x in STRIPE_CENTERS:
        tilt = (center_x - 512) * 0.18
        painter.fill_stroke(start=(center_x, BUCKET_TOP), end=(center_x - tilt, 890), width=78, shade=BUCKET_WHITE, clip=bucket_mask)


def render_popcorn_image():
    painter = FoodPainter()
    paint_kernels(painter)
    paint_bucket(painter)
    painter.save_image(name="popcorn")


if __name__ == "__main__":
    render_popcorn_image()
