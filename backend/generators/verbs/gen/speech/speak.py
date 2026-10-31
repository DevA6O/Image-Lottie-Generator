"""
Scene for the irregular verb "speak" (spoke, spoken).
Output: speak_infinitive.png, speak_past.png and speak_participle.png (1024x1024, transparent background) in frontend/results/verbs
Run it with the form number: 0 = infinitive, 1 = past, 2 = past participle.
"""
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import STAND_HIP
from painting.flat_painter import solid
from verbs.props import draw_lectern, draw_music_note, draw_sound_waves, draw_star
from verbs.render_verb import render_verb_from_command_line
from verbs.tense import PARTICIPLE, PAST, paint_past_clock

LECTERN_TOP_OFFSET_Y = -30    # From the hip
LECTERN_WIDTH = 300
FLOOR_Y = 836
STAND_HEIGHT = 96    # From the lectern top to the center of the microphone head
STAND_COLOR = (96, 106, 130)
MICROPHONE_HEAD_COLOR = (176, 184, 202)
MICROPHONE_HEAD_LIGHT = (210, 216, 230)
RESTING_LEFT_ARM = (-60, 60)    # The forearms rest on the lectern
RESTING_RIGHT_ARM = (60, -60)
SOUND_OFFSET = (130, -190)


def paint_speak_scene(painter, form):
    pose = Pose(left_arm=RESTING_LEFT_ARM, right_arm=RESTING_RIGHT_ARM, mouth="open", eyes="happy")
    Milo(hip=STAND_HIP).draw(painter=painter, pose=pose, before_arms=lambda skeleton: paint_lectern_with_microphone(painter=painter, skeleton=skeleton))

    hip = STAND_HIP
    draw_sound_waves(painter=painter, center=(hip[0] + SOUND_OFFSET[0], hip[1] + SOUND_OFFSET[1]), size=1.0, facing=1)
    draw_sound_waves(painter=painter, center=(hip[0] - SOUND_OFFSET[0], hip[1] + SOUND_OFFSET[1]), size=1.0, facing=-1)

    if form == PAST:
        draw_music_note(painter=painter, center=(830, 520), size=0.9)
        paint_past_clock(painter=painter, center=(850, 230))
    elif form == PARTICIPLE:
        draw_star(painter=painter, center=(830, 540), size=40)


def paint_lectern_with_microphone(
    painter,
    skeleton,
):
    hip = skeleton.hip
    draw_lectern(painter=painter, top_center=(hip[0], hip[1] + LECTERN_TOP_OFFSET_Y), width=LECTERN_WIDTH, bottom_y=FLOOR_Y)
    lectern_top_y = hip[1] + LECTERN_TOP_OFFSET_Y
    paint_microphone_stand(painter=painter, base_center=(hip[0], lectern_top_y))


def paint_microphone_stand(
    painter,
    base_center,
):
    """A straight pole on a flat base, so the microphone stands firmly on the lectern."""
    head_center = (base_center[0], base_center[1] - STAND_HEIGHT)
    painter.fill_ellipse(center=(base_center[0], base_center[1] + 2), radius_x=40, radius_y=10, shade=solid(STAND_COLOR))
    painter.fill_stroke(start=(base_center[0], base_center[1]), end=head_center, width=12, shade=solid(STAND_COLOR))
    painter.fill_circle(center=head_center, radius=24, shade=solid(MICROPHONE_HEAD_COLOR))
    painter.flat_circle(center=head_center, radius=13, color=MICROPHONE_HEAD_LIGHT)


if __name__ == "__main__":
    render_verb_from_command_line(verb_key="speak", paint_scene=paint_speak_scene)
