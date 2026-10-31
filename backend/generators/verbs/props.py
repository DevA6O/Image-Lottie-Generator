"""
Props and symbols for the verb scenes (question marks, bubbles, boxes, arrows ...).
Every prop is flat and has no text. Positions are final pixels. `size` is roughly the radius of the prop.
"""
import math

from painting.flat_painter import (
    build_arc_points,
    build_polyline_points,
    build_star_points,
    move_point,
    rotate_point,
    sample_curve,
    solid,
)

WHITE = (252, 252, 255)
BUBBLE = (234, 240, 252)
GRAY = (176, 184, 202)
DARK_GRAY = (96, 106, 130)
YELLOW = (255, 208, 64)
GOLD = (255, 190, 40)
ORANGE = (250, 150, 50)
RED = (238, 84, 84)
PINK = (250, 130, 170)
BLUE = (78, 140, 230)
LIGHT_BLUE = (150, 200, 250)
GREEN = (80, 190, 110)
BROWN = (160, 100, 58)
ICE = (176, 222, 250)
ICE_LIGHT = (226, 245, 255)
ICE_SPARKLE = (120, 190, 240)
WOOD = (214, 160, 100)

HEART_POINT_COUNT = 80
HEART_HALF_WIDTH = 16


def draw_question_mark(
    painter,
    center,
    size=1.0,
    color=BLUE,
):
    arc_center = (center[0], center[1] - 22 * size)
    hook = build_arc_points(center=arc_center, radius=30 * size, start_angle=170, end_angle=400)
    stem = [(center[0] + 2 * size, center[1] + 8 * size), (center[0], center[1] + 18 * size)]
    painter.fill_curve(points=hook + stem, width=14 * size, shade=solid(color))
    painter.fill_circle(center=(center[0], center[1] + 46 * size), radius=9 * size, shade=solid(color))


def draw_exclamation_mark(
    painter,
    center,
    size=1.0,
    color=ORANGE,
):
    painter.fill_stroke(
        start=(center[0], center[1] - 50 * size),
        end=(center[0], center[1] + 8 * size),
        width=16 * size,
        shade=solid(color),
    )
    painter.fill_circle(center=(center[0], center[1] + 40 * size), radius=10 * size, shade=solid(color))


def draw_heart(
    painter,
    center,
    size=1.0,
    color=RED,
):
    points = []

    for step in range(HEART_POINT_COUNT):
        t = 2 * math.pi * step / HEART_POINT_COUNT
        x = 16 * math.sin(t) ** 3
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        points.append((center[0] + x * size / HEART_HALF_WIDTH, center[1] + y * size / HEART_HALF_WIDTH))

    painter.fill_polygon(points=points, shade=solid(color))


def draw_star(
    painter,
    center,
    size=1.0,
    color=YELLOW,
):
    points = build_star_points(center=center, outer_radius=size, inner_radius=size * 0.46, tip_count=5)
    painter.fill_polygon(points=points, shade=solid(color))


def draw_sparkle(
    painter,
    center,
    size=1.0,
    color=YELLOW,
):
    points = build_star_points(center=center, outer_radius=size, inner_radius=size * 0.28, tip_count=4)
    painter.flat_polygon(points=points, color=color)


def draw_check_mark(
    painter,
    center,
    size=1.0,
    color=GREEN,
    width=22,
):
    corners = [
        (center[0] - size, center[1] + 0.05 * size),
        (center[0] - 0.3 * size, center[1] + 0.7 * size),
        (center[0] + size, center[1] - 0.7 * size),
    ]
    painter.fill_curve(points=build_polyline_points(corners=corners), width=width, shade=solid(color))


def draw_arrow(
    painter,
    start,
    end,
    color=BLUE,
    width=22,
):
    length = math.hypot(end[0] - start[0], end[1] - start[1])
    direction = ((end[0] - start[0]) / length, (end[1] - start[1]) / length)
    side = (-direction[1], direction[0])
    head_length = width * 2.2
    head_base = (end[0] - direction[0] * head_length, end[1] - direction[1] * head_length)
    shaft_end = (end[0] - direction[0] * head_length * 0.6, end[1] - direction[1] * head_length * 0.6)

    painter.fill_stroke(start=start, end=shaft_end, width=width, shade=solid(color))
    painter.fill_polygon(
        points=[
            end,
            (head_base[0] + side[0] * width * 1.2, head_base[1] + side[1] * width * 1.2),
            (head_base[0] - side[0] * width * 1.2, head_base[1] - side[1] * width * 1.2),
        ],
        shade=solid(color),
    )


def draw_wind_lines(
    painter,
    origin,
    length,
    count=3,
    color=(140, 172, 220),
):
    """Wavy lines that trail to the left of the origin. A negative length trails to the right."""
    for index in range(count):
        y = origin[1] + (index - (count - 1) / 2) * 44
        line_length = length * (0.65 + 0.35 * ((index + 1) % 2))
        start = (origin[0], y)
        end = (origin[0] - line_length, y)
        points = sample_curve(
            start=start,
            first_control=(origin[0] - line_length * 0.3, y - 16),
            second_control=(origin[0] - line_length * 0.65, y + 16),
            end=end,
        )
        painter.flat_curve(points=points, width=11, color=color)


