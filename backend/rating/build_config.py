from build_target import BuildTarget

CATEGORY_TITLE = "Rating"

IMAGE_SOURCES = ("star_image.py", "star_shape.py")
ANIMATION_SOURCES = ("star_animation.py", "star_shape.py")

BUILD_TARGETS = [
    BuildTarget(title="Full Star", kind="image", script="full_star.py", output="full_star.png",
                extra_sources=IMAGE_SOURCES),
    BuildTarget(title="Half Star", kind="image", script="half_star.py", output="half_star.png",
                extra_sources=IMAGE_SOURCES),
    BuildTarget(title="Full Star", kind="lottie", script="full_star_lottie.py", output="full_star.json",
                extra_sources=ANIMATION_SOURCES),
    BuildTarget(title="Half Star", kind="lottie", script="half_star_lottie.py", output="half_star.json",
                extra_sources=ANIMATION_SOURCES),
]
