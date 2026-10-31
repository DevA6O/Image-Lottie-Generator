"""
The body that every character shares: a round-headed figure in the flat icon style.
A Pose says how the body is bent. A Figure draws a pose and tells where the hands, feet and head are,
so a scene can put props exactly there. A Look gives the figure its colors and hair.
Arm and leg angles are screen angles: 0 points down, 90 points right, 180 points up.
"""
from dataclasses import dataclass

from painting.flat_painter import build_arc_points, build_direction, rotate_point, sample_curve, solid

HAIR_STRAND_FACTOR = 1.45
FADE_TARGET = 235
EYE = (50, 38, 48)
EYE_WHITE = (252, 252, 255)
MOUTH = (150, 50, 62)
CHEEK = (248, 150, 140)

TORSO_LENGTH = 170
BODY_WIDTH = 112
PELVIS_LENGTH = 50
SHOULDER_DROP = 26
SHOULDER_HALF_WIDTH = 42
HIP_HALF_WIDTH = 30
UPPER_ARM_LENGTH = 84
FOREARM_LENGTH = 80
ARM_WIDTH = 36
HAND_RADIUS = 23
THIGH_LENGTH = 104
SHIN_LENGTH = 104
LEG_WIDTH = 46
FOOT_RADIUS_X = 36
FOOT_RADIUS_Y = 17
FOOT_SHIFT = 14
HEAD_RADIUS = 80
HEAD_RISE = 58
EAR_RADIUS = 16
FACE_LINE_WIDTH = 8

LEFT = -1
RIGHT = 1


@dataclass(frozen=True)
class Pose:
    """lean and head_tilt tip to the right when positive. Arms and legs are (angle, bend)."""

    lean: float = 0
    head_tilt: float = 0
    left_arm: tuple = (-14, 0)
    right_arm: tuple = (14, 0)
    left_leg: tuple = (-5, 0)
    right_leg: tuple = (5, 0)
    eyes: str = "open"      # open, wide, up, side, happy, closed
    mouth: str = "smile"    # smile, sad, open, o, flat, grin
    brows: str = "none"     # none, raised, worry, angry


@dataclass(frozen=True)
class Look:
    """Everything that makes one character look different from another. Hair curves are in head coordinates."""

    skin: tuple
    hair: tuple
    shirt: tuple
    pants: tuple
    shoe: tuple
    hair_outline: tuple    # cubic curves (start, control, control, end) that close into one shape
    hair_strands: tuple    # lighter cubic curves on top of the hair


@dataclass(frozen=True)
class Skeleton:
    hip: tuple
    neck: tuple
    head: tuple
    head_angle: float
    arms: dict    # side -> (shoulder, elbow, hand)
    legs: dict    # side -> (hip joint, knee, ankle)

    @property
    def left_hand(self):
        return self.arms[LEFT][2]

    @property
    def right_hand(self):
        return self.arms[RIGHT][2]

    @property
    def left_foot(self):
        return self.legs[LEFT][2]

    @property
    def right_foot(self):
        return self.legs[RIGHT][2]


def _scale_color(
    color,
    factor,
):
    return tuple(min(255, round(channel * factor)) for channel in color)


def _add(
    point,
    direction,
    length,
):
    return (point[0] + direction[0] * length, point[1] + direction[1] * length)