def draw_sweat_drop(
    painter,
    center,
    radius=14,
    color=LIGHT_BLUE,
):
    tip = (center[0], center[1] - 2.2 * radius)
    painter.fill_polygon(points=[tip] + build_arc_points(center=center, radius=radius, start_angle=-27, end_angle=207), shade=solid(color))


def draw_speech_bubble(
    painter,
    center,
    width,
    height,
    tail_tip,
    color=BUBBLE,
):
    box = (center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2)
    body_mask = painter.build_rounded_rect_mask(box=box, radius=min(width, height) * 0.4)
    base_x = min(max(tail_tip[0], box[0] + 60), box[2] - 60)
    tail_mask = painter.build_polygon_mask(points=[(base_x - 24, box[3] - 6), (base_x + 24, box[3] - 6), tail_tip])
    painter.fill(mask=painter.union_masks(first_mask=body_mask, second_mask=tail_mask), shade=solid(color))


def draw_text_lines(
    painter,
    center,
    width,
    count=2,
    color=(150, 162, 190),
):
    """Gray bars that look like text. They never spell a word."""
    for index in range(count):
        y = center[1] + (index - (count - 1) / 2) * 34
        line_width = width * (1.0 if index % 2 == 0 else 0.65)
        left = center[0] - width / 2
        painter.flat_stroke(start=(left, y), end=(left + line_width, y), width=12, color=color)


def draw_thought_bubble(
    painter,
    center,
    width,
    height,
    tail_tip,
    color=BUBBLE,
):
    box = (center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2)
    cloud_mask = painter.build_rounded_rect_mask(box=box, radius=height * 0.42)

    for fraction, rise in ((0.25, 0.1), (0.5, 0.22), (0.75, 0.1)):
        bump = painter.build_rotated_ellipse_mask(
            center=(box[0] + width * fraction, box[1] + 10),
            radius_x=width * 0.17,
            radius_y=height * (0.3 + rise),
        )
        cloud_mask = painter.union_masks(first_mask=cloud_mask, second_mask=bump)

    painter.fill(mask=cloud_mask, shade=solid(color))

    for fraction, radius in ((0.5, 18), (0.8, 11)):
        dot = (center[0] + (tail_tip[0] - center[0]) * fraction, box[3] + (tail_tip[1] - box[3]) * fraction)
        painter.fill_circle(center=dot, radius=radius, shade=solid(color))


def draw_lightbulb(
    painter,
    center,
    size=1.0,
    glowing=True,
):
    glass_color = YELLOW if glowing else (214, 218, 228)

    if glowing:
        for angle in (-160, -125, -90, -55, -20):
            painter.flat_stroke(
                start=move_point(point=center, angle=angle, distance=1.4 * 60 * size),
                end=move_point(point=center, angle=angle, distance=1.85 * 60 * size),
                width=11 * size,
                color=GOLD,
            )

    painter.fill_circle(center=center, radius=60 * size, shade=solid(glass_color))
    base_box = (center[0] - 30 * size, center[1] + 52 * size, center[0] + 30 * size, center[1] + 96 * size)
    painter.fill_rounded_rect(box=base_box, radius=10 * size, shade=solid(DARK_GRAY))


def draw_gift_box(
    painter,
    center,
    size=1.0,
    color=RED,
):
    painter.fill_rounded_rect(
        box=(center[0] - 70 * size, center[1] - 30 * size, center[0] + 70 * size, center[1] + 70 * size),
        radius=8 * size,
        shade=solid(color),
    )
    painter.fill_rounded_rect(
        box=(center[0] - 80 * size, center[1] - 62 * size, center[0] + 80 * size, center[1] - 14 * size),
        radius=8 * size,
        shade=solid(color),
    )
    painter.flat_polygon(
        points=[
            (center[0] - 14 * size, center[1] - 62 * size),
            (center[0] + 14 * size, center[1] - 62 * size),
            (center[0] + 14 * size, center[1] + 70 * size),
            (center[0] - 14 * size, center[1] + 70 * size),
        ],
        color=YELLOW,
    )

    for side in (-1, 1):
        painter.fill_ellipse(
            center=(center[0] + side * 30 * size, center[1] - 84 * size),
            radius_x=34 * size,
            radius_y=20 * size,
            shade=solid(YELLOW),
            angle=side * -25,
        )


def draw_coin(
    painter,
    center,
    radius=40.0,
):
    painter.fill_circle(center=center, radius=radius, shade=solid(GOLD))
    painter.flat_circle(center=center, radius=radius * 0.72, color=(236, 160, 24))
    painter.flat_circle(center=center, radius=radius * 0.56, color=(255, 214, 80))


