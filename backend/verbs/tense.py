"""
The three verb forms. A form is never written as text:
- infinitive: the action itself, just starting or going on
- past: the action at a moment in the past, always with a clock
- past participle: the result after the action
"""
from verbs.props import draw_clock

INFINITIVE = 0
PAST = 1
PARTICIPLE = 2

PAST_CLOCK_CENTER = (800, 230)


def paint_past_clock(
    painter,
    center=PAST_CLOCK_CENTER,
):
    draw_clock(painter=painter, center=center, size=1.0)
