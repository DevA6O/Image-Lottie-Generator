"""
Painter for the verb images: the flat painter, plus the place where the finished PNGs go.
"""
from painting.flat_painter import FlatPainter
from painting.results_dir import RESULTS_DIR

VERB_OUT_DIR = RESULTS_DIR / "verbs"


class VerbPainter(FlatPainter):
    def save_verb_image(self, file_name):
        self.save(out_file=VERB_OUT_DIR / file_name)