def draw_open_book(
    painter,
    center,
    width,
    height,
):
    painter.fill_rounded_rect(
        box=(center[0] - width / 2 - 12, center[1] - height / 2 - 10, center[0] + width / 2 + 12, center[1] + height / 2 + 12),
        radius=14,
        shade=solid((184, 78, 78)),
    )

    for side in (-1, 1):
        left = center[0] - 3 if side == 1 else center[0] - width / 2
        right = center[0] + width / 2 if side == 1 else center[0] + 3
        painter.fill_rounded_rect(box=(left, center[1] - height / 2, right, center[1] + height / 2), radius=8, shade=solid(WHITE))
        draw_text_lines(painter=painter, center=(center[0] + side * width * 0.25, center[1]), width=width * 0.36, count=3)


def draw_closed_book(
    painter,
    center,
    width,
    height,
    color=RED,
):
    painter.fill_rounded_rect(
        box=(center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2),
        radius=10,
        shade=solid(color),
    )
    painter.flat_stroke(
        start=(center[0] - width / 2 + 22, center[1] - height / 2 + 8),
        end=(center[0] - width / 2 + 22, center[1] + height / 2 - 8),
        width=8,
        color=(255, 255, 255),
    )
    draw_text_lines(painter=painter, center=(center[0] + 14, center[1]), width=width * 0.5, count=2, color=WHITE)


def draw_paper(
    painter,
    center,
    width,
    height,
    line_count=3,
):
    painter.fill_rounded_rect(
        box=(center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2),
        radius=10,
        shade=solid(WHITE),
    )
    draw_text_lines(painter=painter, center=center, width=width * 0.7, count=line_count)


def draw_pencil(
    painter,
    tip,
    angle,
):
    """The pencil points to `tip`. The angle (0 right, 90 down) is the direction from the tip to the eraser."""
    wood_end = move_point(point=tip, angle=angle, distance=46)
    body_end = move_point(point=tip, angle=angle, distance=190)
    eraser_end = move_point(point=tip, angle=angle, distance=222)
    painter.fill_stroke(start=wood_end, end=body_end, width=34, shade=solid(YELLOW))
    painter.fill_stroke(start=body_end, end=eraser_end, width=34, shade=solid(PINK))
    side = move_point(point=(0, 0), angle=angle + 90, distance=17)
    painter.fill_polygon(
        points=[tip, (wood_end[0] + side[0], wood_end[1] + side[1]), (wood_end[0] - side[0], wood_end[1] - side[1])],
        shade=solid((240, 200, 150)),
    )


def draw_door(
    painter,
    bottom_center,
    width,
    height,
    is_open,
):
    left = bottom_center[0] - width / 2
    top = bottom_center[1] - height
    painter.fill_rounded_rect(
        box=(left - 16, top - 16, left + width + 16, bottom_center[1]),
        radius=12,
        shade=solid(BROWN),
    )
    painter.flat_polygon(
        points=[(left, top), (left + width, top), (left + width, bottom_center[1]), (left, bottom_center[1])],
        color=(58, 48, 74) if is_open else (206, 138, 80),
    )

    if is_open:
        panel_right = left + width * 0.42
        painter.fill_polygon(
            points=[(left, top), (panel_right, top + height * 0.07), (panel_right, bottom_center[1] - height * 0.03), (left, bottom_center[1])],
            shade=solid((206, 138, 80)),
        )
        painter.flat_circle(center=(panel_right - 14, bottom_center[1] - height * 0.45), radius=8, color=GOLD)
    else:
        painter.flat_circle(center=(left + width - 26, bottom_center[1] - height * 0.45), radius=10, color=GOLD)


def draw_chair(
    painter,
    seat_center,
    size=1.0,
):
    for side in (-1, 1):
        painter.fill_stroke(
            start=(seat_center[0] + side * 56 * size, seat_center[1]),
            end=(seat_center[0] + side * 64 * size, seat_center[1] + 150 * size),
            width=18 * size,
            shade=solid(BROWN),
        )
        painter.fill_stroke(
            start=(seat_center[0] + side * 60 * size, seat_center[1]),
            end=(seat_center[0] + side * 60 * size, seat_center[1] - 130 * size),
            width=18 * size,
            shade=solid(BROWN),
        )

    painter.fill_rounded_rect(
        box=(seat_center[0] - 78 * size, seat_center[1] - 12 * size, seat_center[0] + 78 * size, seat_center[1] + 22 * size),
        radius=10 * size,
        shade=solid(WOOD),
    )
    painter.fill_rounded_rect(
        box=(seat_center[0] - 70 * size, seat_center[1] - 138 * size, seat_center[0] + 70 * size, seat_center[1] - 100 * size),
        radius=10 * size,
        shade=solid(WOOD),
    )


