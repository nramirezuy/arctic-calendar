import argparse
import sys

from arctic_calendar import notes


def parse_arguments():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(title="commands", dest="command")

    add = commands.add_parser("add")
    add.set_defaults(func=notes.add)
    add.add_argument(
        "infile",
        nargs=(None if sys.stdin.isatty() else "?"),
        type=argparse.FileType("r"),
        default=(None if sys.stdin.isatty() else sys.stdin),
    )

    return parser.parse_args()


def run_with_arguments(arguments):
    match arguments.command:
        case "add":
            arguments.func(arguments.infile)
        case _:
            raise ValueError(f"Unknown command: {arguments.command!r}")
