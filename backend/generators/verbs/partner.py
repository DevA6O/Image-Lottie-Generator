"""
The second person in verb scenes with two people: Milo with a purple shirt and dark hair.
"""
from character.milo.milo import Milo

PARTNER_SHIRT = (190, 120, 220)
PARTNER_HAIR = (50, 50, 64)


def build_partner(
    hip,
    scale=1.0,
):
    return Milo(hip=hip, scale=scale, shirt=PARTNER_SHIRT, hair=PARTNER_HAIR)
