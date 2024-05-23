import csv
import datetime

from arctic_calendar.models import Note
from arctic_calendar.notes import add


def test_add(tmpdir, capsys):
    test_file = tmpdir.join("test.csv")
    df = Note.examples(data={"title": ["a", "b", "c"]})

    def encode(row):
        return [
            cell.isoformat() if isinstance(cell, datetime.datetime) else cell
            for cell in row
        ]

    with open(test_file, "w") as infile:
        csv.writer(infile).writerows([encode(row) for row in df.rows()])

    add(input_file=str(test_file))

    expected_rows = len(df.rows())
    assert f"Rows: {expected_rows}\nColumns: 4" in capsys.readouterr().out[:19]
