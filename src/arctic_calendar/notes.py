import pathlib

import polars

from arctic_calendar.models import Note


def add(input_file, database):
    new_notes = polars.read_csv(
        getattr(input_file, "name", input_file),
        has_header=False,
        new_columns=["title", "description", "start_time", "end_time"],
        try_parse_dates=True,
    )
    Note.validate(new_notes)

    if pathlib.Path(database).exists():
        persisted_notes = polars.read_ipc(database, memory_map=False)
        notes = polars.concat([new_notes, persisted_notes])
    else:
        notes = new_notes

    notes.write_ipc(database)
    notes.glimpse()
