import polars

from arctic_calendar.models import Note


def add(input_file):
    df = polars.read_csv(
        getattr(input_file, "name", input_file),
        has_header=False,
        new_columns=["title", "description", "start_time", "end_time"],
        try_parse_dates=True,
    )
    Note.validate(df)
    df.glimpse()
