from build_target import BuildTarget

CATEGORY_TITLE = "Streak"

BUILD_TARGETS = [
    BuildTarget(
        title="Streak Flame",
        kind="image",
        script="streak_flame.py",
        output="streak_flame.png",
    ),
    BuildTarget(
        title="Streak Flame",
        kind="lottie",
        script="flame_lottie.py",
        output="streak_flame.json",
        extra_sources=("streak_flame.py",),
    ),
]