def draw_eye(
    painter,
    center,
    size=1.0,
):
    half_width = 130 * size
    half_height = 70 * size
    upper = sample_curve(
        start=(center[0] - half_width, center[1]),
        first_control=(center[0] - half_width * 0.5, center[1] - half_height * 1.4),
        second_control=(center[0] + half_width * 0.5, center[1] - half_height * 1.4),
        end=(center[0] + half_width, center[1]),
    )
    lower = [(x, 2 * center[1] - y) for x, y in upper[::-1]]
    painter.fill_polygon(points=upper + lower, shade=solid(WHITE))
    painter.fill_circle(center=center, radius=50 * size, shade=solid(BLUE))
    painter.flat_circle(center=center, radius=24 * size, color=(36, 40, 70))
    painter.flat_circle(center=(center[0] - 16 * size, center[1] - 16 * size), radius=10 * size, color=WHITE)


def draw_sound_waves(
    painter,
    center,
    size=1.0,
    facing=1,
    color=BLUE,
):
    """Three arcs. facing=1 opens to the right, facing=-1 to the left."""
    start_angle, end_angle = (-42, 42) if facing == 1 else (138, 222)

    for index in (1, 2, 3):
        arc = build_arc_points(center=center, radius=42 * index * size, start_angle=start_angle, end_angle=end_angle)
        painter.flat_curve(points=arc, width=13 * size, color=color)


def draw_music_note(
    painter,
    center,
    size=1.0,
    color=PINK,
):
    stem_x = center[0] + 15 * size
    painter.fill_ellipse(center=center, radius_x=19 * size, radius_y=14 * size, shade=solid(color), angle=-20)
    painter.fill_stroke(start=(stem_x, center[1] - 4 * size), end=(stem_x, center[1] - 78 * size), width=9 * size, shade=solid(color))
    flag = sample_curve(
        start=(stem_x, center[1] - 78 * size),
        first_control=(stem_x + 30 * size, center[1] - 66 * size),
        second_control=(stem_x + 36 * size, center[1] - 44 * size),
        end=(stem_x + 22 * size, center[1] - 30 * size),
    )
    painter.fill_curve(points=flag, width=10 * size, shade=solid(color))


def draw_magnifier(
    painter,
    center,
    radius,
    handle_angle=45,
):
    handle_start = move_point(point=center, angle=handle_angle, distance=radius)
    handle_end = move_point(point=center, angle=handle_angle, distance=radius + 90)
    painter.fill_stroke(start=handle_start, end=handle_end, width=24, shade=solid(BROWN))
    painter.fill_circle(center=center, radius=radius, shade=solid((200, 230, 255)))
    painter.fill_ring(center=center, outer_radius=radius, inner_radius=radius - 16, color=(70, 100, 160))


def draw_key(
    painter,
    center,
    size=1.0,
):
    painter.fill_ring(center=center, outer_radius=36 * size, inner_radius=15 * size, color=GOLD)
    shaft_end = (center[0] + 130 * size, center[1])
    painter.fill_stroke(start=(center[0] + 30 * size, center[1]), end=shaft_end, width=16 * size, shade=solid(GOLD))

    for offset in (80, 118):
        painter.fill_stroke(
            start=(center[0] + offset * size, center[1]),
            end=(center[0] + offset * size, center[1] + 28 * size),
            width=14 * size,
            shade=solid(GOLD),
        )


def draw_shopping_bag(
    painter,
    center,
    size=1.0,
    color=PINK,
):
    handle = build_arc_points(center=(center[0], center[1] - 36 * size), radius=32 * size, start_angle=180, end_angle=360)
    painter.flat_curve(points=handle, width=12 * size, color=DARK_GRAY)
    painter.fill_polygon(
        points=[
            (center[0] - 62 * size, center[1] - 40 * size),
            (center[0] + 62 * size, center[1] - 40 * size),
            (center[0] + 76 * size, center[1] + 80 * size),
            (center[0] - 76 * size, center[1] + 80 * size),
        ],
        shade=solid(color),
    )
    draw_star(painter=painter, center=(center[0], center[1] + 20 * size), size=22 * size, color=WHITE)


def draw_flag(
    painter,
    pole_bottom,
    pole_height,
    width=150,
    height=96,
    color=GREEN,
):
    top = pole_bottom[1] - pole_height
    painter.fill_stroke(start=pole_bottom, end=(pole_bottom[0], top), width=14, shade=solid(BROWN))
    upper_edge = sample_curve(
        start=(pole_bottom[0], top),
        first_control=(pole_bottom[0] + width * 0.3, top - 24),
        second_control=(pole_bottom[0] + width * 0.65, top + 24),
        end=(pole_bottom[0] + width, top),
    )
    lower_edge = [(x, y + height) for x, y in upper_edge[::-1]]
    painter.fill_polygon(points=upper_edge + lower_edge, shade=solid(color))


