"""
Raven image, drawn from scratch.
Output: raven.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

BODY = (66, 66, 96)
BELLY = (84, 84, 118)
WING = (46, 46, 72)
BEAK = (28, 28, 38)
LEG = (70, 66, 80)


def paint_shaggy_throat(painter):
    """Ravens have long pointed feathers under the beak."""
    throat_points = [(HEAD_CENTER[0] - 70, HEAD_CENTER[1] + 90), (HEAD_CENTER[0] - 40, HEAD_CENTER[1] + 190), (HEAD_CENTER[0] + 10, HEAD_CENTER[1] + 110), (HEAD_CENTER[0] + 50, HEAD_CENTER[1] + 195), (HEAD_CENTER[0] + 90, HEAD_CENTER[1] + 90)]
    painter.soft_polygon(points=throat_points, color=BODY, softness=16)


def render_raven_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=WING,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=230,
        hooked_beak=True,
        beak_length=105,
        eye_ring_color=(120, 120, 150),
    )
    paint_shaggy_throat(painter)
    painter.save_image(name="raven")


if __name__ == "__main__":
    render_raven_image()
