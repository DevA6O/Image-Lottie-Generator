"""
Scene for the irregular verb "do" (did, done).
Output: do_infinitive.png, do_past.png and do_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from verbs.props import draw_clipboard, draw_pencil, draw_trophy
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock

CLIPBOARD_CENTER = (512, 580)
CLIPBOARD_SIZE = (340, 460)
ROW_COUNT = 3
FIRST_ROW_OFFSET = 80    # From the clipboard top, as in draw_clipboard
ROW_TEXT_OFFSET = 240    # From the clipboard left edge to the end of a written line
PENCIL_SIZE = 0.6
PENCIL_ANGLE = -65    # The eraser points up and to the right


def paint_do_scene(painter, form):
    checked_count = (0, 2, 3)[form]
    draw_clipboard(
        painter=painter,
        center=CLIPBOARD_CENTER,
        width=CLIPBOARD_SIZE[0],
        height=CLIPBOARD_SIZE[1],
        row_count=ROW_COUNT,
        checked_count=checked_count,
    )
    paint_pencil_on_row(painter=painter, row=min(checked_count, ROW_COUNT - 1))

    if form == PAST:
        paint_past_clock(painter=painter, center=(CLIPBOARD_CENTER[0], 170))
    elif form == PARTICIPLE:
        draw_trophy(painter=painter, center=(CLIPBOARD_CENTER[0], 220), size=0.8)


def paint_pencil_on_row(
    painter,
    row,
):
    top = CLIPBOARD_CENTER[1] - CLIPBOARD_SIZE[1] / 2
    left = CLIPBOARD_CENTER[0] - CLIPBOARD_SIZE[0] / 2
    row_spacing = (CLIPBOARD_SIZE[1] - 120) / (ROW_COUNT - 1)
    tip = (left + ROW_TEXT_OFFSET, top + FIRST_ROW_OFFSET + row * row_spacing)
    draw_pencil(painter=painter, tip=tip, angle=PENCIL_ANGLE, size=PENCIL_SIZE)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="do", paint_scene=paint_do_scene)
