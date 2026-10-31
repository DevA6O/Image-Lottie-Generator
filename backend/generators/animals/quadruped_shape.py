"""
Shared side view of a four-legged animal that looks to the left.
An animal script fills a QuadrupedSpec (colors and sizes), calls the paint_* functions in
drawing order and adds its own details (horns, mane, stripes, ...) in between.
"""
import math
from dataclasses import dataclass

from animals.face_parts import EYE, NOSE
from painting.flat_painter import build_width_profile, sample_curve, solid

GROUND_Y = 905
FAR_LEG_SHIFT = 50
EYE_HIGHLIGHT = (255, 255, 255)


@dataclass
class QuadrupedSpec:
    coat: tuple
    far_coat: tuple
    foot: tuple
    muzzle: tuple
    nose: tuple = NOSE
    body_center: tuple = (590, 570)
    body_rx: float = 270
    body_ry: float = 150
    leg_width: float = 66
    foot_rx: float = 44
    foot_ry: float = 24
    neck_base: tuple = (380, 520)
    neck_width: float = 150
    head_center: tuple = (250, 430)
    head_rx: float = 110
    head_ry: float = 95
    snout_rx: float = 85
    snout_ry: float = 50
    snout_drop: float = 35
    eye_size: float = 15
    leg_coat: tuple | None = None

    @property
    def front_leg_x(self):
        return self.body_center[0] - self.body_rx * 0.62

    @property
    def rear_leg_x(self):
        return self.body_center[0] + self.body_rx * 0.62

    @property
    def snout_center(self):
        return (self.head_center[0] - self.head_rx * 0.8, self.head_center[1] + self.snout_drop)

    @property
    def nose_center(self):
        snout_x, snout_y = self.snout_center

        return (snout_x - self.snout_rx * 0.78, snout_y - self.snout_ry * 0.35)


def paint_legs(
    painter,
    spec,
):
    """Far legs first (darker, shifted toward the middle), then the near legs."""
    legs = [
        (spec.front_leg_x + FAR_LEG_SHIFT, spec.far_coat),
        (spec.rear_leg_x - FAR_LEG_SHIFT, spec.far_coat),
        (spec.front_leg_x, spec.leg_coat or spec.coat),
        (spec.rear_leg_x, spec.leg_coat or spec.coat),
    ]

    for leg_x, color in legs:
        _paint_leg(painter=painter, spec=spec, leg_x=leg_x, color=color)


def _paint_leg(
    painter,
    spec,
    leg_x,
    color,
):
    hip_y = spec.body_center[1] + spec.body_ry * 0.3
    foot_y = GROUND_Y - spec.foot_ry
    points = [(leg_x, hip_y), (leg_x, (hip_y + foot_y) / 2), (leg_x, foot_y)]
    widths = build_width_profile(stops=[(0.0, spec.leg_width * 1.1), (1.0, spec.leg_width * 0.85)], point_count=3)
    painter.fill_tapered_curve(points=points, widths=widths, shade=solid(color))
    painter.blob(center=(leg_x - 8, foot_y), radius_x=spec.foot_rx, radius_y=spec.foot_ry, color=spec.foot)


def paint_torso(
    painter,
    spec,
):
    """Paints the torso and returns its mask, so stripes and spots can be clipped to it."""
    torso_mask = painter.build_rotated_ellipse_mask(center=spec.body_center, radius_x=spec.body_rx, radius_y=spec.body_ry)
    painter.fill(mask=torso_mask, shade=solid(spec.coat))

    return torso_mask


def paint_tail(
    painter,
    points,
    widths,
    color,
):
    """A tapered tail through the points (from the body to the tip)."""
    curve = sample_curve(start=points[0], first_control=points[1], second_control=points[2], end=points[3])
    profile = build_width_profile(stops=list(zip((0.0, 1.0), widths)), point_count=len(curve))
    painter.fill_tapered_curve(points=curve, widths=profile, shade=solid(color))


