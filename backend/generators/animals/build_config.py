from build_target import BuildTarget

CATEGORY_TITLE = "Animals"

# Helper files of this category and the shared painter. A change in one of them rebuilds every image.
PAINTER_SOURCES = ("animal_painter.py", "face_parts.py", "../../painting/layer_painter.py", "../../painting/flat_painter.py")

# Shape helpers that only some images use: helper file -> the images that draw it
SHAPE_USERS = {
    "bird_shape.py": ("budgerigar", "chicken", "blackbird", "sparrow", "tit", "pigeon", "raven", "crow", "magpie", "parrot", "woodpecker", "seagull"),
    "quadruped_shape.py": (
        "dog", "cat", "guinea_pig", "cow", "pig", "goat", "fox", "badger", "wolf", "lynx", "beaver", "mouse", "wild_boar",
        "deer", "red_deer", "horse", "donkey", "zebra", "lion", "tiger", "leopard", "cheetah",
        "bear", "polar_bear", "panda", "gorilla", "rhino", "hippo", "giraffe",
    ),
    "deer_shape.py": ("deer", "red_deer"),
    "horse_shape.py": ("horse", "donkey", "zebra"),
    "big_cat_shape.py": ("lion", "tiger", "leopard", "cheetah"),
    "bear_shape.py": ("bear", "polar_bear", "panda", "gorilla"),
    "rabbit_shape.py": ("rabbit", "hare"),
    "frog_shape.py": ("frog", "toad"),
}

# folder: [(title, name)]. The script is gen/<folder>/<name>.py and the output is <name>.png
IMAGE_FOLDERS = {
    "pets": [
        ("Dog", "dog"),
        ("Cat", "cat"),
        ("Rabbit", "rabbit"),
        ("Guinea Pig", "guinea_pig"),
        ("Hamster", "hamster"),
        ("Budgerigar", "budgerigar"),
        ("Goldfish", "goldfish"),
        ("Turtle", "turtle"),
    ],
    "farm": [
        ("Cow", "cow"),
        ("Pig", "pig"),
        ("Horse", "horse"),
        ("Sheep", "sheep"),
        ("Goat", "goat"),
        ("Chicken", "chicken"),
        ("Duck", "duck"),
        ("Goose", "goose"),
        ("Donkey", "donkey"),
        ("Turkey", "turkey"),
    ],
    "wild": [
        ("Roe Deer", "deer"),
        ("Red Deer", "red_deer"),
        ("Wild Boar", "wild_boar"),
        ("Fox", "fox"),
        ("Hare", "hare"),
        ("Squirrel", "squirrel"),
        ("Hedgehog", "hedgehog"),
        ("Badger", "badger"),
        ("Wolf", "wolf"),
        ("Lynx", "lynx"),
        ("Beaver", "beaver"),
        ("Mouse", "mouse"),
        ("Bat", "bat"),
    ],
    "birds": [
        ("Blackbird", "blackbird"),
        ("Sparrow", "sparrow"),
        ("Tit", "tit"),
        ("Pigeon", "pigeon"),
        ("Raven", "raven"),
        ("Crow", "crow"),
        ("Magpie", "magpie"),
        ("Stork", "stork"),
        ("Eagle", "eagle"),
        ("Owl", "owl"),
        ("Woodpecker", "woodpecker"),
        ("Swan", "swan"),
        ("Seagull", "seagull"),
        ("Parrot", "parrot"),
        ("Penguin", "penguin"),
        ("Ostrich", "ostrich"),
    ],
    "zoo": [
        ("Lion", "lion"),
        ("Tiger", "tiger"),
        ("Elephant", "elephant"),
        ("Giraffe", "giraffe"),
        ("Zebra", "zebra"),
        ("Rhino", "rhino"),
        ("Hippo", "hippo"),
        ("Monkey", "monkey"),
        ("Gorilla", "gorilla"),
        ("Kangaroo", "kangaroo"),
        ("Koala", "koala"),
        ("Bear", "bear"),
        ("Polar Bear", "polar_bear"),
        ("Panda", "panda"),
        ("Camel", "camel"),
        ("Crocodile", "crocodile"),
        ("Leopard", "leopard"),
        ("Cheetah", "cheetah"),
    ],
    "sea": [
        ("Whale", "whale"),
        ("Dolphin", "dolphin"),
        ("Shark", "shark"),
        ("Seal", "seal"),
        ("Harbor Seal", "harbor_seal"),
        ("Octopus", "octopus"),
        ("Jellyfish", "jellyfish"),
        ("Crab", "crab"),
        ("Lobster", "lobster"),
        ("Starfish", "starfish"),
    ],
    "reptiles": [
        ("Snake", "snake"),
        ("Lizard", "lizard"),
        ("Frog", "frog"),
        ("Toad", "toad"),
        ("Chameleon", "chameleon"),
        ("Iguana", "iguana"),
    ],
    "insects": [
        ("Bee", "bee"),
        ("Wasp", "wasp"),
        ("Ant", "ant"),
        ("Butterfly", "butterfly"),
        ("Ladybug", "ladybug"),
        ("Fly", "fly"),
        ("Mosquito", "mosquito"),
        ("Spider", "spider"),
        ("Snail", "snail"),
        ("Earthworm", "earthworm"),
        ("Grasshopper", "grasshopper"),
    ],
}


def find_shape_sources(name):
    return tuple(source for source, users in SHAPE_USERS.items() if name in users)


BUILD_TARGETS = [
    BuildTarget(
        title=title,
        kind="image",
        script=f"gen/{folder}/{name}.py",
        output=f"{name}.png",
        extra_sources=PAINTER_SOURCES + find_shape_sources(name=name),
    )
    for folder, items in IMAGE_FOLDERS.items()
    for title, name in items
]
