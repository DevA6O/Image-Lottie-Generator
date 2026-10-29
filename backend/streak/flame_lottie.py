"""
Streak flame as a Lottie animation (JSON), generated from scratch.

How it works:
  1. The three flame layers (outer, middle, core) are rendered by streak_flame.py
     and embedded as Base64 PNG, so the animation is a single file.
  2. Each layer flickers smoothly: stretch plus sideways sway, anchored at the bottom.
     There is a keyframe on EVERY frame with linear interpolation, so nothing slows down or jitters.
  3. Lava drops are vector shapes. They leave the flame at the sides and fly along a
     parabola with gravity. They turn in flight direction, stretch with speed, shrink and fade out.
  4. All motion is periodic over the loop length, so the loop is seamless.

Dependencies: pip install numpy pillow scipy (streak_flame.py must be in the same folder)
Output: streak_flame.json (in frontend/results/streak)
"""
import base64
import io
import json
import math

from streak_flame import OUT_DIR, FlameRenderer

CANVAS_SIZE = 512   # Animation size in pixels
FRAMES_PER_SECOND = 60
LOOP_FRAMES = 240   # 4 seconds per loop

# Bottom point of each flame layer (0..1). The flame stays fixed there while it flickers.
FLAME_ANCHORS = {
    "outer": (0.50, 0.92),
    "middle": (0.51, 0.895),
    "core": (0.51, 0.865),
}

# Flicker per layer: [(amplitude, cycles_per_loop, phase), ...]
# Few cycles per loop give a calm, soft movement.
FLAME_MOTION = {
    "outer": {"scale_y": [(2.5, 1, 0.0), (1.2, 3, 1.0)],
              "skew":    [(2.0, 1, 0.5), (0.6, 3, 0.0)]},
    "middle": {"scale_y": [(3.5, 3, 1.2), (1.2, 4, 0.3)],
               "skew":    [(2.5, 1, 2.0), (0.8, 3, 1.0)]},
    "core":  {"scale_y": [(4.5, 3, 2.0), (1.5, 4, 0.7)],
              "skew":    [(1.8, 3, 1.4)]},
}

# 1.0 = fast, smaller = slower. Speed, gravity and flight time are scaled together,
# so the flight path stays the same and only gets slower.
DROP_SPEED = 0.6
GRAVITY = 900.0 * DROP_SPEED ** 2                # px/s^2
DROP_FLIGHT_SECONDS = 0.75 / DROP_SPEED
DROP_SIDE_SLOT_FRAMES = LOOP_FRAMES // 2         # Per side: flight time plus a pause

DROP_OUTER_COLOR = [255 / 255, 104 / 255, 24 / 255, 1]   # Orange
DROP_CORE_COLOR = [255 / 255, 214 / 255, 96 / 255, 1]    # Yellow
DROP_RADIUS = 15.0
DROP_CORE_RADIUS_FACTOR = 0.55


def sum_of_sines(loop_progress, sine_parts):
    """Adds up sine waves. loop_progress runs from 0 to 1 over one loop."""
    return sum(
        amplitude * math.sin(2 * math.pi * cycles * loop_progress + phase)
        for amplitude, cycles, phase in sine_parts
    )


def smoothstep(value):
    clamped = min(max(value, 0.0), 1.0)

    return clamped * clamped * (3 - 2 * clamped)


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


def encode_png_data_uri(image):
    image = image.resize((CANVAS_SIZE, CANVAS_SIZE))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=True)

    return "data:image/png;base64," + base64.b64encode(buffer.getvalue()).decode()


