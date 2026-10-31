"""
Shared side view of a deer looking to the left (roe deer and red deer): slim legs,
long neck, white rump, antlers. Red deer get bigger antlers.
"""
from dataclasses import dataclass

from animals.animal_painter import AnimalPainter
from animals.quadruped_shape import QuadrupedSpec, paint_blob_ear, paint_head, paint_legs, paint_neck, paint_tail, paint_torso
from painting.flat_painter import build_width_profile, sample_curve, solid

RUMP = (252, 238, 214)
HOOF = (60, 48, 46)
ANTLER_ROOT = (300, 265)


@dataclass
class DeerLook:
    coat: tuple
    far_coat: tuple
    antler: tuple
    antler_scale: float = 1.0


def draw_deer(
    painter,
    look,
):
    spec = QuadrupedSpec(
        coat=look.coat,
        far_coat=look.far_coat,
        foot=HOOF,
        muzzle=RUMP,
        nose=HOOF,
        body_center=(590, 530),
        body_rx=260,
        body_ry=122,
        leg_width=38,
        foot_rx=28,
        foot_ry=20,
        neck_base=(430, 470),
        neck_width=130,
        head_center=(270, 330),
        head_rx=84,
        head_ry=72,
        snout_rx=80,
        snout_ry=38,
        snout_drop=30,
    )
    paint_legs(painter=painter, spec=spec)
    paint_tail(painter=painter, points=[(840, 500), (880, 490), (895, 470), (890, 440)], widths=(50, 30), color=RUMP)
    _paint_antlers(painter=painter, look=look)
    paint_neck(painter=painter, spec=spec)
    torso_mask = paint_torso(painter=painter, spec=spec)
    painter.blob(center=(840, 540), radius_x=80, radius_y=100, color=RUMP, clip=torso_mask)
    painter.blob(center=(560, 650), radius_x=230, radius_y=60, color=RUMP, clip=torso_mask)

    paint_head(painter=painter, spec=spec)
    paint_blob_ear(painter=painter, base=(325, 300), tip=(415, 245), width=58, color=look.far_coat, inner_color=RUMP)


def _paint_antlers(
    painter,
    look,
):
    scale = look.antler_scale
    root_x, root_y = ANTLER_ROOT
    beam = sample_curve(
        start=(root_x, root_y),
        first_control=(root_x + 10 * scale, root_y - 70 * scale),
        second_control=(root_x + 50 * scale, root_y - 120 * scale),
        end=(root_x + 90 * scale, root_y - 190 * scale),
    )
    widths = build_width_profile(stops=[(0.0, 26), (1.0, 12)], point_count=len(beam))
    painter.fill_tapered_curve(points=beam, widths=widths, shade=solid(look.antler))

    tine_count = 2 if scale < 1.2 else 3

    for tine_index in range(tine_count):
        start = beam[int(len(beam) * (0.35 + 0.17 * tine_index))]
        end = (start[0] - 40 * scale, start[1] - 55 * scale)
        painter.line(points=[start, end], width=14, color=look.antler)
