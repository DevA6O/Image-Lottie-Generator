"""
Scene for the irregular verb "draw" (drew, drawn).
Output: draw_infinitive.png, draw_past.png and draw_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from painting.flat_painter import solid
from verbs.props import BROWN, GOLD, draw_heart, draw_pencil, draw_star, draw_sun
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock

CANVAS_BOX = (342, 270, 682, 590)    # left, top, right, bottom
CANVAS_BORDER = 10
EASEL_TOP = (512, 450)    # Hidden behind the canvas, so the legs come out under it
TRAY_HEIGHT = 26
EASEL_FOOT_XS = (392, 512, 632)
FLOOR_Y = 836
PENCIL_SIZE = 0.6
PENCIL_ANGLE = -65    # The eraser points up and to the right
PENCIL_TIP_ON_CANVAS = (590, 545)
PAPER_COLOR = (250, 250, 255)


def paint_draw_scene(painter, form):
    for foot_x in EASEL_FOOT_XS:
        painter.fill_stroke(start=EASEL_TOP, end=(foot_x, FLOOR_Y), width=16, shade=solid(BROWN))

    painter.fill_rounded_rect(
        box=(CANVAS_BOX[0] - 16, CANVAS_BOX[3] - 6, CANVAS_BOX[2] + 16, CANVAS_BOX[3] + TRAY_HEIGHT),
        radius=8,
        shade=solid(BROWN),
    )
    frame_color = GOLD if form == PARTICIPLE else PAPER_COLOR
    painter.fill_rounded_rect(box=CANVAS_BOX, radius=8, shade=solid(frame_color))
    painter.fill_rounded_rect(
        box=(CANVAS_BOX[0] + CANVAS_BORDER, CANVAS_BOX[1] + CANVAS_BORDER, CANVAS_BOX[2] - CANVAS_BORDER, CANVAS_BOX[3] - CANVAS_BORDER),
        radius=6,
        shade=solid(PAPER_COLOR),
    )
    draw_pencil(painter=painter, tip=PENCIL_TIP_ON_CANVAS, angle=PENCIL_ANGLE, size=PENCIL_SIZE)

    if form == PAST:
        draw_sun(painter=painter, center=(470, 410), radius=50)
        paint_past_clock(painter=painter, center=(800, 230))
    elif form == PARTICIPLE:
        draw_sun(painter=painter, center=(440, 390), radius=44)
        draw_heart(painter=painter, center=(500, 490), size=40)
        draw_star(painter=painter, center=(720, 290), size=34)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="draw", paint_scene=paint_draw_scene)
