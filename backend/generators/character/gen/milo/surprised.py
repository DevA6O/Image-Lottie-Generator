"""
Milo surprised, drawn from scratch.
Output: milo_surprised.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.figure import Pose
from character.milo.milo import Milo
from character.poses import SHOWCASE_HIP, SHOWCASE_SCALE

POSE = Pose(left_arm=(-65, 0), right_arm=(65, 0), eyes="wide", mouth="o", brows="raised")


def render_milo_surprised_image():
    painter = CharacterPainter()
    Milo(hip=SHOWCASE_HIP, scale=SHOWCASE_SCALE).draw(painter=painter, pose=POSE)
    painter.save_image(name="milo_surprised")


if __name__ == "__main__":
    render_milo_surprised_image()
