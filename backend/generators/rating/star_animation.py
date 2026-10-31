"""
Star Lottie animations (JSON), drawn as vector shapes (no images).
Used by full_star_lottie.py and half_star_lottie.py.

A star appears, holds for a moment and leaves again:
  - Full star:  spins in one full turn with a bounce, then a burst of mini stars and sparkles.
  - Half star:  flips in like a coin and slides up. Then the gold half fills in from the
                left (layer mask), followed by mini stars and sparkles.
  - Both stars: gentle breathing, several twinkles and a spinning exit.

Every value has a keyframe on EVERY frame (linear interpolation), so the easing is
calculated here and the motion is smooth in every player. The loop is seamless,
because the star is fully gone at the end.

Dependencies: none (star_shape.py must be in the same folder)
"""
import json
import math
from dataclasses import dataclass

from star_shape import (
    CANVAS_SIZE,
    EMPTY_STAR_COLOR,
    OUT_DIR,
    STAR_CENTER_X,
    STAR_CENTER_Y,
    STAR_COLOR_STOPS,
    STAR_RADIUS,
    build_star_outline,
    clip_to_left_half,
)

FRAMES_PER_SECOND = 60
LOOP_FRAMES = 330           # 5.5 seconds per loop

# Timeline of one star, in frames
APPEAR_FRAMES = 60
FADE_IN_FRAMES = 12
IDLE_FADE_IN_FRAMES = 20
IDLE_CYCLE_FRAMES = 80      # One breathing cycle
EXIT_START_FRAME = 266      # The star stays and keeps moving for a long time before it leaves
EXIT_FRAMES = 40
FILL_START_FRAME = 52       # Half star only: gold half starts to fill
FILL_FRAMES = 40

BREATHING_AMPLITUDE = 0.05
WOBBLE_DEGREES = 5.0
WOBBLE_PHASE = 1.0
BOB_PIXELS = 6.0
EXIT_SPIN_DEGREES = 160.0
OVERSHOOT = 1.70158         # Strength of the bounce in ease_out_back

MINI_STAR_COLOR = (255, 196, 40)
MINI_STAR_COUNT = 12
MINI_STAR_SIZE = 150       # Percent of the base mini star radius
MINI_STAR_FRAMES = 60
MINI_STAR_STAGGER_FRAMES = 1
MINI_STAR_DISTANCE_RATIO = 1.7   # How far the mini stars fly, relative to the star radius
MINI_STAR_SPIN_DEGREES = 220.0

SPARKLE_COLOR = (255, 247, 214)
SPARKLE_RADIUS = 26.0
SPARKLE_INNER_RATIO = 0.22
SPARKLE_FRAMES = 36
SPARKLE_STAGGER_FRAMES = 2
SPARKLE_BURST_END_RATIO = 1.3
TWINKLE_FRAMES = 50
TWINKLE_SIZE = 170
SPARKLE_SPIN_DEGREES = 90.0

REVEAL_MARGIN = 20.0        # The reveal mask is a bit bigger than the star


def clamp(value):
    return min(max(value, 0.0), 1.0)


def smoothstep(value):
    clamped = clamp(value)

    return clamped * clamped * (3 - 2 * clamped)


def ease_out_cubic(value):
    return 1 - (1 - clamp(value)) ** 3


def ease_in_cubic(value):
    return clamp(value) ** 3


def ease_out_back(value):
    """Runs from 0 to 1, shoots a bit over 1 and settles back."""
    shifted = clamp(value) - 1

    return 1 + (OVERSHOOT + 1) * shifted ** 3 + OVERSHOOT * shifted ** 2


def blend(
    start,
    end,
    weight,
):
    return start + (end - start) * weight


def to_lottie_color(color):
    return [channel / 255 for channel in color] + [1]


def build_static_property(value):
    return {"a": 0, "k": value}


def build_linear_keyframes(values_per_frame):
    """One keyframe per frame with linear interpolation, for an even movement."""
    keyframes = []

    for frame, value in enumerate(values_per_frame):
        value = value if isinstance(value, list) else [value]
        component_count = len(value)
        keyframes.append({
            "t": frame,
            "s": value,
            "i": {"x": [1] * component_count, "y": [1] * component_count},
            "o": {"x": [0] * component_count, "y": [0] * component_count},
        })

    # The last keyframe only holds the final value
    keyframes[-1] = {"t": keyframes[-1]["t"], "s": keyframes[-1]["s"]}

    return keyframes


