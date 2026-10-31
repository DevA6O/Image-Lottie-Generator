from build_target import BuildTarget

CATEGORY_TITLE = "Characters"

# Helper files of this category and the shared painter. A change in one of them rebuilds every image.
SHARED_SOURCES = ("character_painter.py", "figure.py", "poses.py", "milo/milo.py", "../../painting/layer_painter.py", "../../painting/flat_painter.py")

# character: [(title, name)]. The script is gen/<character>/<name>.py and the output is <character>_<name>.png
IMAGE_FOLDERS = {
    "milo": [
        ("Milo Standing", "standing"),
        ("Milo Waving", "waving"),
        ("Milo Walking", "walking"),
        ("Milo Running", "running"),
        ("Milo Cheering", "cheering"),
        ("Milo Thinking", "thinking"),
        ("Milo Surprised", "surprised"),
        ("Milo Portrait", "portrait"),
    ],
}

BUILD_TARGETS = [
    BuildTarget(
        title=title,
        kind="image",
        script=f"gen/{character}/{name}.py",
        output=f"{character}_{name}.png",
        extra_sources=SHARED_SOURCES,
    )
    for character, items in IMAGE_FOLDERS.items()
    for title, name in items
]
