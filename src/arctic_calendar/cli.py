import argparse
import sys
import tempfile

from arctic_calendar import appointments


def parse_arguments():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(title="commands", dest="command")

    add = commands.add_parser("add")
    add.add_argument(
        "infile",
        nargs=(None if sys.stdin.isatty() else "?"),
        type=argparse.FileType("r"),
        default=(None if sys.stdin.isatty() else sys.stdin),
    )
    add.add_argument(
        "--database",
        default=tempfile.mktemp(suffix=".feather"),
        help="Path to the persisted feather database",
    )

    return parser.parse_args()


def run_with_arguments(arguments):
    match arguments.command:
        case "add":
            appointments.add(arguments.infile, arguments.database)
        case _:
            raise ValueError(f"Unknown command: {arguments.command!r}")
