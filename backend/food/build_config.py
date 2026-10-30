from build_target import BuildTarget

CATEGORY_TITLE = "Food"

PAINTER_SOURCES = ("layer_painter.py", "food_painter.py")

# (title, name): the script is <name>.py and the output is <name>.png
IMAGE_ITEMS = [
    ("Bread", "bread"),
    ("Cheese", "cheese"),
    ("Butter", "butter"),
    ("Pizza", "pizza"),
    ("Toast", "toast"),
    ("Olives", "olives"),
    ("Croissant", "croissant"),
    ("Baguette", "baguette"),
    ("Pretzel", "pretzel"),
    ("Donut", "donut"),
    ("Cookie", "cookie"),
    ("Cupcake", "cupcake"),
    ("Cake Slice", "cake_slice"),
    ("Pancakes", "pancakes"),
    ("Fried Egg", "fried_egg"),
    ("Egg", "egg"),
    ("Bacon", "bacon"),
    ("Sausage", "sausage"),
    ("Drumstick", "drumstick"),
    ("Burger", "burger"),
    ("Hot Dog", "hot_dog"),
    ("Fries", "fries"),
    ("Taco", "taco"),
    ("Sandwich", "sandwich"),
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
    ("Tomato", "tomato"),
    ("Carrot", "carrot"),
    ("Broccoli", "broccoli"),
    ("Corn", "corn"),
    ("Eggplant", "eggplant"),
    ("Mushroom", "mushroom"),
    ("Avocado", "avocado"),
    ("Bell Pepper", "bell_pepper"),
    ("Onion", "onion"),
    ("Potato", "potato"),
    ("Garlic", "garlic"),
    ("Cucumber", "cucumber"),
    ("Peanut", "peanut"),
    ("Popcorn", "popcorn"),
    ("Chocolate", "chocolate"),
    ("Ice Cream", "ice_cream"),
    ("Honey", "honey"),
    ("Milk", "milk"),
    ("Coffee", "coffee"),
    ("Soda", "soda"),
]

BUILD_TARGETS = [
    BuildTarget(
        title=title,
        kind="image",
        script=f"{name}.py",
        output=f"{name}.png",
        extra_sources=PAINTER_SOURCES,
    )
    for title, name in IMAGE_ITEMS
]