def paint_neck(
    painter,
    spec,
    end_width=None,
):
    neck_points = [spec.neck_base, ((spec.neck_base[0] + spec.head_center[0]) / 2, (spec.neck_base[1] + spec.head_center[1]) / 2), spec.head_center]
    widths = build_width_profile(stops=[(0.0, spec.neck_width), (1.0, end_width or spec.head_ry * 1.6)], point_count=3)
    painter.fill_tapered_curve(points=neck_points, widths=widths, shade=solid(spec.coat))


def paint_head(
    painter,
    spec,
    snout_color=None,
    face=True,
):
    """The head and the snout. Pass face=False to paint marks first and the face afterwards."""
    painter.blob(center=spec.head_center, radius_x=spec.head_rx, radius_y=spec.head_ry, color=spec.coat)
    painter.blob(center=spec.snout_center, radius_x=spec.snout_rx, radius_y=spec.snout_ry, color=snout_color or spec.muzzle)

    if face:
        paint_face(painter=painter, spec=spec)


def paint_face(
    painter,
    spec,
):
    painter.spot(center=spec.nose_center, radius_x=spec.snout_ry * 0.34, radius_y=spec.snout_ry * 0.3, color=spec.nose)
    paint_side_eye(painter=painter, spec=spec)


def build_head_mask(
    painter,
    spec,
):
    return painter.union_masks(
        first_mask=painter.build_rotated_ellipse_mask(center=spec.head_center, radius_x=spec.head_rx, radius_y=spec.head_ry),
        second_mask=painter.build_rotated_ellipse_mask(center=spec.snout_center, radius_x=spec.snout_rx, radius_y=spec.snout_ry),
    )


def paint_side_eye(
    painter,
    spec,
):
    eye_x = spec.head_center[0] - spec.head_rx * 0.3
    eye_y = spec.head_center[1] - spec.head_ry * 0.2
    painter.spot(center=(eye_x, eye_y), radius_x=spec.eye_size, radius_y=spec.eye_size, color=EYE)
    painter.spot(center=(eye_x - 5, eye_y - 6), radius_x=spec.eye_size * 0.3, radius_y=spec.eye_size * 0.3, color=EYE_HIGHLIGHT)


def paint_pointed_ear(
    painter,
    base,
    tip,
    width,
    color,
    inner_color=None,
):
    """A rounded triangle from a base point to a tip."""
    direction_x = tip[0] - base[0]
    direction_y = tip[1] - base[1]
    length = (direction_x**2 + direction_y**2) ** 0.5
    normal = (-direction_y / length * width / 2, direction_x / length * width / 2)
    corners = [(base[0] + normal[0], base[1] + normal[1]), tip, (base[0] - normal[0], base[1] - normal[1])]
    painter.soft_polygon(points=corners, color=color, softness=28)

    if inner_color:
        inner_tip = (base[0] + direction_x * 0.78, base[1] + direction_y * 0.78)
        inner_corners = [(base[0] + normal[0] * 0.5, base[1] + normal[1] * 0.5), inner_tip, (base[0] - normal[0] * 0.5, base[1] - normal[1] * 0.5)]
        painter.flat_soft_polygon(points=inner_corners, color=inner_color, softness=14)


def paint_blob_ear(
    painter,
    base,
    tip,
    width,
    color,
    inner_color=None,
):
    """An oval ear from a base point to a tip: round, floppy or long."""
    center = ((base[0] + tip[0]) / 2, (base[1] + tip[1]) / 2)
    length = ((tip[0] - base[0]) ** 2 + (tip[1] - base[1]) ** 2) ** 0.5
    angle = _angle_of_ellipse_axis(base=base, tip=tip)
    painter.blob(center=center, radius_x=length / 2, radius_y=width / 2, color=color, angle=angle)

    if inner_color:
        painter.spot(center=center, radius_x=length * 0.34, radius_y=width * 0.3, color=inner_color, angle=angle)


def _angle_of_ellipse_axis(
    base,
    tip,
):
    return math.degrees(math.atan2(tip[1] - base[1], tip[0] - base[0]))
