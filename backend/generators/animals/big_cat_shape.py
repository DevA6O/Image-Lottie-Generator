"""
Shared side view of a big cat looking to the left (lion, tiger, leopard, cheetah).
The body is painted first, then the animal adds its marks (stripes, spots, mane), then the face.
"""
from dataclasses import dataclass

from animals.quadruped_shape import QuadrupedSpec, build_head_mask, paint_blob_ear, paint_face, paint_head, paint_legs, paint_neck, paint_tail, paint_torso

CAT_NOSE = (84, 52, 52)


@dataclass
class BigCatLook:
    coat: tuple
    far_coat: tuple
    belly: tuple
    tail_tip: tuple
    ear_inner: tuple
    slim: bool = False


def build_big_cat_spec(look):
    return QuadrupedSpec(
        coat=look.coat,
        far_coat=look.far_coat,
        foot=look.belly,
        muzzle=look.belly,
        nose=CAT_NOSE,
        body_center=(590, 560) if look.slim else (590, 575),
        body_rx=275 if look.slim else 270,
        body_ry=112 if look.slim else 140,
        leg_width=50 if look.slim else 72,
        foot_rx=40 if look.slim else 52,
        neck_base=(400, 520),
        neck_width=120 if look.slim else 170,
        head_center=(260, 440),
        head_rx=95 if look.slim else 112,
        head_ry=82 if look.slim else 98,
        snout_rx=62 if look.slim else 76,
        snout_ry=42 if look.slim else 52,
        snout_drop=32,
        eye_size=16,
    )


def paint_big_cat_body(
    painter,
    spec,
    look,
    before_head=None,
):
    """Paints everything but the face. Returns the masks of the torso and of the head, for marks."""
    paint_legs(painter=painter, spec=spec)
    paint_tail(painter=painter, points=[(830, 560), (940, 610), (960, 730), (915, 810)], widths=(46, 32), color=look.coat)
    painter.blob(center=(912, 825), radius_x=36, radius_y=48, color=look.tail_tip)
    torso_mask = paint_torso(painter=painter, spec=spec)
    painter.blob(center=(520, 680), radius_x=200, radius_y=50, color=look.belly, clip=torso_mask)
    paint_neck(painter=painter, spec=spec)

    if before_head:
        before_head()

    paint_head(painter=painter, spec=spec, face=False)
    paint_blob_ear(painter=painter, base=(315, 380), tip=(345, 340), width=70, color=look.coat, inner_color=look.ear_inner)

    return torso_mask, build_head_mask(painter=painter, spec=spec)


def paint_big_cat_face(
    painter,
    spec,
):
    paint_face(painter=painter, spec=spec)
    painter.arc_line(center=(spec.snout_center[0] + 10, spec.snout_center[1] - 6), radius=30, start_angle=20, end_angle=100, width=7, color=CAT_NOSE)
