"""
Soda can image, drawn from scratch.
Output: soda.png (1024x1024, transparent background) in frontend/results/food
"""
from food.food_painter import FoodPainter
from painting.flat_painter import sample_curve

CAN = ((240, 60, 60), (166, 22, 38))
METAL = ((236, 240, 246), (166, 174, 190))
WAVE = ((255, 255, 255), (240, 240, 244))
SHINE = ((255, 150, 150), (255, 130, 130))

CAN_LEFT, CAN_RIGHT = 330, 694
CAN_TOP, CAN_BOTTOM = 250, 850
RIM_RADIUS_Y = 40


def paint_body(painter):
    painter.fill_rounded_rect(box=(CAN_LEFT, CAN_TOP, CAN_RIGHT, CAN_BOTTOM), radius=36, shade=CAN)
    wave_points = sample_curve(start=(CAN_LEFT, 600), first_control=(430, 480), second_control=(600, 720), end=(CAN_RIGHT, 580))
    painter.fill_curve(points=wave_points, width=84, shade=WAVE)
    painter.fill_stroke(start=(380, 330), end=(380, 800), width=22, shade=SHINE)


def paint_lids(painter):
    painter.fill_ellipse(center=(512, CAN_TOP + 10), radius_x=(CAN_RIGHT - CAN_LEFT) / 2, radius_y=RIM_RADIUS_Y, shade=METAL)
    painter.fill_ellipse(center=(512, CAN_TOP + 10), radius_x=130, radius_y=24, shade=CAN)
    painter.fill_rounded_rect(box=(CAN_LEFT, CAN_BOTTOM - 20, CAN_RIGHT, CAN_BOTTOM + 14), radius=14, shade=METAL)


def render_soda_image():
    painter = FoodPainter()
    paint_body(painter)
    paint_lids(painter)
    painter.save_image(name="soda")


if __name__ == "__main__":
    render_soda_image()
