# Arctic Calendar

## About

This is a Calendar/Diary application built on top of [polars][polars].
Because, why not? :relaxed:

## Usage

Adding a single note can be done with HereDoc, supported format is csv
without headers. Dates have to be parsable by [polars][polars].

```sh
arctic-calendar add << EOF
title,description,start-time,end-time
EOF
```

Or you could point to a file:

```sh
arctic-calendar add mynotes.csv
```

## Roadmap

- [x] Design initial data schemas
- [x] Load a single note from cli
- [x] Make notes persistent
- [ ] List notes to cli
- [x] Read notes from stdin
- [ ] Filter notes to cli
- [ ] What next?

See the [open issues][open-issues] for a full list of
proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place
to learn, inspire, and create.
Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork
the reposiotry and create a pull request. You can also simply open
an issue with the tag "enhancement".

Things to keep in mind:

- We use pre-commit, so don't forget to run `pre-commit install`

[open-issues]: https://github.com/othneildrew/Best-README-Template/issues
[polars]: https://pola.rs/
