"""
Milo thinking, drawn from scratch.
Output: milo_thinking.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import SHOWCASE_HIP, SHOWCASE_SCALE

POSE = Pose(head_tilt=8, left_arm=(-14, 0), right_arm=(40, 185), eyes="up", mouth="flat")


def render_milo_thinking_image():
    painter = CharacterPainter()
    Milo(hip=SHOWCASE_HIP, scale=SHOWCASE_SCALE).draw(painter=painter, pose=POSE)
    painter.save_image(name="milo_thinking")


if __name__ == "__main__":
    render_milo_thinking_image()
