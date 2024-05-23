import pathlib

import polars

from arctic_calendar.models import Appointment


def add(input_file, database):
    new_appointments = polars.read_csv(
        getattr(input_file, "name", input_file),
        has_header=False,
        new_columns=["title", "description", "start_time", "end_time"],
        try_parse_dates=True,
    )
    Appointment.validate(new_appointments)

    if pathlib.Path(database).exists():
        stored_appointments = polars.read_ipc(database, memory_map=False)
        appointments = polars.concat([new_appointments, stored_appointments])
    else:
        appointments = new_appointments

    appointments.write_ipc(database)
    appointments.glimpse()
