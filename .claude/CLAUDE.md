# Project Guide

Generates images and Lottie animations (backend) and shows them in a dark-mode gallery (frontend).

## Project Layout

- `start.py` is the cross-platform launcher: sets up `_env` if needed, runs the backend, then the frontend opens in the browser.
- `backend/main.py` checks for changes, rebuilds outdated results and starts the frontend server.
- `backend/build.py` finds all categories automatically. Do not register files there.
- `backend/generators/` holds everything that generates images or Lottie files, one folder per category (e.g. `streak/`).
  Nothing else lives there: shared helpers are in `backend/painting/`.
- Categories with many images (`food/`, `verbs/`) keep one generator script per image in `gen/<theme>/` (e.g. `generators/food/gen/fruits/apple.py`).
  Helpers (painter, catalog, runner, `build_config.py`) stay directly in the category folder, never in `gen/`.
- `generators/character/` holds the characters: the shared body (`figure.py`), one subfolder per character (e.g. `milo/`) and their showcase images in `gen/<character>/`.
  Other categories (e.g. `verbs/`) import a character from there.
- `backend/painting/` holds the painters that several categories share. Import them as `from painting.flat_painter import ...`.
  The build sets `PYTHONPATH` to `backend/` and `backend/generators/` (so `food`, `verbs` ... are importable), and `pyrightconfig.json` tells the IDE the same.
- `backend/generators/<category>/build_config.py` registers every generated file of that category as a `BuildTarget`.
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

## Image Design

### Look of every image
- Flat icon style like the Magnific "Special Flat" icons: no outlines, no gradients, rounded simple shapes.
  One solid color per shape plus a darker crescent on the lower right. The painters do this in `fill_*`. Small details use `fill_flat` / `flat_*` (no crescent).
- Few details: one or two highlights or spots, no textures. Strong colors, but not harsh.
- 1024x1024, transparent background. Only the subject: no backdrop, no ground shadow, no scenery.
- Never write a word or letters into an image. Say it with symbols: question mark, exclamation mark, check mark, heart, star, clock, arrows, wind lines.
- Draw a shape once. A shape that two categories need goes into a helper file (e.g. `food/banana_shape.py`, `verbs/props.py`).

### Words without an object (verbs and similar)
- Words like "be", "go" or "why" are shown with a character (Milo) plus the symbols or props that carry the meaning.
  Examples: a question mark for "why", wind lines for speed, a lightbulb for an idea.
- The character and its prop or symbol are the foreground. Nothing else.
- Irregular verbs: the 50 most common English ones, three images each (infinitive, past, past participle).
  Files are `<verb>_<form>.png`, the gallery title looks like "Went (past)".
  - Infinitive: the action itself, just starting or going on.
  - Past: the same action at a moment in the past. It always has the orange clock. Faded copies of the character can show that it is over.
  - Past participle: the result after the action (check mark, star, heart, a finished object).
  - The three forms must differ in scene, pose or props. A different color alone is never enough.
- Build verbs in small batches (about 10) and review them before the next batch. A verb is built when its key is in `BUILT_VERB_KEYS` in `verb_catalog.py`.

### Characters
- A character is a `Look` (colors and hair shape) on the shared `Figure` body in `generators/character/`.
  A new character gets a name, its own subfolder and showcase images in `gen/<name>/`.
- Milo is a clean-shaven young man with a high, swept quiff. No beard.
- Arms stay straight unless the pose needs a bend (for example hands on hips). Raised arms point to the side, never along the head, so they stay visible.
- Props and symbols never touch or cover the head, hair or face. Worn things (medal, scarf) are painted under the arms with `before_arms`.
- Before an image counts as done, look at it enlarged: every arm is visible, no arm is kinked, nothing sits inside the character, and the meaning is clear at first glance.

### When an object does not read
- If an object still looks wrong after two tries, stop redrawing it. Compare a few variants in a preview outside the project,
  or replace it with a simpler symbol that says the same (black ice instead of a banana peel), or ask what the user has in mind.

## Working Rules

- Tests: new tests go in a `tests/` folder. If there is none, ask before creating it.
- Generated outputs are rebuilt through `python backend/main.py` (or `start.py`), not by copying files around.
- After code changes in `backend/`, run `python typecheck.py` and fix every error it reports.
- When a generator script changes, check that it still builds. A change to a shared script (e.g. `streak_flame.py`) can affect other outputs.
