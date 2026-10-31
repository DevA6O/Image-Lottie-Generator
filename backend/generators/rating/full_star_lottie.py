"""
Full star as a Lottie animation. Output: full_star.json in frontend/results/rating
"""
from star_animation import FULL_STAR_SPEC, save_animation

if __name__ == "__main__":
    save_animation(spec=FULL_STAR_SPEC, title="Full Star", file_name="full_star.json")
