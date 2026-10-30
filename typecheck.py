"""
Type check of the backend with Pyright (the checker that Pylance uses in the IDE).
Installs requirements-dev.txt into the _env virtual environment on the first run.

Usage: python typecheck.py
"""
import subprocess
import sys

from start import ENV_DIR, PROJECT_DIR, find_environment_python

DEV_REQUIREMENTS_FILE = PROJECT_DIR / "requirements-dev.txt"


def is_pyright_installed(python):
    result = subprocess.run([str(python), "-m", "pyright", "--version"], capture_output=True)

    return result.returncode == 0


def install_dev_requirements(python):
    print("Installing Pyright ...")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--quiet", "-r", str(DEV_REQUIREMENTS_FILE)],
        check=True,
    )


def main():
    if not ENV_DIR.exists():
        print("The _env virtual environment is missing. Run python start.py once first.")
        return 1

    python = find_environment_python()

    if not is_pyright_installed(python=python):
        install_dev_requirements(python=python)

    return subprocess.run([str(python), "-m", "pyright"], cwd=PROJECT_DIR).returncode


if __name__ == "__main__":
    sys.exit(main())
