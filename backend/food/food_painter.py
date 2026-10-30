"""
Painter for the food images: the flat painter, plus the place where the finished PNGs go.
"""
from pathlib import Path

from painting.flat_painter import FlatPainter

FOOD_OUT_DIR = Path(__file__).resolve().parents[2] / "frontend" / "results" / "food"


class FoodPainter(FlatPainter):
    def save_image(self, name):
        self.save(out_file=FOOD_OUT_DIR / f"{name}.png")
