"""
Red bell pepper image, drawn from scratch.
Output: bell_pepper.png (1024x1024, transparent background) in frontend/results/food
"""
from food_painter import FoodPainter

PEPPER = ((246, 76, 60), (184, 28, 36))
LOBE_LINE = ((160, 24, 34), (160, 24, 34))
SHINE = ((255, 150, 136), (255, 136, 120))
STEM = ((110, 180, 70), (60, 126, 46))

LOBES = [(360, 590, 150, 280), (664, 590, 150, 280), (512, 610, 170, 290)]


def paint_pepper(painter):
    lobe_masks = [
        painter.build_rotated_ellipse_mask(center=(x, y), radius_x=radius_x, radius_y=radius_y)
        for x, y, radius_x, radius_y in LOBES
    ]
    pepper_mask = painter.round_corners(mask=painter.union_all(masks=lobe_masks), radius=30)
    painter.fill(mask=pepper_mask, shade=PEPPER)

    painter.fill_curve(points=[(430, 340), (410, 600), (440, 860)], width=10, shade=LOBE_LINE, clip=pepper_mask)
    painter.fill_curve(points=[(594, 340), (614, 600), (584, 860)], width=10, shade=LOBE_LINE, clip=pepper_mask)
    painter.fill_ellipse(center=(310, 540), radius_x=26, radius_y=100, shade=SHINE, angle=8, clip=pepper_mask)


def paint_stem(painter):
    painter.fill_curve(points=[(512, 340), (516, 280), (560, 220)], width=56, shade=STEM)


def render_bell_pepper_image():
    painter = FoodPainter()
    paint_pepper(painter)
    paint_stem(painter)
    painter.save_image(name="bell_pepper")


if __name__ == "__main__":
    render_bell_pepper_image()
