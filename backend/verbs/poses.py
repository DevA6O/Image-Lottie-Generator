"""
Poses that more than one verb uses.
"""
from verbs.character import Pose

WALK_POSE = Pose(lean=6, head_tilt=3, left_arm=(-24, -14), right_arm=(26, 16), left_leg=(-24, 6), right_leg=(26, -14))
RUN_POSE = Pose(lean=18, head_tilt=6, left_arm=(-40, -100), right_arm=(40, 110), left_leg=(-35, -15), right_leg=(50, -80), mouth="grin")
