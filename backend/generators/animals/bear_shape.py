"""
Shared side view of a bear looking to the left (bear, polar bear, panda).
The body is painted first, then the animal adds its marks (panda patches), then the face.
"""
from dataclasses import dataclass

from animals.quadruped_shape import QuadrupedSpec, build_head_mask, paint_legs, paint_neck, paint_torso, paint_head


@dataclass
class BearLook:
    coat: tuple
    far_coat: tuple
    foot: tuple
    muzzle: tuple
    ear: tuple
    ear_inner: tuple
    nose: tuple
    leg_coat: tuple | None = None


def build_bear_spec(look):
    return QuadrupedSpec(
        coat=look.coat,
        far_coat=look.far_coat,
        foot=look.foot,
        muzzle=look.muzzle,
        nose=look.nose,
        leg_coat=look.leg_coat,
        body_center=(610, 590),
        body_rx=300,
        body_ry=180,
        leg_width=104,
        foot_rx=64,
        foot_ry=30,
        neck_base=(410, 520),
        neck_width=240,
        head_center=(265, 470),
        head_rx=130,
        head_ry=112,
        snout_rx=84,
        snout_ry=56,
        snout_drop=45,
    )


def paint_bear_body(
    painter,
    spec,
    look,
):
    """Paints everything but the face. Returns the masks of the torso and of the head, for marks."""
    paint_legs(painter=painter, spec=spec)
    painter.blob(center=(905, 570), radius_x=34, radius_y=34, color=look.coat)
    torso_mask = paint_torso(painter=painter, spec=spec)
    paint_neck(painter=painter, spec=spec)
    painter.blob(center=(330, 370), radius_x=48, radius_y=48, color=look.ear)
    painter.spot(center=(332, 376), radius_x=24, radius_y=24, color=look.ear_inner)
    paint_head(painter=painter, spec=spec, face=False)

    return torso_mask, build_head_mask(painter=painter, spec=spec)
