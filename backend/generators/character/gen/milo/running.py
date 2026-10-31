"""
Milo running, drawn from scratch.
Output: milo_running.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.milo.milo import Milo
from character.poses import RUN_POSE, SHOWCASE_HIP, SHOWCASE_SCALE

POSE = RUN_POSE


def render_milo_running_image():
    painter = CharacterPainter()
    Milo(hip=SHOWCASE_HIP, scale=SHOWCASE_SCALE).draw(painter=painter, pose=POSE)
    painter.save_image(name="milo_running")


if __name__ == "__main__":
    render_milo_running_image()
