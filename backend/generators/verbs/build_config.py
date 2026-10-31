from build_target import BuildTarget
from verbs.verb_catalog import FORM_FILE_NAMES, build_image_name, build_image_title, find_built_verbs

CATEGORY_TITLE = "Irregular Verbs"

# Helper files of this category and the shared painter. A change in one of them rebuilds every image.
SHARED_SOURCES = (
    "verb_painter.py",
    "partner.py",
    "props.py",
    "tense.py",
    "verb_catalog.py",
    "render_verb.py",
    "../character/figure.py",
    "../character/poses.py",
    "../character/milo/milo.py",
    "../../painting/layer_painter.py",
    "../../painting/flat_painter.py",
)


def build_verb_targets():
    targets = []

    for verb in find_built_verbs():
        for form in range(len(FORM_FILE_NAMES)):
            targets.append(
                BuildTarget(
                    title=build_image_title(verb=verb, form=form),
                    kind="image",
                    script=verb.script,
                    output=build_image_name(verb=verb, form=form),
                    extra_sources=SHARED_SOURCES,
                    arguments=(str(form),),
                )
            )

    return targets


BUILD_TARGETS = build_verb_targets()
