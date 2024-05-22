import patito
import polars


class Note(patito.Model):
    title = patito.Field(
        constraints=polars.col("title").is_not_null(),
        dtype=polars.String(),
        max_length=256,
    )
    description = patito.Field(dtype=polars.String(), max_length=1e6)
    start_time = patito.Field(
        constraints=polars.col("start_time").is_not_null(),
        dtype=polars.Datetime(),
    )
    end_time = patito.Field(
        constraints=polars.col("end_time").is_not_null(),
        dtype=polars.Datetime(),
    )
