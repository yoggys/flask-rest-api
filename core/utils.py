import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1", type=str, help="Host name")
    parser.add_argument("--port", default=5000, type=int, help="Port number")
    parser.add_argument("--dev", action='store_true', help="Run server in development mode")
    return parser.parse_args()