from build_target import BuildTarget

CATEGORY_TITLE = "Food"

# Helper files of this category and the shared painter. A change in one of them rebuilds every image.
PAINTER_SOURCES = ("food_painter.py", "../painting/layer_painter.py", "../painting/flat_painter.py")

# folder: [(title, name)]. The script is gen/<folder>/<name>.py and the output is <name>.png
IMAGE_FOLDERS = {
    "bakery": [
        ("Bread", "bread"),
        ("Toast", "toast"),
        ("Croissant", "croissant"),
        ("Baguette", "baguette"),
        ("Pretzel", "pretzel"),
        ("Donut", "donut"),
        ("Cookie", "cookie"),
        ("Cupcake", "cupcake"),
        ("Cake Slice", "cake_slice"),
        ("Pancakes", "pancakes"),
    ],
    "dairy_and_eggs": [
        ("Cheese", "cheese"),
        ("Butter", "butter"),
        ("Egg", "egg"),
        ("Fried Egg", "fried_egg"),
    ],
    "fast_food": [
        ("Pizza", "pizza"),
        ("Burger", "burger"),
        ("Hot Dog", "hot_dog"),
        ("Fries", "fries"),
        ("Taco", "taco"),
        ("Sandwich", "sandwich"),
        ("Popcorn", "popcorn"),
    ],
    "meat": [
        ("Bacon", "bacon"),
        ("Sausage", "sausage"),
        ("Drumstick", "drumstick"),
    ],
    "fruits": [
        ("Apple", "apple"),
        ("Banana", "banana"),
        ("Orange", "orange"),
        ("Strawberry", "strawberry"),
        ("Cherries", "cherries"),
        ("Grapes", "grapes"),
        ("Watermelon", "watermelon"),
        ("Lemon", "lemon"),
        ("Pear", "pear"),
        ("Pineapple", "pineapple"),
        ("Avocado", "avocado"),
    ],
    "vegetables": [
        ("Tomato", "tomato"),
        ("Carrot", "carrot"),
        ("Broccoli", "broccoli"),
        ("Corn", "corn"),
        ("Eggplant", "eggplant"),
        ("Mushroom", "mushroom"),
        ("Bell Pepper", "bell_pepper"),
        ("Onion", "onion"),
        ("Potato", "potato"),
        ("Garlic", "garlic"),
        ("Cucumber", "cucumber"),
        ("Olives", "olives"),
        ("Peanut", "peanut"),
    ],
    "sweets": [
        ("Chocolate", "chocolate"),
        ("Ice Cream", "ice_cream"),
        ("Honey", "honey"),
    ],
    "drinks": [
        ("Milk", "milk"),
        ("Coffee", "coffee"),
        ("Soda", "soda"),
    ],
}

BUILD_TARGETS = [
    BuildTarget(
        title=title,
        kind="image",
        script=f"gen/{folder}/{name}.py",
        output=f"{name}.png",
        extra_sources=PAINTER_SOURCES,
    )
    for folder, items in IMAGE_FOLDERS.items()
    for title, name in items
]
