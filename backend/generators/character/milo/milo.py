"""
Milo: a clean-shaven young man with a high, swept quiff and a blue shirt.
"""
from dataclasses import replace

from character.figure import Figure, Look

# Hair shape in head coordinates (the head has radius 80). Every curve is (start, control, control, end).
MILO_HAIR_OUTLINE = (
    ((-78, -4), (-92, -30), (-92, -70), (-62, -92)),
    ((-62, -92), (-48, -122), (-10, -132), (36, -126)),
    ((36, -126), (74, -122), (94, -100), (86, -62)),
    ((86, -62), (84, -46), (80, -36), (74, -26)),
    ((74, -26), (56, -56), (24, -60), (-8, -48)),
    ((-8, -48), (-34, -40), (-56, -30), (-78, -4)),
)
MILO_HAIR_STRANDS = (
    ((-44, -88), (-24, -112), (14, -118), (50, -108)),
    ((-60, -64), (-48, -80), (-30, -88), (-10, -90)),
)

MILO_LOOK = Look(
    skin=(250, 205, 160),
    hair=(96, 60, 42),
    shirt=(78, 140, 230),
    pants=(70, 84, 130),
    shoe=(60, 52, 70),
    hair_outline=MILO_HAIR_OUTLINE,
    hair_strands=MILO_HAIR_STRANDS,
)


class Milo(Figure):
    """shirt and hair can be changed, for example to show a second person next to Milo."""

    def __init__(
        self,
        hip=(512, 600),
        scale=1.0,
        shirt=None,
        hair=None,
        fade=0.0,
    ):
        look = replace(MILO_LOOK, shirt=shirt or MILO_LOOK.shirt, hair=hair or MILO_LOOK.hair)
        super().__init__(look=look, hip=hip, scale=scale, fade=fade)
