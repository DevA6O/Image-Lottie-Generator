"""
Shared side view of a horse-like animal looking to the left (horse, donkey, zebra):
long legs, arched neck, long head, mane and tail.
"""
from dataclasses import dataclass

from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from animals.quadruped_shape import EYE_HIGHLIGHT, QuadrupedSpec, paint_legs, paint_pointed_ear, paint_tail, paint_torso
from painting.flat_painter import build_width_profile, sample_curve, solid

HEAD_ANGLE = -55


@dataclass
class HorseLook:
    coat: tuple
    far_coat: tuple
    hoof: tuple
    muzzle: tuple
    mane: tuple
    ear_inner: tuple
    ear_length: float = 120
    stocky: bool = False


def draw_horse(
    painter,
    look,
):
    """Paints the whole horse and returns the mask of torso and neck (for stripes)."""
    spec = _build_spec(look=look)
    head = (255, 330) if look.stocky else (255, 270)
    neck_mask = _build_neck_mask(painter=painter, spec=spec, head=head)

    paint_legs(painter=painter, spec=spec)
    painter.fill(mask=neck_mask, shade=solid(look.coat))
    paint_tail(painter=painter, points=[(850, spec.body_center[1] - 40), (950, 520), (965, 700), (900, 800)], widths=(60, 120), color=look.mane)
    _paint_far_ear(painter=painter, look=look, head=head)
    torso_mask = paint_torso(painter=painter, spec=spec)
    _paint_mane(painter=painter, look=look, head=head, spec_y=spec.body_center[1])
    _paint_head(painter=painter, look=look, head=head)

    return painter.union_masks(first_mask=torso_mask, second_mask=neck_mask)


def _build_spec(look):
    body_y = 540 if look.stocky else 500
    return QuadrupedSpec(
        coat=look.coat,
        far_coat=look.far_coat,
        foot=look.hoof,
        muzzle=look.muzzle,
        body_center=(600, body_y),
        body_rx=270,
        body_ry=150 if look.stocky else 135,
        leg_width=58 if look.stocky else 50,
        foot_rx=34,
        foot_ry=22,
    )


def _build_neck_mask(
    painter,
    spec,
    head,
):
    base = (470, spec.body_center[1] - 20)
    middle = ((base[0] + head[0]) / 2 + 10, (base[1] + head[1]) / 2 + 10)
    widths = build_width_profile(stops=[(0.0, 250), (1.0, 135)], point_count=3)

    return painter.build_tapered_curve_mask(points=[base, middle, head], widths=widths)


def _paint_mane(
    painter,
    look,
    head,
    spec_y,
):
    mane_points = sample_curve(start=(head[0] + 95, head[1] - 55), first_control=(head[0] + 190, head[1] + 40), second_control=(head[0] + 200, head[1] + 140), end=(515, spec_y - 85))
    widths = build_width_profile(stops=[(0.0, 40), (1.0, 55)], point_count=len(mane_points))
    painter.fill_tapered_curve(points=mane_points, widths=widths, shade=solid(look.mane))


def _paint_far_ear(
    painter,
    look,
    head,
):
    base = (head[0] + 80, head[1] - 50)
    paint_pointed_ear(painter=painter, base=base, tip=(base[0] + 30, base[1] - look.ear_length), width=60, color=look.far_coat)


def _paint_head(
    painter,
    look,
    head,
):
    base = (head[0] + 40, head[1] - 55)
    paint_pointed_ear(painter=painter, base=base, tip=(base[0] + 12, base[1] - look.ear_length), width=64, color=look.coat, inner_color=look.ear_inner)
    painter.blob(center=head, radius_x=140, radius_y=80, color=look.coat, angle=HEAD_ANGLE)
    painter.blob(center=(head[0] - 70, head[1] + 100), radius_x=70, radius_y=62, color=look.muzzle, angle=HEAD_ANGLE)
    painter.spot(center=(head[0] - 88, head[1] + 120), radius_x=9, radius_y=14, color=NOSE, angle=HEAD_ANGLE)
    painter.spot(center=(head[0] + 14, head[1] - 4), radius_x=15, radius_y=15, color=EYE)
    painter.spot(center=(head[0] + 9, head[1] - 10), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)
