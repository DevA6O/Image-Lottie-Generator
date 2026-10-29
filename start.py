"""
Cross-platform launcher (Windows, macOS, Linux).
Sets up the _env virtual environment on first run, installs the requirements,
then runs the backend, which opens the frontend in the browser.

Usage: python start.py [--port 8000] [--force] [--no-browser]
"""
import hashlib
import subprocess
import sys
import venv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
ENV_DIR = PROJECT_DIR / "_env"
REQUIREMENTS_FILE = PROJECT_DIR / "requirements.txt"
REQUIREMENTS_STAMP_FILE = ENV_DIR / ".requirements_hash"
BACKEND_MAIN = PROJECT_DIR / "backend" / "main.py"


def find_environment_python():
    windows_python = ENV_DIR / "Scripts" / "python.exe"

    return windows_python if windows_python.exists() else ENV_DIR / "bin" / "python"


def hash_requirements():
    return hashlib.sha256(REQUIREMENTS_FILE.read_bytes()).hexdigest()


def are_requirements_installed():
    try:
        return REQUIREMENTS_STAMP_FILE.read_text() == hash_requirements()
    except OSError:
        return False


def install_requirements(python):
    print("Installing requirements ...")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--quiet", "-r", str(REQUIREMENTS_FILE)],
        check=True,
    )
    REQUIREMENTS_STAMP_FILE.write_text(hash_requirements())


def prepare_environment():
    """Creates _env if it is missing and installs the requirements if they changed."""
    if not ENV_DIR.exists():
        print("Creating virtual environment _env ...")
        venv.create(ENV_DIR, with_pip=True)

    python = find_environment_python()

    if not are_requirements_installed():
        install_requirements(python=python)

    return python


def main():
    python = prepare_environment()

    try:
        result = subprocess.run([str(python), str(BACKEND_MAIN), *sys.argv[1:]])
    except KeyboardInterrupt:
        return 0

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