def build_animated_property(values_per_frame):
    return {"a": 1, "k": build_linear_keyframes(values_per_frame=values_per_frame)}


def build_polygon_path(points):
    corner_count = len(points)

    return {
        "c": True,
        "v": [[round(x, 2), round(y, 2)] for x, y in points],
        "i": [[0, 0]] * corner_count,
        "o": [[0, 0]] * corner_count,
    }


def build_sparkle_points():
    """Four-point sparkle: long tips up, down, left and right, pinched in between."""
    points = []

    for index in range(8):
        is_tip = index % 2 == 0
        radius = SPARKLE_RADIUS if is_tip else SPARKLE_RADIUS * SPARKLE_INNER_RATIO
        angle = index * math.pi / 4
        points.append((radius * math.cos(angle), radius * math.sin(angle)))

    return points


def build_mini_star_points():
    """Small five-point star with sharp tips, used for the burst around the big star."""
    points = []

    for index in range(10):
        is_tip = index % 2 == 0
        radius = SPARKLE_RADIUS if is_tip else SPARKLE_RADIUS * 0.45
        angle = -math.pi / 2 + index * math.pi / 5
        points.append((radius * math.cos(angle), radius * math.sin(angle)))

    return points


def build_shape_group(
    shape_name,
    shape_item,
    paint_item,
):
    return {"ty": "gr", "nm": shape_name, "it": [
        shape_item,
        paint_item,
        {"ty": "tr", "p": build_static_property([0, 0]), "a": build_static_property([0, 0]),
         "s": build_static_property([100, 100]), "r": build_static_property(0),
         "o": build_static_property(100), "sk": build_static_property(0), "sa": build_static_property(0)},
    ]}


def build_path_item(points):
    return {"ty": "sh", "nm": "path", "ks": build_static_property(build_polygon_path(points=points))}


def build_solid_fill(color):
    return {"ty": "fl", "nm": "fill", "c": build_static_property(to_lottie_color(color)),
            "o": build_static_property(100), "r": 1}


def build_gradient_fill(
    gradient_type,
    start,
    end,
    color_stops,
    alpha_stops=(),
):
    """gradient_type: 1 = linear, 2 = radial. Alpha stops are appended after the color stops."""
    values = []

    for position, color in color_stops:
        values += [position, *[channel / 255 for channel in color]]

    for position, alpha in alpha_stops:
        values += [position, alpha]

    return {"ty": "gf", "nm": "gradient", "o": build_static_property(100), "r": 1, "t": gradient_type,
            "s": build_static_property(start), "e": build_static_property(end),
            "g": {"p": len(color_stops), "k": build_static_property(values)}}


def build_shape_layer(
    layer_name,
    shapes,
    position,
    rotation,
    scale,
    opacity,
    mask=None,
):
    layer = {
        "ddd": 0, "ind": 0, "ty": 4, "nm": layer_name, "sr": 1,
        "ks": {"o": opacity, "r": rotation, "p": position, "a": build_static_property([0, 0, 0]), "s": scale},
        "ao": 0, "shapes": shapes, "ip": 0, "op": LOOP_FRAMES, "st": 0, "bm": 0,
    }

    if mask is not None:
        layer["hasMask"] = True
        layer["masksProperties"] = [mask]

    return layer


def collect_states(build_frame_state):
    """Calls build_frame_state for every frame. Returns one list per value of the state."""
    states = [build_frame_state(frame=frame) for frame in range(LOOP_FRAMES + 1)]

    return [list(values) for values in zip(*states)]