def draw_plant(
    painter,
    pot_center,
    stem_height,
    leaf_count,
    has_flower,
):
    painter.fill_polygon(
        points=[
            (pot_center[0] - 62, pot_center[1] - 40),
            (pot_center[0] + 62, pot_center[1] - 40),
            (pot_center[0] + 46, pot_center[1] + 46),
            (pot_center[0] - 46, pot_center[1] + 46),
        ],
        shade=solid((214, 120, 84)),
    )
    stem_top = (pot_center[0], pot_center[1] - 40 - stem_height)
    stem = sample_curve(
        start=(pot_center[0], pot_center[1] - 40),
        first_control=(pot_center[0] + 14, pot_center[1] - 40 - stem_height * 0.35),
        second_control=(pot_center[0] - 14, pot_center[1] - 40 - stem_height * 0.7),
        end=stem_top,
    )
    painter.fill_curve(points=stem, width=14, shade=solid((70, 160, 80)))

    for index in range(leaf_count):
        side = 1 if index % 2 == 0 else -1
        leaf_y = pot_center[1] - 40 - stem_height * (0.25 + 0.5 * index / max(leaf_count, 1))
        painter.fill_ellipse(
            center=(pot_center[0] + side * 44, leaf_y),
            radius_x=44,
            radius_y=19,
            shade=solid((100, 200, 100)),
            angle=side * -30,
        )

    if has_flower:
        for angle in range(0, 360, 72):
            painter.fill_circle(center=move_point(point=stem_top, angle=angle, distance=30), radius=24, shade=solid(PINK))

        painter.fill_circle(center=stem_top, radius=20, shade=solid(YELLOW))


def draw_brick_wall(
    painter,
    left_bottom,
    column_count,
    row_count,
):
    brick_width = 96
    brick_height = 46

    for row in range(row_count):
        shift = (brick_width / 2) if row % 2 else 0

        for column in range(column_count):
            x = left_bottom[0] + shift + column * (brick_width + 6)
            y = left_bottom[1] - (row + 1) * (brick_height + 6)
            painter.fill_rounded_rect(box=(x, y, x + brick_width, y + brick_height), radius=6, shade=solid((218, 112, 82)))


def draw_scissors(
    painter,
    pivot,
    size=1.0,
    open_angle=18,
    direction=-90,
):
    """Blades point to `direction` (0 right, 90 down, -90 up) and open by `open_angle` degrees."""
    for sign in (-1, 1):
        blade_angle = direction + sign * open_angle
        blade_tip = move_point(point=pivot, angle=blade_angle, distance=190 * size)
        painter.fill_stroke(start=pivot, end=blade_tip, width=26 * size, shade=solid((200, 208, 224)))
        handle_center = move_point(point=pivot, angle=blade_angle + 180 - sign * 14, distance=74 * size)
        painter.fill_ring(center=handle_center, outer_radius=38 * size, inner_radius=20 * size, color=RED)

    painter.flat_circle(center=pivot, radius=11 * size, color=DARK_GRAY)


def draw_crown(
    painter,
    center,
    size=1.0,
):
    painter.fill_polygon(
        points=[
            (center[0] - size, center[1] + 0.7 * size),
            (center[0] - size, center[1] - 0.3 * size),
            (center[0] - 0.5 * size, center[1] + 0.25 * size),
            (center[0], center[1] - 0.6 * size),
            (center[0] + 0.5 * size, center[1] + 0.25 * size),
            (center[0] + size, center[1] - 0.3 * size),
            (center[0] + size, center[1] + 0.7 * size),
        ],
        shade=solid(GOLD),
    )

    for offset, color in ((-0.5, RED), (0, BLUE), (0.5, GREEN)):
        painter.flat_circle(center=(center[0] + offset * size, center[1] + 0.4 * size), radius=0.12 * size, color=color)


def draw_bird(
    painter,
    center,
    size=1.0,
    color=BLUE,
    facing=1,
):
    painter.fill_ellipse(center=center, radius_x=60 * size, radius_y=42 * size, shade=solid(color))
    painter.fill_circle(center=(center[0] + facing * 52 * size, center[1] - 30 * size), radius=28 * size, shade=solid(color))
    beak_base = (center[0] + facing * 76 * size, center[1] - 30 * size)
    painter.fill_polygon(
        points=[
            (beak_base[0], beak_base[1] - 9 * size),
            (beak_base[0] + facing * 28 * size, beak_base[1] + 4 * size),
            (beak_base[0], beak_base[1] + 12 * size),
        ],
        shade=solid(ORANGE),
    )
    painter.fill_ellipse(center=(center[0] - 4 * size, center[1] - 8 * size), radius_x=34 * size, radius_y=16 * size, shade=solid(LIGHT_BLUE), angle=facing * -25)
    painter.flat_circle(center=(center[0] + facing * 58 * size, center[1] - 36 * size), radius=5 * size, color=(40, 40, 60))
    painter.fill_polygon(
        points=[
            (center[0] - facing * 54 * size, center[1] - 8 * size),
            (center[0] - facing * 108 * size, center[1] - 30 * size),
            (center[0] - facing * 100 * size, center[1] + 14 * size),
        ],
        shade=solid(color),
    )


