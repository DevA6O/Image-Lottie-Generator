"""
Full star image, drawn from scratch.
Output: full_star.png (1024x1024, transparent background) in frontend/results/rating
"""
from star_image import StarPainter, save_star_image
from star_shape import OUT_DIR

if __name__ == "__main__":
    save_star_image(paint_star=StarPainter.paint_full_star, out_file=OUT_DIR / "full_star.png")
