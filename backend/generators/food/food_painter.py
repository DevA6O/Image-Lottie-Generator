"""
Painter for the food images: the flat painter, plus the place where the finished PNGs go.
"""
from painting.flat_painter import FlatPainter
from painting.results_dir import RESULTS_DIR

FOOD_OUT_DIR = RESULTS_DIR / "food"


class FoodPainter(FlatPainter):
    def save_image(self, name):
        self.save(out_file=FOOD_OUT_DIR / f"{name}.png")