def draw_footprints(
    painter,
    start,
    end,
    count,
    color=(150, 170, 204),
):
    angle = math.degrees(math.atan2(end[1] - start[1], end[0] - start[0]))

    for index in range(count):
        progress = index / max(count - 1, 1)
        point = (start[0] + (end[0] - start[0]) * progress, start[1] + (end[1] - start[1]) * progress)
        offset = 22 if index % 2 == 0 else -22
        sideways = move_point(point=point, angle=angle + 90, distance=offset)
        painter.flat_ellipse(center=sideways, radius_x=26, radius_y=14, color=color, angle=angle)


def draw_dust_puff(
    painter,
    center,
    size=1.0,
    color=(206, 214, 230),
):
    for offset_x, offset_y, radius in ((-40, 8, 30), (0, -8, 40), (42, 6, 32)):
        painter.fill_circle(center=(center[0] + offset_x * size, center[1] + offset_y * size), radius=radius * size, shade=solid(color))


def draw_shards(
    painter,
    center,
    spread,
    color,
):
    """Sharp pieces that fly away from the center."""
    for angle in range(0, 360, 60):
        tip = move_point(point=center, angle=angle, distance=spread)
        base = move_point(point=center, angle=angle, distance=spread * 0.45)
        left = move_point(point=base, angle=angle + 90, distance=spread * 0.2)
        right = move_point(point=base, angle=angle - 90, distance=spread * 0.2)
        painter.fill_polygon(points=[tip, left, right], shade=solid(color))


def draw_cloud(
    painter,
    center,
    size=1.0,
    color=WHITE,
):
    for offset_x, offset_y, radius in ((-62, 10, 42), (-10, -14, 56), (50, 8, 46)):
        painter.fill_circle(center=(center[0] + offset_x * size, center[1] + offset_y * size), radius=radius * size, shade=solid(color))

    painter.fill_rounded_rect(
        box=(center[0] - 100 * size, center[1] + 8 * size, center[0] + 94 * size, center[1] + 52 * size),
        radius=22 * size,
        shade=solid(color),
    )


def draw_sun(
    painter,
    center,
    radius=80,
):
    for angle in range(0, 360, 45):
        painter.fill_stroke(
            start=move_point(point=center, angle=angle, distance=radius * 1.3),
            end=move_point(point=center, angle=angle, distance=radius * 1.7),
            width=16,
            shade=solid(GOLD),
        )

    painter.fill_circle(center=center, radius=radius, shade=solid(YELLOW))


def draw_hat(
    painter,
    center,
    size=1.0,
    color=RED,
):
    """The center is the middle of the brim."""
    painter.fill_rounded_rect(
        box=(center[0] - 62 * size, center[1] - 90 * size, center[0] + 62 * size, center[1] + 4 * size),
        radius=26 * size,
        shade=solid(color),
    )
    painter.flat_stroke(start=(center[0] - 62 * size, center[1] - 14 * size), end=(center[0] + 62 * size, center[1] - 14 * size), width=18 * size, color=YELLOW)
    painter.fill_ellipse(center=center, radius_x=100 * size, radius_y=20 * size, shade=solid(color))


def draw_microphone(
    painter,
    center,
    size=1.0,
):
    handle_end = (center[0] + 40 * size, center[1] + 110 * size)
    painter.fill_stroke(start=center, end=handle_end, width=26 * size, shade=solid(DARK_GRAY))
    painter.fill_circle(center=center, radius=38 * size, shade=solid(GRAY))
    painter.flat_circle(center=center, radius=20 * size, color=(210, 216, 230))


def draw_envelope(
    painter,
    center,
    width=180,
    height=124,
):
    box = (center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2)
    painter.fill_rounded_rect(box=box, radius=10, shade=solid((255, 240, 200)))
    painter.fill_polygon(points=[(box[0], box[1]), (box[2], box[1]), (center[0], center[1] + 8)], shade=solid((240, 206, 140)))


def draw_paper_plane(
    painter,
    center,
    size=1.0,
    rotation=0,
):
    def place(point):
        rotated = rotate_point(point=(center[0] + point[0] * size, center[1] + point[1] * size), center=center, angle_degrees=rotation)
        return rotated

    painter.fill_polygon(points=[place((90, 0)), place((-90, -52)), place((-40, 4))], shade=solid(WHITE))
    painter.fill_polygon(points=[place((90, 0)), place((-40, 4)), place((-20, 56))], shade=solid((210, 220, 240)))


def draw_clipboard(
    painter,
    center,
    width,
    height,
    row_count,
    checked_count,
):
    box = (center[0] - width / 2, center[1] - height / 2, center[0] + width / 2, center[1] + height / 2)
    painter.fill_rounded_rect(box=box, radius=16, shade=solid(BROWN))
    painter.fill_rounded_rect(box=(box[0] + 14, box[1] + 30, box[2] - 14, box[3] - 14), radius=8, shade=solid(WHITE))
    painter.fill_rounded_rect(box=(center[0] - 40, box[1] - 10, center[0] + 40, box[1] + 40), radius=12, shade=solid(GRAY))

    for row in range(row_count):
        y = box[1] + 80 + row * (height - 120) / max(row_count - 1, 1)
        painter.flat_stroke(start=(box[0] + 90, y), end=(box[2] - 40, y), width=12, color=(150, 162, 190))

        if row < checked_count:
            draw_check_mark(painter=painter, center=(box[0] + 52, y), size=16, width=10)
        else:
            painter.fill_ring(center=(box[0] + 52, y), outer_radius=15, inner_radius=8, color=GRAY)


