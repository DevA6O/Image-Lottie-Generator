"""
The shared part of every verb script. A verb script draws its scene and then calls
render_verb_from_command_line, which reads the form number from the command line
(0 = infinitive, 1 = past, 2 = past participle) and writes <verb>_<form>.png to frontend/results/verbs.
"""
import sys

from verbs.verb_catalog import IRREGULAR_VERBS, build_image_name
from verbs.verb_painter import VerbPainter


def find_verb(verb_key):
    return next(verb for verb in IRREGULAR_VERBS if verb.key == verb_key)


def render_verb_form(
    verb_key,
    paint_scene,
    form,
):
    verb = find_verb(verb_key=verb_key)
    painter = VerbPainter()

    paint_scene(painter, form)
    painter.save_verb_image(file_name=build_image_name(verb=verb, form=form))


def render_verb_from_command_line(
    verb_key,
    paint_scene,
):
    render_verb_form(verb_key=verb_key, paint_scene=paint_scene, form=int(sys.argv[1]))
