"""
Milo as a close-up portrait, drawn from scratch.
Output: milo_portrait.png (1024x1024, transparent background) in frontend/results/character
"""
from character.character_painter import CharacterPainter
from character.figure import Pose
from character.milo.milo import Milo

PORTRAIT_HIP = (512, 1056)    # The head is centered and the body is cut off at the shoulders
PORTRAIT_SCALE = 2.7

POSE = Pose(eyes="happy", mouth="grin")


def render_milo_portrait_image():
    painter = CharacterPainter()
    Milo(hip=PORTRAIT_HIP, scale=PORTRAIT_SCALE).draw(painter=painter, pose=POSE, with_legs=False)
    painter.save_image(name="milo_portrait")


if __name__ == "__main__":
    render_milo_portrait_image()