class Sparkle:
    """A small shape (sparkle or mini star) that grows, spins and shrinks once per loop."""

    def __init__(
        self,
        name,
        start,
        end,
        start_frame,
        life_frames,
        size,
        spin_degrees,
        points,
        color,
    ):
        self._name = name
        self._points = points
        self._color = color
        self._start = start
        self._end = end
        self._start_frame = start_frame
        self._life_frames = life_frames
        self._size = size
        self._spin_degrees = spin_degrees

    def build_layer(self):
        positions, rotations, scales, opacities = collect_states(self._build_frame_state)

        return build_shape_layer(
            layer_name=self._name,
            shapes=[build_shape_group(
                shape_name="sparkle",
                shape_item=build_path_item(points=self._points),
                paint_item=build_solid_fill(color=self._color),
            )],
            position=build_animated_property(positions),
            rotation=build_animated_property(rotations),
            scale=build_animated_property(scales),
            opacity=build_animated_property(opacities),
        )

    def _build_frame_state(self, frame):
        progress = (frame - self._start_frame) / self._life_frames
        is_visible = 0 <= progress <= 1
        travel = ease_out_cubic(progress)

        return (
            [round(blend(self._start[0], self._end[0], travel), 2),
             round(blend(self._start[1], self._end[1], travel), 2), 0],
            round(self._spin_degrees * clamp(progress), 2),
            [round(self._size * math.sin(math.pi * progress), 2)] * 2 + [100] if is_visible else [0, 0, 100],
            100 if is_visible else 0,
        )


@dataclass(frozen=True)
class StarTimeline:
    appear: float           # 0..1 while the star arrives
    exit_progress: float    # 0..1 while the star leaves
    idle_weight: float      # 0..1, breathing fades in after landing and out before leaving
    idle_phase: float       # Angle in radians, one full cycle per IDLE_CYCLE_FRAMES


@dataclass(frozen=True)
class StarSpec:
    name: str
    is_half: bool
    entry_spin_degrees: float   # Rotation it arrives with (turns to 0)
    does_flip: bool             # True: turns around its vertical axis like a coin
    entry_slide_pixels: float   # How far below its place it starts
    burst_frame: int            # Frame of the mini star and sparkle burst
    sparkle_count: int
    twinkles: tuple             # ((frame, (x, y)), ...): when and where (relative to the star center) it twinkles


