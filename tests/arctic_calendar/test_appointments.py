import csv
import datetime

from arctic_calendar.appointments import add
from arctic_calendar.models import Appointment


def test_add__from_nothing(tmpdir, capsys):
    test_file = tmpdir.join("test.csv")
    df = Appointment.examples(data={"title": ["a", "b", "c"]})

    def encode(row):
        return [
            cell.isoformat() if isinstance(cell, datetime.datetime) else cell
            for cell in row
        ]

    with open(test_file, "w") as infile:
        csv.writer(infile).writerows([encode(row) for row in df.rows()])

    add(
        input_file=str(test_file),
        database=str(tmpdir.join("database.feather")),
    )

    expected_rows = len(df.rows())
    assert f"Rows: {expected_rows}\nColumns: 4" in capsys.readouterr().out[:19]


def test_add__persistency(tmpdir, capsys):
    test_file = tmpdir.join("test.csv")
    df = Appointment.examples(data={"title": ["a", "b", "c"]})

    def encode(row):
        return [
            cell.isoformat() if isinstance(cell, datetime.datetime) else cell
            for cell in row
        ]

    with open(test_file, "w") as infile:
        csv.writer(infile).writerows([encode(row) for row in df.rows()])

    database = str(tmpdir.join("database.feather"))
    add(input_file=str(test_file), database=database)
    add(input_file=str(test_file), database=database)

    expected_rows = len(df.rows()) * 2
    captured = capsys.readouterr()
    assert f"Rows: {expected_rows}\nColumns: 4" in captured.out
