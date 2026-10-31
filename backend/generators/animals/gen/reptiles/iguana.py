"""
Iguana image, drawn from scratch.
Output: iguana.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE
from painting.flat_painter import build_normal, build_width_profile, sample_curve, solid

SKIN = (122, 184, 84)
SKIN_DARK = (78, 136, 66)
DEWLAP = (250, 150, 70)
BODY_WIDTHS = [(0.0, 70), (0.08, 130), (0.3, 190), (0.6, 120), (1.0, 14)]


def paint_legs(painter):
    for leg_x in (330, 580):
        painter.line(points=[(leg_x, 650), (leg_x - 60, 760), (leg_x - 20, 860)], width=46, color=SKIN_DARK)
        painter.blob(center=(leg_x + 10, 880), radius_x=58, radius_y=26, color=SKIN_DARK)


def paint_body(painter, points):
    body_mask = painter.build_tapered_curve_mask(points=points, widths=build_width_profile(stops=BODY_WIDTHS))
    painter.fill(mask=body_mask, shade=solid(SKIN))

    for band_index in range(100, 150, 14):
        painter.fill_stroke(start=(points[band_index][0], points[band_index][1] - 50), end=(points[band_index][0], points[band_index][1] + 70), width=16, shade=solid(SKIN_DARK), clip=body_mask)


def paint_crest(painter, points):
    widths = build_width_profile(stops=BODY_WIDTHS)

    for crest_index in range(14, 110, 10):
        x, y = points[crest_index]
        normal_x, normal_y = build_normal(points=points, index=crest_index)
        base_y = y - abs(normal_y) * widths[crest_index] / 2 + 10
        painter.soft_polygon(points=[(x - 20, base_y), (x - 6, base_y - 62), (x + 26, base_y)], color=SKIN_DARK, softness=8)


def paint_head(painter):
    painter.blob(center=(215, 640), radius_x=52, radius_y=92, color=DEWLAP, angle=-25)
    painter.blob(center=(215, 505), radius_x=135, radius_y=100, color=SKIN, angle=8)
    painter.spot(center=(195, 470), radius_x=22, radius_y=22, color=EYE)
    painter.spot(center=(188, 463), radius_x=7, radius_y=7, color=(255, 255, 255))
    painter.spot(center=(105, 500), radius_x=8, radius_y=8, color=EYE)
    painter.arc_line(center=(150, 520), radius=80, start_angle=30, end_angle=75, width=11, color=SKIN_DARK)


def render_iguana_image():
    painter = AnimalPainter()
    points = sample_curve(start=(150, 520), first_control=(400, 560), second_control=(650, 540), end=(930, 840))
    paint_legs(painter)
    paint_body(painter, points=points)
    paint_crest(painter, points=points)
    paint_head(painter)
    painter.save_image(name="iguana")


if __name__ == "__main__":
    render_iguana_image()
