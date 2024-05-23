import sys

from arctic_calendar.cli import parse_arguments
from arctic_calendar.cli import run_with_arguments


def main():
    run_with_arguments(parse_arguments())
    return 0


if __name__ == "__main__":
    sys.exit(main())
