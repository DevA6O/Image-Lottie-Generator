"""
Painter for the character images: the flat painter, plus the place where the finished PNGs go.
"""
from painting.flat_painter import FlatPainter
from painting.results_dir import RESULTS_DIR

CHARACTER_OUT_DIR = RESULTS_DIR / "character"


class CharacterPainter(FlatPainter):
    def save_image(self, name):
        self.save(out_file=CHARACTER_OUT_DIR / f"{name}.png")
