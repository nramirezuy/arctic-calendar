import argparse
import datetime
import sys
import tempfile

import dateutil

from arctic_calendar import appointments


def to_datetime(value):
    return dateutil.parser.parse(value)


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

    where = commands.add_parser("where")
    where.add_argument(
        "--after",
        type=to_datetime,
        default=datetime.datetime.now() - datetime.timedelta(days=3),
    )
    where.add_argument(
        "--before",
        type=to_datetime,
        default=datetime.datetime.now() + datetime.timedelta(days=3),
    )
    where.add_argument(
        "--database",
        help="Path to the persisted feather database",
    )

    return parser.parse_args()


def run_with_arguments(arguments):
    match arguments.command:
        case "add":
            appointments.add(arguments.infile, arguments.database)
        case "where":
            appointments.where(
                arguments.after, arguments.before, arguments.database
            )
        case _:
            raise ValueError(f"Unknown command: {arguments.command!r}")
