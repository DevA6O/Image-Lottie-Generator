"""
Poses and showcase placement that several scripts use.
"""
from character.figure import Pose

STAND_HIP = (512, 620)
SHOWCASE_HIP = (512, 596)    # A full body that fills the canvas
SHOWCASE_SCALE = 1.45

CHEER_POSE = Pose(left_arm=(-150, 0), right_arm=(150, 0), eyes="happy", mouth="grin")
WALK_POSE = Pose(lean=6, head_tilt=3, left_arm=(-24, -14), right_arm=(26, 16), left_leg=(-24, 6), right_leg=(26, -14))
RUN_POSE = Pose(lean=18, head_tilt=6, left_arm=(-40, -100), right_arm=(40, 110), left_leg=(-35, -15), right_leg=(50, -80), mouth="grin")

# Both hands hang at the sides of something held in front of the belly (gift, book, box)
CARRY_LEFT_ARM = (-35, 55)
CARRY_RIGHT_ARM = (35, -55)
