"""
Entry point: checks for new versions (rebuilds images/Lottie), then starts the frontend.

Usage: python backend/main.py [--port 8000] [--force] [--no-browser]
"""
import argparse
import functools
import http.server
import threading
import webbrowser
from pathlib import Path

from build import rebuild_outdated_results

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
BROWSER_OPEN_DELAY_SECONDS = 0.5


class FrontendRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Windows sometimes serves .js as text/plain, and the browser then rejects the script
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".json": "application/json",
    }

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")   # Rebuilt files show up immediately
        super().end_headers()

    def log_message(self, format, *arguments):
        pass


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--force", action="store_true", help="rebuild everything")
    parser.add_argument("--no-browser", action="store_true", help="do not open the browser")

    return parser.parse_args()


def serve_frontend(port, open_browser):
    handler = functools.partial(FrontendRequestHandler, directory=str(FRONTEND_DIR))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{port}/"
    print(f"Frontend running: {url}  (Ctrl+C to stop)")

    if open_browser:
        threading.Timer(BROWSER_OPEN_DELAY_SECONDS, webbrowser.open, args=(url,)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


def main():
    arguments = parse_arguments()

    rebuild_outdated_results(force_all=arguments.force)
    serve_frontend(port=arguments.port, open_browser=not arguments.no_browser)


if __name__ == "__main__":
    main()