def build_flame_layer(layer_index, layer_name):
    anchor_x, anchor_y = FLAME_ANCHORS[layer_name]
    anchor = [anchor_x * CANVAS_SIZE, anchor_y * CANVAS_SIZE, 0]
    motion = FLAME_MOTION[layer_name]
    scales = []
    skews = []

    for frame in range(LOOP_FRAMES + 1):
        loop_progress = frame / LOOP_FRAMES
        scale_y = 100 + sum_of_sines(loop_progress=loop_progress, sine_parts=motion["scale_y"])
        scale_x = 100 - 0.4 * (scale_y - 100)    # Taller flame gets a bit narrower
        scales.append([round(scale_x, 3), round(scale_y, 3), 100])
        skews.append(round(sum_of_sines(loop_progress=loop_progress, sine_parts=motion["skew"]), 3))

    return {
        "ddd": 0, "ind": layer_index, "ty": 2, "nm": layer_name, "refId": f"img_{layer_name}", "sr": 1,
        "ks": {"o": build_static_property(100), "r": build_static_property(0),
               "p": build_static_property(anchor), "a": build_static_property(anchor),
               "s": build_animated_property(scales), "sk": build_animated_property(skews),
               "sa": build_static_property(0)},
        "ao": 0, "ip": 0, "op": LOOP_FRAMES, "st": 0, "bm": 0,
    }


def build_teardrop_path(radius):
    """Teardrop: round head points to +x (flight direction), pointed tail to -x."""
    circle_handle = 0.5523 * radius     # Bezier constant for circle arcs
    tail_length = 2.4 * radius

    return {
        "c": True,
        "v": [[-tail_length, 0], [0, -radius], [radius, 0], [0, radius]],
        "i": [[0.9 * radius, 0.25 * radius], [-0.9 * radius, 0], [0, -circle_handle], [circle_handle, 0]],
        "o": [[0.9 * radius, -0.25 * radius], [circle_handle, 0], [0, circle_handle], [-0.9 * radius, 0]],
    }


def build_filled_shape(shape_name, path, color):
    return {"ty": "gr", "nm": shape_name, "it": [
        {"ty": "sh", "nm": "path", "ks": build_static_property(path)},
        {"ty": "fl", "nm": "fill", "c": build_static_property(color), "o": build_static_property(100), "r": 1},
        {"ty": "tr", "p": build_static_property([0, 0]), "a": build_static_property([0, 0]),
         "s": build_static_property([100, 100]), "r": build_static_property(0),
         "o": build_static_property(100), "sk": build_static_property(0), "sa": build_static_property(0)},
    ]}


