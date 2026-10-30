import sys
from pathlib import Path

from build_target import BuildTarget

sys.path.append(str(Path(__file__).resolve().parent))   # The build loads this file by path, so its folder is not importable yet

from verb_catalog import FORM_FILE_NAMES, build_image_name, build_image_title, find_built_verbs

CATEGORY_TITLE = "Irregular Verbs"

SHARED_SOURCES = ("verb_painter.py", "character.py", "props.py", "tense.py", "verb_catalog.py")


def build_verb_targets():
    targets = []

    for verb in find_built_verbs():
        for form in range(len(FORM_FILE_NAMES)):
            targets.append(
                BuildTarget(
                    title=build_image_title(verb=verb, form=form),
                    kind="image",
                    script="render_verb.py",
                    output=build_image_name(verb=verb, form=form),
                    extra_sources=(*SHARED_SOURCES, f"{verb.scene_module}.py"),
                    arguments=(verb.key, str(form)),
                )
            )

    return targets


BUILD_TARGETS = build_verb_targets()
