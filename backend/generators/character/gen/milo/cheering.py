"""
Milo cheering, drawn from scratch.
Output: milo_cheering.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.milo.milo import Milo
from character.poses import CHEER_POSE, SHOWCASE_HIP, SHOWCASE_SCALE

POSE = CHEER_POSE


def render_milo_cheering_image():
    painter = CharacterPainter()
    Milo(hip=SHOWCASE_HIP, scale=SHOWCASE_SCALE).draw(painter=painter, pose=POSE)
    painter.save_image(name="milo_cheering")


if __name__ == "__main__":
    render_milo_cheering_image()