class LavaDrop:
    """One lava drop that flies once per loop along a parabola."""

    def __init__(
        self,
        start,
        velocity,
        size,
        frame_offset,
    ):
        self._start_x, self._start_y = start
        self._velocity_x = velocity[0] * DROP_SPEED
        self._velocity_y = velocity[1] * DROP_SPEED
        self._size = size
        self._frame_offset = frame_offset
        self._flight_frames = DROP_FLIGHT_SECONDS * FRAMES_PER_SECOND
        self._previous_angle = 0.0

    def build_layer(self, layer_index):
        self._previous_angle = 0.0
        positions = []
        rotations = []
        scales = []
        opacities = []

        for frame in range(LOOP_FRAMES + 1):
            position, rotation, scale, opacity = self._build_frame_state(frame=frame)
            positions.append(position)
            rotations.append(rotation)
            scales.append(scale)
            opacities.append(opacity)

        return {
            "ddd": 0, "ind": layer_index, "ty": 4, "nm": f"lava_drop_{layer_index}", "sr": 1,
            "ks": {"o": build_animated_property(opacities), "r": build_animated_property(rotations),
                   "p": build_animated_property(positions), "a": build_static_property([0, 0, 0]),
                   "s": build_animated_property(scales)},
            "ao": 0,
            "shapes": [
                build_filled_shape(     # Bright core on top
                    shape_name="core",
                    path=build_teardrop_path(radius=DROP_RADIUS * DROP_CORE_RADIUS_FACTOR),
                    color=DROP_CORE_COLOR,
                ),
                build_filled_shape(
                    shape_name="outer",
                    path=build_teardrop_path(radius=DROP_RADIUS),
                    color=DROP_OUTER_COLOR,
                ),
            ],
            "ip": 0, "op": LOOP_FRAMES, "st": 0, "bm": 0,
        }

    def _build_frame_state(self, frame):
        frame_in_flight = (frame - self._frame_offset) % LOOP_FRAMES
        seconds = frame_in_flight / FRAMES_PER_SECOND
        is_flying = frame_in_flight <= self._flight_frames
        flight_progress = frame_in_flight / self._flight_frames

        x = self._start_x + self._velocity_x * seconds
        y = self._start_y + self._velocity_y * seconds + 0.5 * GRAVITY * seconds * seconds
        current_velocity_y = self._velocity_y + GRAVITY * seconds
        speed = math.hypot(self._velocity_x, current_velocity_y)

        rotation = self._build_continuous_angle(
            velocity_y=current_velocity_y,
            is_flight_start=frame_in_flight == 0,
        )
        stretch = 1 + 0.35 * min(speed / 400, 1.2)
        grow = smoothstep(flight_progress / 0.15)                   # Appears quickly
        shrink = 1 - 0.55 * smoothstep((flight_progress - 0.4) / 0.6)     # Shrinks slowly
        scale = 100 * self._size * grow * shrink
        fade = 1 - smoothstep((flight_progress - 0.55) / 0.45)

        if not is_flying:
            scale, fade = 0, 0

        return (
            [round(x, 2), round(y, 2), 0],
            round(rotation, 2),
            [round(scale * stretch, 2), round(scale / math.sqrt(stretch), 2), 100],
            round(100 * fade, 2),
        )

    def _build_continuous_angle(
        self,
        velocity_y,
        is_flight_start,
    ):
        """
        Flight direction in degrees without jumps. atan2 jumps at +-180 degrees, and
        Lottie would then spin the drop almost a full turn within one frame (drops flying left).
        """
        angle = math.degrees(math.atan2(velocity_y, self._velocity_x))

        if not is_flight_start:
            angle += 360 * round((self._previous_angle - angle) / 360)

        self._previous_angle = angle

        return angle


# Per loop: left, pause, right, pause. A drop only appears after the previous one is gone.
# The small pops at the bottom fly on the opposite side while the big drop is in the air.
LAVA_DROPS = [
    LavaDrop(start=(150, 330), velocity=(-150, -330), size=1.00, frame_offset=0),
    LavaDrop(start=(365, 320), velocity=(160, -350), size=1.00, frame_offset=DROP_SIDE_SLOT_FRAMES),
    LavaDrop(start=(380, 380), velocity=(120, -280), size=0.70, frame_offset=40),
    LavaDrop(start=(138, 385), velocity=(-110, -260), size=0.65, frame_offset=DROP_SIDE_SLOT_FRAMES + 40),
]


def build_animation():
    outer_image, middle_image, core_image = FlameRenderer().render_layers()
    assets = [
        {"id": f"img_{layer_name}", "w": CANVAS_SIZE, "h": CANVAS_SIZE, "u": "",
         "p": encode_png_data_uri(image), "e": 1}
        for layer_name, image in (("outer", outer_image), ("middle", middle_image), ("core", core_image))
    ]

    # The first layer in the array is on top. Drops sit behind the flame,
    # so they appear from behind its edge and move outwards.
    layers = [
        build_flame_layer(layer_index=1, layer_name="core"),
        build_flame_layer(layer_index=2, layer_name="middle"),
        build_flame_layer(layer_index=3, layer_name="outer"),
    ]
    layers += [drop.build_layer(layer_index=4 + index) for index, drop in enumerate(LAVA_DROPS)]

    return {
        "v": "5.7.4", "fr": FRAMES_PER_SECOND, "ip": 0, "op": LOOP_FRAMES,
        "w": CANVAS_SIZE, "h": CANVAS_SIZE, "nm": "Streak Flame", "ddd": 0,
        "assets": assets, "layers": layers,
    }


def save_animation():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUT_DIR / "streak_flame.json"

    with open(out_file, "w") as file:
        json.dump(build_animation(), file, separators=(",", ":"))

    print(f"Saved: {out_file}")


if __name__ == "__main__":
    save_animation()
