"""
Pigeon image, drawn from scratch.
Output: pigeon.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.bird_shape import HEAD_CENTER, draw_perched_bird

BODY = (150, 158, 176)
BELLY = (178, 186, 200)
WING = (118, 126, 146)
TAIL = (96, 102, 122)
BEAK = (240, 214, 200)
LEG = (226, 108, 122)
EYE_RING = (246, 150, 60)
NECK_SHEEN = (96, 178, 158)
WING_BAR = (70, 76, 96)


def render_pigeon_image():
    painter = AnimalPainter()
    draw_perched_bird(
        painter=painter,
        body_color=BODY,
        belly_color=BELLY,
        wing_color=WING,
        tail_color=TAIL,
        beak_color=BEAK,
        leg_color=LEG,
        tail_length=150,
        beak_length=50,
        eye_ring_color=EYE_RING,
    )
    painter.spot(center=(HEAD_CENTER[0] + 70, HEAD_CENTER[1] + 100), radius_x=70, radius_y=36, color=NECK_SHEEN, angle=35)
    painter.line(points=[(520, 560), (620, 610)], width=16, color=WING_BAR)
    painter.line(points=[(560, 520), (670, 580)], width=16, color=WING_BAR)
    painter.save_image(name="pigeon")


if __name__ == "__main__":
    render_pigeon_image()
