"""
Shared sitting rabbit seen from the side, looking to the left (rabbit and hare).
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from animals.quadruped_shape import EYE_HIGHLIGHT, paint_blob_ear

TAIL_COLOR = (255, 250, 244)
BODY_CENTER = (610, 690)
HEAD_CENTER = (370, 470)


def draw_sitting_rabbit(
    painter,
    coat,
    far_coat,
    belly_color,
    ear_inner,
    ear_tip=None,
    ear_length=330,
):
    painter.blob(center=(850, 770), radius_x=62, radius_y=58, color=TAIL_COLOR)
    _paint_ears(painter=painter, coat=coat, far_coat=far_coat, ear_inner=ear_inner, ear_length=ear_length)
    painter.blob(center=BODY_CENTER, radius_x=235, radius_y=205, color=coat, angle=-15)
    painter.blob(center=(650, 770), radius_x=165, radius_y=130, color=coat)
    painter.blob(center=(470, 800), radius_x=100, radius_y=95, color=belly_color)
    painter.blob(center=(520, 895), radius_x=165, radius_y=36, color=far_coat)
    painter.blob(center=(430, 895), radius_x=62, radius_y=30, color=coat)
    painter.blob(center=HEAD_CENTER, radius_x=130, radius_y=115, color=coat)
    painter.blob(center=(280, 520), radius_x=62, radius_y=50, color=belly_color)
    painter.spot(center=(240, 505), radius_x=20, radius_y=15, color=NOSE)
    painter.spot(center=(350, 450), radius_x=16, radius_y=16, color=EYE)
    painter.spot(center=(345, 444), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)

    if ear_tip:
        _paint_ear_tips(painter=painter, ear_tip=ear_tip, ear_length=ear_length)


def _paint_ear_tips(
    painter,
    ear_tip,
    ear_length,
):
    reach = ear_length * 0.8

    for tip_x, tip_y in ((470 + reach * 0.2, 400 - reach), (380 + reach * 0.12, 390 - reach)):
        painter.spot(center=(tip_x, tip_y + 28), radius_x=36, radius_y=40, color=ear_tip)


def _paint_ears(
    painter,
    coat,
    far_coat,
    ear_inner,
    ear_length,
):
    reach = ear_length * 0.8
    paint_blob_ear(painter=painter, base=(440, 400), tip=(470 + reach * 0.2, 400 - reach), width=95, color=far_coat, inner_color=ear_inner)
    paint_blob_ear(painter=painter, base=(380, 390), tip=(380 + reach * 0.12, 390 - reach), width=100, color=coat, inner_color=ear_inner)