class Figure:
    """A character body. The look (colors and hair) decides who it is. Every character is a Figure with its own Look."""

    def __init__(
        self,
        look,
        hip=(512, 600),
        scale=1.0,
        fade=0.0,
    ):
        self.look = look
        self.hip = hip
        self.scale = scale
        self.fade = fade

    def build_skeleton(self, pose):
        scale = self.scale
        up = build_direction(180 - pose.lean)
        sideways = build_direction(90 - pose.lean)
        neck = _add(self.hip, up, TORSO_LENGTH * scale)
        shoulder_center = _add(self.hip, up, (TORSO_LENGTH - SHOULDER_DROP) * scale)
        head_angle = pose.lean + pose.head_tilt
        head = _add(neck, build_direction(180 - head_angle), HEAD_RISE * scale)

        arms = {}
        for side, arm in ((LEFT, pose.left_arm), (RIGHT, pose.right_arm)):
            shoulder = _add(shoulder_center, sideways, side * SHOULDER_HALF_WIDTH * scale)
            elbow = _add(shoulder, build_direction(arm[0]), UPPER_ARM_LENGTH * scale)
            hand = _add(elbow, build_direction(arm[0] + arm[1]), FOREARM_LENGTH * scale)
            arms[side] = (shoulder, elbow, hand)

        legs = {}
        for side, leg in ((LEFT, pose.left_leg), (RIGHT, pose.right_leg)):
            hip_joint = _add(self.hip, sideways, side * HIP_HALF_WIDTH * scale)
            knee = _add(hip_joint, build_direction(leg[0]), THIGH_LENGTH * scale)
            ankle = _add(knee, build_direction(leg[0] + leg[1]), SHIN_LENGTH * scale)
            legs[side] = (hip_joint, knee, ankle)

        return Skeleton(hip=self.hip, neck=neck, head=head, head_angle=head_angle, arms=arms, legs=legs)

    def draw(
        self,
        painter,
        pose,
        with_legs=True,
        before_arms=None,
    ):
        """before_arms(skeleton) paints worn things, such as a medal, on the shirt and under the arms."""
        skeleton = self.build_skeleton(pose=pose)

        if with_legs:
            self._draw_legs(painter=painter, skeleton=skeleton)

        self._draw_torso(painter=painter, skeleton=skeleton)

        if before_arms is not None:
            before_arms(skeleton)

        self._draw_arms(painter=painter, skeleton=skeleton)
        self._draw_head(painter=painter, skeleton=skeleton, pose=pose)

        return skeleton

    def _draw_legs(
        self,
        painter,
        skeleton,
    ):
        scale = self.scale

        for side, (hip_joint, knee, ankle) in skeleton.legs.items():
            painter.fill_stroke(start=hip_joint, end=knee, width=LEG_WIDTH * scale, shade=self._shade(self.look.pants))
            painter.fill_stroke(start=knee, end=ankle, width=LEG_WIDTH * scale, shade=self._shade(self.look.pants))
            foot_center = (ankle[0] + side * FOOT_SHIFT * scale, ankle[1] + 10 * scale)
            painter.fill_ellipse(
                center=foot_center,
                radius_x=FOOT_RADIUS_X * scale,
                radius_y=FOOT_RADIUS_Y * scale,
                shade=self._shade(self.look.shoe),
            )

    def _draw_torso(
        self,
        painter,
        skeleton,
    ):
        scale = self.scale
        torso_direction = self._normalize(start=skeleton.hip, end=skeleton.neck)
        pelvis_end = _add(skeleton.hip, torso_direction, PELVIS_LENGTH * scale)
        torso_start = _add(skeleton.hip, torso_direction, (PELVIS_LENGTH - 10) * scale)
        painter.fill_stroke(start=skeleton.hip, end=pelvis_end, width=(BODY_WIDTH - 8) * scale, shade=self._shade(self.look.pants))
        painter.fill_stroke(start=torso_start, end=skeleton.neck, width=BODY_WIDTH * scale, shade=self._shade(self.look.shirt))

    def _draw_arms(
        self,
        painter,
        skeleton,
    ):
        scale = self.scale

        for shoulder, elbow, hand in skeleton.arms.values():
            painter.fill_stroke(start=shoulder, end=elbow, width=ARM_WIDTH * scale, shade=self._shade(self.look.shirt))
            painter.fill_stroke(start=elbow, end=hand, width=(ARM_WIDTH - 4) * scale, shade=self._shade(self.look.skin))
            painter.fill_circle(center=hand, radius=HAND_RADIUS * scale, shade=self._shade(self.look.skin))

    def _draw_head(
        self,
        painter,
        skeleton,
        pose,
    ):
        scale = self.scale
        head = skeleton.head
        angle = skeleton.head_angle

        def to_world(local_point):
            offset = rotate_point(point=(local_point[0] * scale, local_point[1] * scale), center=(0, 0), angle_degrees=angle)

            return (head[0] + offset[0], head[1] + offset[1])

        for side in (LEFT, RIGHT):
            painter.fill_circle(center=to_world((side * 78, 8)), radius=EAR_RADIUS * scale, shade=self._shade(self.look.skin))

        painter.fill_circle(center=head, radius=HEAD_RADIUS * scale, shade=self._shade(self.look.skin))
        head_mask = painter.build_rotated_ellipse_mask(center=head, radius_x=HEAD_RADIUS * scale, radius_y=HEAD_RADIUS * scale)
        self._draw_hair(painter=painter, to_world=to_world, head_mask=head_mask, angle=angle)

        for side in (LEFT, RIGHT):
            painter.flat_ellipse(center=to_world((side * 50, 30)), radius_x=14 * scale, radius_y=9 * scale, color=CHEEK, angle=angle)

        self._draw_eyes(painter=painter, to_world=to_world, pose=pose, angle=angle)
        self._draw_brows(painter=painter, to_world=to_world, pose=pose)
        self._draw_mouth(painter=painter, to_world=to_world, pose=pose, angle=angle)

    def _draw_hair(
        self,
        painter,
        to_world,
        head_mask,
        angle,
    ):
        """The hair is one smooth shape with lighter strands on top. Both come from the look."""
        outline = []

        for start, first_control, second_control, end in self.look.hair_outline:
            outline += sample_curve(start=start, first_control=first_control, second_control=second_control, end=end)[:-1]

        painter.fill_polygon(points=[to_world(point) for point in outline], shade=self._shade(self.look.hair))

        for strand in self.look.hair_strands:
            points = sample_curve(start=strand[0], first_control=strand[1], second_control=strand[2], end=strand[3])
            painter.flat_curve(
                points=[to_world(point) for point in points],
                width=8 * self.scale,
                color=_scale_color(self.look.hair, HAIR_STRAND_FACTOR),
            )

    def _draw_eyes(
        self,
        painter,
        to_world,
        pose,
        angle,
    ):
        scale = self.scale

        for side in (LEFT, RIGHT):
            if pose.eyes in ("happy", "closed"):
                arc = (200, 340) if pose.eyes == "happy" else (20, 160)
                center_y = 12 if pose.eyes == "happy" else -2
                arc_points = build_arc_points(center=(side * 30, center_y), radius=15, start_angle=arc[0], end_angle=arc[1])
                painter.flat_curve(points=[to_world(point) for point in arc_points], width=FACE_LINE_WIDTH * scale, color=EYE)
            elif pose.eyes == "open":
                painter.flat_ellipse(center=to_world((side * 30, 2)), radius_x=10 * scale, radius_y=14 * scale, color=EYE, angle=angle)
            else:
                gaze = {"wide": (0, 0), "up": (0, -7), "side": (7, 0)}[pose.eyes]
                painter.flat_circle(center=to_world((side * 30, 2)), radius=18 * scale, color=EYE_WHITE)
                painter.flat_circle(center=to_world((side * 30 + gaze[0], 2 + gaze[1])), radius=9 * scale, color=EYE)

    def _draw_brows(
        self,
        painter,
        to_world,
        pose,
    ):
        # (outer height, inner height): the outer end is 44 pixels and the inner end 18 pixels from the face center
        shapes = {
            "raised": (-34, -42),
            "worry": (-26, -40),
            "angry": (-40, -26),
        }

        if pose.brows not in shapes:
            return

        outer_height, inner_height = shapes[pose.brows]

        for side in (LEFT, RIGHT):
            painter.flat_stroke(
                start=to_world((side * 44, outer_height)),
                end=to_world((side * 18, inner_height)),
                width=8 * self.scale,
                color=self.look.hair,
            )

    def _draw_mouth(
        self,
        painter,
        to_world,
        pose,
        angle,
    ):
        scale = self.scale

        if pose.mouth in ("smile", "sad"):
            arc = build_arc_points(
                center=(0, 22 if pose.mouth == "smile" else 56),
                radius=26,
                start_angle=20 if pose.mouth == "smile" else 200,
                end_angle=160 if pose.mouth == "smile" else 340,
            )
            painter.flat_curve(points=[to_world(point) for point in arc], width=FACE_LINE_WIDTH * scale, color=EYE)
        elif pose.mouth == "open":
            painter.flat_ellipse(center=to_world((0, 44)), radius_x=22 * scale, radius_y=18 * scale, color=MOUTH, angle=angle)
        elif pose.mouth == "o":
            painter.flat_circle(center=to_world((0, 44)), radius=12 * scale, color=MOUTH)
        elif pose.mouth == "flat":
            painter.flat_stroke(start=to_world((-16, 44)), end=to_world((16, 44)), width=FACE_LINE_WIDTH * scale, color=EYE)
        else:
            arc = build_arc_points(center=(0, 32), radius=30, start_angle=0, end_angle=180)
            painter.flat_polygon(points=[to_world(point) for point in arc], color=MOUTH)

    def _shade(self, color):
        """A solid shade. With fade > 0 the color moves toward light gray, so a past self looks like a ghost."""
        faded_color = tuple(round(channel + (FADE_TARGET - channel) * self.fade) for channel in color)

        return solid(faded_color)

    def _normalize(
        self,
        start,
        end,
    ):
        length_x = end[0] - start[0]
        length_y = end[1] - start[1]
        length = (length_x ** 2 + length_y ** 2) ** 0.5

        return (length_x / length, length_y / length)
