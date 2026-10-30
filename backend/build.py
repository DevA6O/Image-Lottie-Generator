"""
Build check: renders images and Lottie JSONs again when their source scripts changed
(or the output file is missing) and writes the manifest for the gallery.

Every category folder in backend/ describes its files in its own build_config.py.
To add a new category: create the folder and add a build_config.py. Nothing changes here.
"""
import importlib.util
import json
import os
import subprocess
import sys
from dataclasses import dataclass, replace

from build_target import BACKEND_DIR, RESULTS_DIR

BUILD_STATE_FILE = BACKEND_DIR / ".build_state.json"
MANIFEST_FILE = RESULTS_DIR / "manifest.json"
BUILD_CONFIG_FILE_NAME = "build_config.py"


@dataclass(frozen=True)
class BuildCategory:
    name: str
    title: str
    targets: tuple


def load_build_category(category_dir):
    config_path = category_dir / BUILD_CONFIG_FILE_NAME
    spec = importlib.util.spec_from_file_location(f"{category_dir.name}_build_config", config_path)

    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {config_path}")

    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)

    return BuildCategory(
        name=category_dir.name,
        title=config.CATEGORY_TITLE,
        targets=tuple(replace(target, category=category_dir.name) for target in config.BUILD_TARGETS),
    )


def discover_build_categories():
    category_dirs = sorted(
        path for path in BACKEND_DIR.iterdir()
        if (path / BUILD_CONFIG_FILE_NAME).exists()
    )

    return [load_build_category(category_dir=category_dir) for category_dir in category_dirs]


class ResultBuilder:
    def __init__(self, categories):
        self._categories = categories

    def rebuild_outdated_results(self, force_all=False):
        build_state = self._load_build_state()

        for category in self._categories:
            for target in category.targets:
                build_state = self._rebuild_if_outdated(
                    target=target,
                    build_state=build_state,
                    force=force_all,
                )

        return self._write_manifest()

    def _rebuild_if_outdated(
        self,
        target,
        build_state,
        force,
    ):
        source_hash = target.hash_sources()
        is_up_to_date = target.output_path.exists() and build_state.get(target.state_key) == source_hash

        if is_up_to_date and not force:
            print(f"[up to date]  {target.state_key}")
            return build_state

        print(f"[rebuild]     {target.state_key}")
        subprocess.run(
            [sys.executable, str(target.script_path), *target.arguments],
            env=self._build_script_environment(),
            check=True,
        )

        build_state[target.state_key] = source_hash
        self._save_build_state(build_state=build_state)

        return build_state

    def _build_script_environment(self):
        """The scripts import the shared packages (painting, food, verbs) from the backend folder."""
        search_path = os.pathsep.join(filter(None, [str(BACKEND_DIR), os.environ.get("PYTHONPATH")]))

        return {**os.environ, "PYTHONPATH": search_path}

    def _load_build_state(self):
        try:
            return json.loads(BUILD_STATE_FILE.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}

    def _save_build_state(self, build_state):
        BUILD_STATE_FILE.write_text(json.dumps(build_state, indent=2), encoding="utf-8")

    def _write_manifest(self):
        manifest_categories = [
            self._build_manifest_category(category=category)
            for category in self._categories
        ]
        manifest = {"categories": [category for category in manifest_categories if category["items"]]}

        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        MANIFEST_FILE.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

        return manifest

    def _build_manifest_category(self, category):
        return {
            "id": category.name,
            "title": category.title,
            "items": [
                {"title": target.title, "kind": target.kind, "file": target.frontend_path}
                for target in category.targets
                if target.output_path.exists()
            ],
        }


def rebuild_outdated_results(force_all=False):
    return ResultBuilder(categories=discover_build_categories()).rebuild_outdated_results(force_all=force_all)
