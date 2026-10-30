"""
Renders one form of one verb. Usage: python render_verb.py <verb key> <form number>
Form numbers: 0 = infinitive, 1 = past, 2 = past participle.
Output: <verb>_<form>.png (1024x1024, transparent background) in frontend/results/verbs
"""
import importlib
import sys

from verb_catalog import IRREGULAR_VERBS, build_image_name
from verb_painter import VerbPainter


def find_verb(verb_key):
    return next(verb for verb in IRREGULAR_VERBS if verb.key == verb_key)


def render_verb_form(
    verb_key,
    form,
):
    verb = find_verb(verb_key=verb_key)
    scenes = importlib.import_module(verb.scene_module).SCENES
    painter = VerbPainter()

    scenes[verb.key](painter, form)
    painter.save_verb_image(file_name=build_image_name(verb=verb, form=form))


if __name__ == "__main__":
    render_verb_form(verb_key=sys.argv[1], form=int(sys.argv[2]))