def draw_trophy(
    painter,
    center,
    size=1.0,
):
    for side in (-1, 1):
        handle = build_arc_points(center=(center[0] + side * 70 * size, center[1] - 30 * size), radius=30 * size, start_angle=-90, end_angle=90) if side == 1 else build_arc_points(center=(center[0] - 70 * size, center[1] - 30 * size), radius=30 * size, start_angle=90, end_angle=270)
        painter.flat_curve(points=handle, width=12 * size, color=GOLD)

    painter.fill_polygon(
        points=[
            (center[0] - 76 * size, center[1] - 90 * size),
            (center[0] + 76 * size, center[1] - 90 * size),
            (center[0] + 50 * size, center[1] + 30 * size),
            (center[0] - 50 * size, center[1] + 30 * size),
        ],
        shade=solid(GOLD),
    )
    painter.fill_stroke(start=(center[0], center[1] + 20 * size), end=(center[0], center[1] + 70 * size), width=22 * size, shade=solid(GOLD))
    painter.fill_rounded_rect(
        box=(center[0] - 56 * size, center[1] + 66 * size, center[0] + 56 * size, center[1] + 96 * size),
        radius=8 * size,
        shade=solid(BROWN),
    )
    draw_star(painter=painter, center=(center[0], center[1] - 36 * size), size=28 * size, color=WHITE)


def draw_gear(
    painter,
    center,
    size=1.0,
    color=GRAY,
):
    for angle in range(0, 360, 45):
        painter.fill_stroke(
            start=move_point(point=center, angle=angle, distance=40 * size),
            end=move_point(point=center, angle=angle, distance=62 * size),
            width=26 * size,
            shade=solid(color),
        )

    painter.fill_ring(center=center, outer_radius=52 * size, inner_radius=20 * size, color=color)


def draw_hammer(
    painter,
    center,
    size=1.0,
    angle=-45,
):
    """The head is at `center`, the handle points to `angle` (0 right, 90 down)."""
    handle_end = move_point(point=center, angle=angle, distance=170 * size)
    painter.fill_stroke(start=center, end=handle_end, width=24 * size, shade=solid(BROWN))
    painter.fill_ellipse(center=center, radius_x=64 * size, radius_y=28 * size, shade=solid(DARK_GRAY), angle=angle + 90)


def draw_chest(
    painter,
    center,
    size=1.0,
):
    painter.fill_rounded_rect(
        box=(center[0] - 100 * size, center[1] - 10 * size, center[0] + 100 * size, center[1] + 80 * size),
        radius=10 * size,
        shade=solid(BROWN),
    )
    lid_top = build_arc_points(center=(center[0], center[1] - 10 * size), radius=100 * size, start_angle=180, end_angle=360)
    painter.fill_polygon(points=[(x, (y - (center[1] - 10 * size)) * 0.55 + (center[1] - 10 * size)) for x, y in lid_top], shade=solid((184, 116, 66)))
    painter.fill_rounded_rect(
        box=(center[0] - 18 * size, center[1] - 20 * size, center[0] + 18 * size, center[1] + 36 * size),
        radius=6 * size,
        shade=solid(GOLD),
    )


def draw_vase(
    painter,
    center,
    size=1.0,
    color=(90, 180, 210),
):
    painter.fill_ellipse(center=center, radius_x=64 * size, radius_y=84 * size, shade=solid(color))
    painter.fill_rounded_rect(
        box=(center[0] - 28 * size, center[1] - 130 * size, center[0] + 28 * size, center[1] - 40 * size),
        radius=10 * size,
        shade=solid(color),
    )
    painter.fill_ellipse(center=(center[0], center[1] - 130 * size), radius_x=40 * size, radius_y=12 * size, shade=solid(color))


def draw_balloon(
    painter,
    center,
    radius=60,
    color=RED,
    string_end=None,
):
    if string_end is not None:
        knot = (center[0], center[1] + radius * 1.25)
        string = sample_curve(start=knot, first_control=(knot[0] + 20, knot[1] + 50), second_control=(string_end[0] - 20, string_end[1] - 50), end=string_end)
        painter.flat_curve(points=string, width=5, color=DARK_GRAY)

    painter.fill_polygon(
        points=[(center[0] - 12, center[1] + radius * 1.3), (center[0] + 12, center[1] + radius * 1.3), (center[0], center[1] + radius * 0.9)],
        shade=solid(color),
    )
    painter.fill_ellipse(center=center, radius_x=radius, radius_y=radius * 1.12, shade=solid(color))
    painter.flat_ellipse(center=(center[0] - radius * 0.4, center[1] - radius * 0.4), radius_x=9, radius_y=16, color=WHITE, angle=30)


