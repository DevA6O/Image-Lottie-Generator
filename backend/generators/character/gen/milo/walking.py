"""
Milo walking, drawn from scratch.
Output: milo_walking.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.milo.milo import Milo
from character.poses import SHOWCASE_HIP, SHOWCASE_SCALE, WALK_POSE

POSE = WALK_POSE


def render_milo_walking_image():
    painter = CharacterPainter()
    Milo(hip=SHOWCASE_HIP, scale=SHOWCASE_SCALE).draw(painter=painter, pose=POSE)
    painter.save_image(name="milo_walking")


if __name__ == "__main__":
    render_milo_walking_image()
