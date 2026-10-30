"""
Avocado half with pit, drawn from scratch.
Output: avocado.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

SKIN = ((70, 120, 50), (36, 74, 36))
FLESH = ((226, 240, 130), (170, 204, 80))
FLESH_RIM = ((120, 170, 60), (96, 146, 50))
PIT = ((166, 100, 60), (104, 58, 34))
PIT_SHINE = ((210, 150, 110), (200, 140, 100))


def build_avocado_mask(
    painter,
    inset,
):
    return painter.build_pear_mask(
        center_x=512,
        top_center_y=400,
        top_radius=165 - inset,
        bottom_center_y=630,
        bottom_radius=260 - inset,
    )


def paint_avocado(painter):
    painter.fill(mask=build_avocado_mask(painter=painter, inset=0), shade=SKIN)
    painter.fill(mask=build_avocado_mask(painter=painter, inset=26), shade=FLESH_RIM)
    painter.fill(mask=build_avocado_mask(painter=painter, inset=56), shade=FLESH)


def paint_pit(painter):
    painter.fill_circle(center=(512, 660), radius=125, shade=PIT)
    painter.fill_ellipse(center=(468, 612), radius_x=34, radius_y=18, shade=PIT_SHINE, angle=-40)


def render_avocado_image():
    painter = FoodPainter()
    paint_avocado(painter)
    paint_pit(painter)
    painter.save_image(name="avocado")


if __name__ == "__main__":
    render_avocado_image()