def draw_car_cabin(
    painter,
    center,
):
    """The glass part of the car. Draw the character after it and the car body after the character."""
    painter.fill_polygon(
        points=[(center[0] - 130, center[1] - 70), (center[0] - 84, center[1] - 190), (center[0] + 96, center[1] - 190), (center[0] + 150, center[1] - 70)],
        shade=solid((190, 226, 252)),
    )


def draw_car_body(
    painter,
    center,
):
    painter.fill_rounded_rect(
        box=(center[0] - 230, center[1] - 80, center[0] + 230, center[1] + 66),
        radius=44,
        shade=solid(RED),
    )
    painter.flat_ellipse(center=(center[0] + 214, center[1] - 28), radius_x=16, radius_y=24, color=YELLOW)

    for side in (-1, 1):
        painter.fill_circle(center=(center[0] + side * 132, center[1] + 66), radius=58, shade=solid((54, 60, 78)))
        painter.flat_circle(center=(center[0] + side * 132, center[1] + 66), radius=24, color=GRAY)


def draw_clock(
    painter,
    center,
    size=1.0,
):
    painter.fill_circle(center=center, radius=60 * size, shade=solid(WHITE))
    painter.fill_ring(center=center, outer_radius=60 * size, inner_radius=47 * size, color=ORANGE)
    painter.flat_stroke(start=center, end=(center[0], center[1] - 34 * size), width=8 * size, color=DARK_GRAY)
    painter.flat_stroke(start=center, end=(center[0] - 24 * size, center[1] + 12 * size), width=8 * size, color=DARK_GRAY)
    painter.flat_circle(center=center, radius=7 * size, color=DARK_GRAY)


def draw_pin(
    painter,
    center,
    size=1.0,
    color=RED,
):
    painter.fill_polygon(
        points=[(center[0] - 44 * size, center[1] + 20 * size), (center[0] + 44 * size, center[1] + 20 * size), (center[0], center[1] + 110 * size)],
        shade=solid(color),
    )
    painter.fill_circle(center=center, radius=56 * size, shade=solid(color))
    painter.flat_circle(center=center, radius=22 * size, color=WHITE)


def draw_medal(
    painter,
    neck,
    medal_center,
    size=1.0,
):
    """The ribbon starts at the neck on both sides and runs down to the medal."""
    length = math.hypot(medal_center[0] - neck[0], medal_center[1] - neck[1])
    down = ((medal_center[0] - neck[0]) / length, (medal_center[1] - neck[1]) / length)
    sideways = (-down[1], down[0])

    for side in (-1, 1):
        ribbon_start = (neck[0] + sideways[0] * side * 34 * size, neck[1] + sideways[1] * side * 34 * size)
        painter.fill_stroke(start=ribbon_start, end=medal_center, width=20 * size, shade=solid(RED))

    draw_coin(painter=painter, center=(medal_center[0] + down[0] * 20 * size, medal_center[1] + down[1] * 20 * size), radius=38 * size)


# (offset x, offset y, radius x, radius y) of the ellipses that form the outline of an ice patch
ICE_PATCH_BLOBS = ((0, 0, 230, 52), (-125, 6, 110, 38), (135, -4, 120, 40), (20, 14, 170, 44))
ICE_SHINE_STROKES = ((-120, -14, -70, -26), (-30, 10, 40, -8), (90, -16, 140, -28))    # (x1, y1, x2, y2)


def draw_ice_patch(
    painter,
    center,
    size=1.0,
):
    """Black ice on the ground: a flat pale blue patch with shiny streaks and a few sparkles."""
    blob_masks = [
        painter.build_rotated_ellipse_mask(
            center=(center[0] + offset_x * size, center[1] + offset_y * size),
            radius_x=radius_x * size,
            radius_y=radius_y * size,
        )
        for offset_x, offset_y, radius_x, radius_y in ICE_PATCH_BLOBS
    ]
    ice_mask = painter.union_all(masks=blob_masks)
    painter.fill(mask=ice_mask, shade=solid(ICE))
    painter.fill_ellipse(center=(center[0], center[1] + 6 * size), radius_x=170 * size, radius_y=32 * size, shade=solid(ICE_LIGHT), clip=ice_mask)

    for x1, y1, x2, y2 in ICE_SHINE_STROKES:
        painter.flat_stroke(
            start=(center[0] + x1 * size, center[1] + y1 * size),
            end=(center[0] + x2 * size, center[1] + y2 * size),
            width=11 * size,
            color=WHITE,
        )

    draw_sparkle(painter=painter, center=(center[0] - 190 * size, center[1] - 40 * size), size=22 * size, color=ICE_SPARKLE)
    draw_sparkle(painter=painter, center=(center[0] + 175 * size, center[1] - 44 * size), size=18 * size, color=ICE_SPARKLE)
