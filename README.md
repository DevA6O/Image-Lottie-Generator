# Images & Animations

Code that generates high-quality images for apps and websites, including Lottie animations.

**Goal:** Create our own images and animations, so we own the rights to them.

Everything is generated from scratch by code. No stock assets, no third-party artwork.

## Live gallery

See the "about" category of the repo

## How it works

- `backend/` holds the generator scripts, one folder per category (e.g. `streak/`).
- When started, the backend checks which scripts changed and rebuilds only the outdated images and Lottie JSONs.
- `frontend/` shows the results in a dark-mode gallery, grouped by category. Click an image or animation to view it larger.

## Quick start

Works on Windows, macOS and Linux (Python 3.9+):

```
python start.py
```

On the first run it creates the `_env` virtual environment and installs `requirements.txt`. Then it rebuilds what is outdated and opens the gallery in your browser. (On macOS/Linux use `python3 start.py` if `python` is not available.)

Options: `--force` (rebuild everything), `--port 8000`, `--no-browser`.

## Adding a new image or animation

1. Add a generator script to `backend/<category>/` (new folder for a new category). It writes to `frontend/results/<category>/`.
2. Register the file in `backend/<category>/build_config.py` as a `BuildTarget`. New categories need their own `build_config.py`.

`backend/build.py` finds all categories on its own, so it never needs to change.

Code style rules are in `.claude/CLAUDE.md`.
