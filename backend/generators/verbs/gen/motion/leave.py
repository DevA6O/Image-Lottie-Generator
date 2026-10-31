"""
Scene for the irregular verb "leave" (left, left).
Output: leave_infinitive.png, leave_past.png and leave_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from painting.flat_painter import solid
from verbs.props import draw_door, draw_footprints
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock

SUITCASE_COLOR = (184, 100, 70)
SUITCASE_HANDLE_COLOR = (120, 70, 50)
SUITCASE_HALF_WIDTH = 58
SUITCASE_HALF_HEIGHT = 46
SUITCASE_HANDLE_RADIUS = 32
SUITCASE_HANDLE_GAP = 6    # Ring center above the suitcase top; the hand grips the ring top
TRAVELING_POSE = Pose(
    lean=4,
    head_tilt=-6,
    left_arm=(-28, 0),
    right_arm=(125, 30),
    left_leg=(-6, 0),
    right_leg=(22, -12),
    eyes="happy",
)


def paint_leave_scene(painter, form):
    draw_door(painter=painter, bottom_center=(250, 836), width=150, height=320, is_open=True)

    if form == PARTICIPLE:
        draw_footprints(painter=painter, start=(380, 830), end=(660, 830), count=5)
        Milo(hip=(800, 700), scale=0.5).draw(
            painter=painter,
            pose=Pose(left_arm=(-28, 0), right_arm=(125, 30)),
            before_arms=lambda skeleton: paint_suitcase_in_hand(painter=painter, hand=skeleton.left_hand, size=0.5),
        )
        return

    Milo(hip=(610, 600)).draw(
        painter=painter,
        pose=TRAVELING_POSE,
        before_arms=lambda skeleton: paint_suitcase_in_hand(painter=painter, hand=skeleton.left_hand),
    )

    if form == PAST:
        draw_footprints(painter=painter, start=(400, 830), end=(480, 830), count=2)
        paint_past_clock(painter=painter, center=(860, 230))


def paint_suitcase_in_hand(
    painter,
    hand,
    size=1.0,
):
    """The hand grips the top of a handle ring that stands on the suitcase."""
    half_width = SUITCASE_HALF_WIDTH * size
    half_height = SUITCASE_HALF_HEIGHT * size
    handle_radius = SUITCASE_HANDLE_RADIUS * size
    center = (hand[0], hand[1] + handle_radius + SUITCASE_HANDLE_GAP * size + half_height)
    painter.fill_ring(
        center=(center[0], center[1] - half_height - SUITCASE_HANDLE_GAP * size),
        outer_radius=handle_radius,
        inner_radius=handle_radius - 9 * size,
        color=SUITCASE_HANDLE_COLOR,
    )
    painter.fill_rounded_rect(
        box=(center[0] - half_width, center[1] - half_height, center[0] + half_width, center[1] + half_height),
        radius=10 * size,
        shade=solid(SUITCASE_COLOR),
    )


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="leave", paint_scene=paint_leave_scene)
