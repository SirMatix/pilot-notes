import argparse
from .normalize import normalize


def main(argv=None):
    parser = argparse.ArgumentParser(prog="pilot-notes")
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("normalize")
    command.add_argument("text")
    args = parser.parse_args(argv)
    print(normalize(args.text))
