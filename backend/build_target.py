from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BACKEND_DIR.parent / "frontend" / "results"


@dataclass(frozen=True)
class BuildTarget:
    """One generated file. Defined in backend/<category>/build_config.py."""

    title: str
    kind: str                  # "image" or "lottie"
    script: str                # Script in the category folder that writes the output
    output: str                # File name in frontend/results/<category>/
    extra_sources: tuple = ()  # Imported modules that also trigger a rebuild when they change
    arguments: tuple = ()      # Command line arguments for the script, so one script can write many outputs
    category: str = ""         # Set automatically from the folder name

    @property
    def state_key(self):
        return f"{self.category}/{self.output}"

    @property
    def script_path(self):
        return BACKEND_DIR / self.category / self.script

    @property
    def output_path(self):
        return RESULTS_DIR / self.category / self.output

    @property
    def frontend_path(self):
        return f"results/{self.category}/{self.output}"

    def hash_sources(self):
        digest = sha256()

        for source in (self.script, *self.extra_sources):
            digest.update((BACKEND_DIR / self.category / source).read_bytes())

        return digest.hexdigest()
