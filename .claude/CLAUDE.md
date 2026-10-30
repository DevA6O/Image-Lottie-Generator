# Project Guide

Generates images and Lottie animations (backend) and shows them in a dark-mode gallery (frontend).

## Project Layout

- `start.py` is the cross-platform launcher: sets up `_env` if needed, runs the backend, then the frontend opens in the browser.
- `backend/main.py` checks for changes, rebuilds outdated results and starts the frontend server.
- `backend/build.py` finds all categories automatically. Do not register files there.
- `backend/<category>/` contains the generator scripts of one category (e.g. `streak/`).
- Categories with many images (`food/`, `verbs/`) keep one generator script per image in `gen/<theme>/` (e.g. `food/gen/fruits/apple.py`, `verbs/gen/motion/go.py`).
  Helpers (painter, catalog, runner, `build_config.py`) stay directly in the category folder, never in `gen/`.
- `backend/painting/` holds the painters that several categories share. Import them as `from painting.flat_painter import ...`.
  The build sets `PYTHONPATH` to `backend/`, and `pyrightconfig.json` tells the IDE the same.
- `backend/<category>/build_config.py` registers every generated file of that category as a `BuildTarget`.
- `frontend/results/<category>/` contains the generated files and the `manifest.json`. Never edit these by hand.
- `frontend/` is plain HTML, CSS and JS. No framework, no build step, libraries live in `frontend/vendor/`.
- Python environment: `_env`. Dependencies go into `requirements.txt` (ask before adding a new one).

## Code Style

### Clean code first
- Keep it simple. If there is an easier way, use the easier way.
- The code must be understandable at first glance, without long thinking.
- Split code into small functions. One function does one job.
- Separate logical blocks with a blank line.
- Replace magic numbers with named constants.

### Language
- English everywhere: code, names, comments, docstrings, UI text, log messages, docs.

### Naming
- No generic names like `process`, `handle`, `run`, `do_work`, `data`, `result`, `helper`, `utils`, `tmp`.
  The name must say what the thing does or is: `render_flame_layers`, `build_manifest`, `drop_trajectory`.
- Write names out in full: `index` instead of `i`, `frame` instead of `f`.
  Only short math names (`x`, `y`, `t`) are fine inside real math formulas.
- Functions are verbs, classes and variables are nouns.

### Structure
- Use OOP when several functions share state or belong to one concept (e.g. a flame layer, a drop).
  Simple helpers stay plain functions. Do not force a class.
- Python: private helpers start with `_`.
  Order a file bottom-up: helpers first, the function that calls them below, the main entry point at the very bottom.
- JS: main function first, then the helpers in the order they are called.

### Formatting
- A function with 2 or more parameters puts each parameter on its own line.
- A call with 2 or more arguments uses keyword arguments (Python), each on its own line.
  Never pass several arguments positionally.
- Do not shorten code with clever one-liners if a clear version needs only a few more lines.

### Comments
- Comment only what the code cannot say: the why, a non-obvious rule, a trap.
- Never repeat what the code already says.
- Keep them short (1-2 lines) and in simple, plain English.
  Simple and a bit redundant is better than short and hard to read.

## Working Rules

- Tests: new tests go in a `tests/` folder. If there is none, ask before creating it.
- Generated outputs are rebuilt through `python backend/main.py` (or `start.py`), not by copying files around.
- After code changes in `backend/`, run `python typecheck.py` and fix every error it reports.
- When a generator script changes, check that it still builds. A change to a shared script (e.g. `streak_flame.py`) can affect other outputs.
