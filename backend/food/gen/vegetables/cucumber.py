"""
Cucumber with a slice, drawn from scratch.
Output: cucumber.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter

SKIN = ((96, 186, 84), (44, 126, 58))
STRIPE = ((150, 214, 120), (150, 214, 120))
SLICE_RIM = ((60, 140, 66), (40, 110, 52))
SLICE_FLESH = ((226, 246, 190), (190, 226, 150))
SEED = ((246, 252, 214), (246, 252, 214))

SEED_POSITIONS = [(0, -62), (54, -30), (54, 30), (0, 62), (-54, 30), (-54, -30)]
SLICE_CENTER = (700, 710)


def paint_cucumber(painter):
    cucumber_mask = painter.build_stroke_mask(start=(220, 640), end=(800, 280), width=190)
    painter.fill(mask=cucumber_mask, shade=SKIN)
    painter.fill_stroke(start=(250, 600), end=(780, 270), width=14, shade=STRIPE, clip=cucumber_mask)
    painter.fill_stroke(start=(250, 690), end=(780, 360), width=14, shade=STRIPE, clip=cucumber_mask)


def paint_slice(painter):
    painter.fill_circle(center=SLICE_CENTER, radius=160, shade=SLICE_RIM)
    painter.fill_circle(center=SLICE_CENTER, radius=136, shade=SLICE_FLESH)

    for offset_x, offset_y in SEED_POSITIONS:
        center = (SLICE_CENTER[0] + offset_x, SLICE_CENTER[1] + offset_y)
        painter.fill_ellipse(center=center, radius_x=16, radius_y=26, shade=SEED)


def render_cucumber_image():
    painter = FoodPainter()
    paint_cucumber(painter)
    paint_slice(painter)
    painter.save_image(name="cucumber")


if __name__ == "__main__":
    render_cucumber_image()
