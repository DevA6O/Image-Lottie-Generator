"""
Half star as a Lottie animation. Output: half_star.json in frontend/results/rating
"""
from star_animation import HALF_STAR_SPEC, save_animation

if __name__ == "__main__":
    save_animation(spec=HALF_STAR_SPEC, title="Half Star", file_name="half_star.json")