class AnimatedStar:
    """One star with its mini stars, sparkles and (for the half star) the fill reveal."""

    def __init__(self, spec):
        self._spec = spec
        self._center = (STAR_CENTER_X, STAR_CENTER_Y)
        self._outline = build_star_outline()

    def build_layers(self):
        """Returns the layers from top to bottom."""
        layers = self._build_sparkle_layers()
        layers.append(self._build_gold_layer())

        if self._spec.is_half:
            layers.append(self._build_empty_layer())

        return layers

    def _build_timeline(self, frame):
        frame_after_start = frame
        landed = smoothstep((frame_after_start - APPEAR_FRAMES) / IDLE_FADE_IN_FRAMES)
        exit_progress = clamp((frame_after_start - EXIT_START_FRAME) / EXIT_FRAMES)

        return StarTimeline(
            appear=clamp(frame_after_start / APPEAR_FRAMES),
            exit_progress=exit_progress,
            idle_weight=landed * (1 - exit_progress),
            idle_phase=2 * math.pi * (frame_after_start - APPEAR_FRAMES) / IDLE_CYCLE_FRAMES,
        )

    def _build_body_state(self, frame):
        """Position, rotation, scale and opacity of the star itself."""
        spec = self._spec
        timeline = self._build_timeline(frame=frame)
        arrival = ease_out_cubic(timeline.appear)
        size = ease_out_back(timeline.appear) * (1 - ease_in_cubic(timeline.exit_progress))
        breathing = 1 + BREATHING_AMPLITUDE * timeline.idle_weight * math.sin(timeline.idle_phase)
        flip = math.cos(2 * math.pi * (1 - arrival)) if spec.does_flip else 1.0

        rotation = (
            spec.entry_spin_degrees * (1 - arrival)
            + WOBBLE_DEGREES * timeline.idle_weight * math.sin(timeline.idle_phase + WOBBLE_PHASE)
            + EXIT_SPIN_DEGREES * ease_in_cubic(timeline.exit_progress)
        )
        offset_y = (
            spec.entry_slide_pixels * (1 - ease_out_back(timeline.appear))
            + BOB_PIXELS * timeline.idle_weight * math.sin(timeline.idle_phase)
        )
        fade_in = smoothstep(frame / FADE_IN_FRAMES)
        fade_out = 1 - smoothstep((timeline.exit_progress - 0.5) / 0.5)

        return (
            [round(self._center[0], 2), round(self._center[1] + offset_y, 2), 0],
            round(rotation, 2),
            [round(100 * size * breathing * flip, 2), round(100 * size * breathing, 2), 100],
            round(100 * fade_in * fade_out, 2),
        )

    def _build_body_properties(self):
        positions, rotations, scales, opacities = collect_states(self._build_body_state)

        return {
            "position": build_animated_property(positions),
            "rotation": build_animated_property(rotations),
            "scale": build_animated_property(scales),
            "opacity": build_animated_property(opacities),
        }

    def _build_gold_layer(self):
        spec = self._spec
        outline = clip_to_left_half(self._outline) if spec.is_half else self._outline
        body = self._build_body_properties()

        return build_shape_layer(
            layer_name=f"{spec.name}_gold",
            shapes=[build_shape_group(
                shape_name="gold",
                shape_item=build_path_item(points=outline),
                paint_item=build_gradient_fill(
                    gradient_type=1,
                    start=[0, -STAR_RADIUS],
                    end=[0, STAR_RADIUS],
                    color_stops=STAR_COLOR_STOPS,
                ),
            )],
            position=body["position"],
            rotation=body["rotation"],
            scale=body["scale"],
            opacity=body["opacity"],
            mask=self._build_reveal_mask() if spec.is_half else None,
        )

    def _build_empty_layer(self):
        body = self._build_body_properties()

        return build_shape_layer(
            layer_name=f"{self._spec.name}_empty",
            shapes=[build_shape_group(
                shape_name="empty",
                shape_item=build_path_item(points=self._outline),
                paint_item=build_solid_fill(color=EMPTY_STAR_COLOR),
            )],
            position=body["position"],
            rotation=body["rotation"],
            scale=body["scale"],
            opacity=body["opacity"],
        )

    def _build_reveal_mask(self):
        """A rectangle that grows from the left edge and uncovers the gold half."""
        keyframes = []

        for frame in range(LOOP_FRAMES + 1):
            keyframes.append({
                "t": frame,
                "s": [self._build_reveal_rectangle(frame=frame)],
                "i": {"x": 1, "y": 1},
                "o": {"x": 0, "y": 0},
            })

        keyframes[-1] = {"t": keyframes[-1]["t"], "s": keyframes[-1]["s"]}

        return {"inv": False, "mode": "a", "nm": "reveal", "o": build_static_property(100),
                "x": build_static_property(0), "pt": {"a": 1, "k": keyframes}}

    def _build_reveal_rectangle(self, frame):
        frame_after_start = frame
        fill_progress = smoothstep((frame_after_start - FILL_START_FRAME) / FILL_FRAMES)
        left = -STAR_RADIUS - REVEAL_MARGIN
        right = blend(left, REVEAL_MARGIN, fill_progress)
        top = -STAR_RADIUS - REVEAL_MARGIN
        bottom = STAR_RADIUS + REVEAL_MARGIN

        return {
            "c": True,
            "v": [[left, top], [right, top], [right, bottom], [left, bottom]],
            "i": [[0, 0]] * 4,
            "o": [[0, 0]] * 4,
        }

    def _build_sparkle_layers(self):
        spec = self._spec
        center_x, center_y = self._center
        sparkles = []

        for index in range(spec.sparkle_count):
            angle = -math.pi / 2 + 2 * math.pi * index / spec.sparkle_count
            direction = (math.cos(angle), math.sin(angle))
            is_large = index % 2 == 0
            sparkles.append(Sparkle(
                name=f"{spec.name}_sparkle_{index}",
                start=(center_x + direction[0] * STAR_RADIUS, center_y + direction[1] * STAR_RADIUS),
                end=(center_x + direction[0] * STAR_RADIUS * SPARKLE_BURST_END_RATIO,
                     center_y + direction[1] * STAR_RADIUS * SPARKLE_BURST_END_RATIO),
                start_frame=spec.burst_frame + index * SPARKLE_STAGGER_FRAMES,
                life_frames=SPARKLE_FRAMES,
                size=100 if is_large else 65,
                spin_degrees=SPARKLE_SPIN_DEGREES if is_large else -SPARKLE_SPIN_DEGREES,
                points=build_sparkle_points(),
                color=SPARKLE_COLOR,
            ))

        for index, (twinkle_frame, twinkle_offset) in enumerate(spec.twinkles):
            twinkle_position = (center_x + twinkle_offset[0], center_y + twinkle_offset[1])
            sparkles.append(Sparkle(
                name=f"{spec.name}_twinkle_{index}",
                start=twinkle_position,
                end=twinkle_position,
                start_frame=twinkle_frame,
                life_frames=TWINKLE_FRAMES,
                size=TWINKLE_SIZE,
                spin_degrees=SPARKLE_SPIN_DEGREES,
                points=build_sparkle_points(),
                color=SPARKLE_COLOR,
            ))

        sparkles += self._build_mini_stars()

        return [sparkle.build_layer() for sparkle in sparkles]

    def _build_mini_stars(self):
        """Small gold stars that fly out of the big star in all directions, like confetti."""
        center_x, center_y = self._center
        mini_stars = []

        for index in range(MINI_STAR_COUNT):
            # Half a step offset, so they fly between the sparkles
            angle = -math.pi / 2 + 2 * math.pi * (index + 0.5) / MINI_STAR_COUNT
            distance = STAR_RADIUS * MINI_STAR_DISTANCE_RATIO
            is_spinning_forward = index % 2 == 0
            mini_stars.append(Sparkle(
                name=f"{self._spec.name}_mini_star_{index}",
                start=(center_x, center_y),
                end=(center_x + math.cos(angle) * distance, center_y + math.sin(angle) * distance),
                start_frame=self._spec.burst_frame + index * MINI_STAR_STAGGER_FRAMES,
                life_frames=MINI_STAR_FRAMES,
                size=MINI_STAR_SIZE,
                spin_degrees=MINI_STAR_SPIN_DEGREES if is_spinning_forward else -MINI_STAR_SPIN_DEGREES,
                points=build_mini_star_points(),
                color=MINI_STAR_COLOR,
            ))

        return mini_stars


