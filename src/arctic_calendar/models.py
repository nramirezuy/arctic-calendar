import datetime

import patito
import polars


class Note(patito.Model):
    title: str = patito.Field(
        constraints=polars.col("title").is_not_null(),
        dtype=polars.String(),
        max_length=256,
    )
    description: str | None = patito.Field(
        dtype=polars.String(), max_length=1e6
    )
    start_time: datetime.datetime = patito.Field(
        constraints=polars.col("start_time").is_not_null(),
        dtype=polars.Datetime(),
    )
    end_time: datetime.datetime = patito.Field(
        constraints=polars.col("end_time").is_not_null(),
        dtype=polars.Datetime(),
    )
