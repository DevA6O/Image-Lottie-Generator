"""
Pig image, drawn from scratch: full body from the side.
Output: pig.png (1024x1024, transparent background) in frontend/results/animals
"""
from animals.animal_painter import AnimalPainter
from animals.face_parts import EYE, NOSE
from animals.quadruped_shape import EYE_HIGHLIGHT, QuadrupedSpec, paint_legs, paint_pointed_ear, paint_torso

SKIN = (248, 170, 184)
SKIN_FAR = (214, 134, 150)
HOOF = (186, 106, 126)
SNOUT = (252, 198, 208)
NOSTRIL = (190, 96, 120)

SPEC = QuadrupedSpec(
    coat=SKIN,
    far_coat=SKIN_FAR,
    foot=HOOF,
    muzzle=SNOUT,
    body_center=(610, 620),
    body_rx=310,
    body_ry=195,
    leg_width=70,
    foot_rx=46,
)


def paint_head(painter):
    painter.blob(center=(300, 580), radius_x=150, radius_y=135, color=SKIN)
    painter.blob(center=(170, 610), radius_x=62, radius_y=82, color=SNOUT)
    painter.spot(center=(158, 590), radius_x=11, radius_y=24, color=NOSTRIL)
    painter.spot(center=(188, 590), radius_x=11, radius_y=24, color=NOSTRIL)
    painter.spot(center=(280, 520), radius_x=17, radius_y=17, color=EYE)
    painter.spot(center=(274, 513), radius_x=5, radius_y=5, color=EYE_HIGHLIGHT)


def paint_curly_tail(painter):
    painter.arc_line(center=(930, 560), radius=45, start_angle=-30, end_angle=250, width=18, color=SKIN_FAR)


def render_pig_image():
    painter = AnimalPainter()
    paint_legs(painter=painter, spec=SPEC)
    paint_curly_tail(painter=painter)
    paint_torso(painter=painter, spec=SPEC)
    paint_pointed_ear(painter=painter, base=(340, 470), tip=(410, 380), width=100, color=SKIN_FAR)
    paint_head(painter=painter)
    paint_pointed_ear(painter=painter, base=(290, 470), tip=(330, 350), width=105, color=SKIN, inner_color=SNOUT)
    painter.save_image(name="pig")


if __name__ == "__main__":
    render_pig_image()