FULL_STAR_SPEC = StarSpec(
    name="full_star",
    is_half=False,
    entry_spin_degrees=-360,
    does_flip=False,
    entry_slide_pixels=0,
    burst_frame=34,
    sparkle_count=6,
    twinkles=(
        (105, (0.8 * STAR_RADIUS, -0.8 * STAR_RADIUS)),
        (170, (-0.75 * STAR_RADIUS, -0.5 * STAR_RADIUS)),
        (220, (0.7 * STAR_RADIUS, 0.55 * STAR_RADIUS)),
    ),
)

HALF_STAR_SPEC = StarSpec(
    name="half_star",
    is_half=True,
    entry_spin_degrees=-25,
    does_flip=True,
    entry_slide_pixels=90,
    burst_frame=FILL_START_FRAME + FILL_FRAMES,
    sparkle_count=4,
    twinkles=(
        (115, (-0.8 * STAR_RADIUS, -0.8 * STAR_RADIUS)),
        (180, (0.75 * STAR_RADIUS, -0.6 * STAR_RADIUS)),
        (225, (-0.7 * STAR_RADIUS, 0.55 * STAR_RADIUS)),
    ),
)


def number_layers(layers):
    for index, layer in enumerate(layers, start=1):
        layer["ind"] = index

    return layers


def build_animation(
    spec,
    title,
):
    return {
        "v": "5.7.4", "fr": FRAMES_PER_SECOND, "ip": 0, "op": LOOP_FRAMES,
        "w": CANVAS_SIZE, "h": CANVAS_SIZE, "nm": title, "ddd": 0,
        "assets": [], "layers": number_layers(AnimatedStar(spec=spec).build_layers()),
    }


def save_animation(
    spec,
    title,
    file_name,
):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / file_name

    with open(out_file, "w") as file:
        json.dump(build_animation(spec=spec, title=title), file, separators=(",", ":"))

    print(f"Saved: {out_file}")
