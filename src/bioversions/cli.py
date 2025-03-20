"""Command line interface for :mod:`bioversions`."""

import click
from click_default_group import DefaultGroup
from more_click import make_web_command, verbose_option
from tabulate import tabulate

from bioversions.resources.update import update


@click.group(cls=DefaultGroup, default="web", default_if_no_args=True)
@click.version_option()
def main() -> None:
    """The bioversions CLI."""  # noqa:D401


main.add_command(update)

web = make_web_command(
    app="bioversions.wsgi:app",
    group=main,
    command_kwargs={
        "help": "Run the bioversions web application.",
    },
)


@main.command()  # type:ignore
@click.argument("key")
@verbose_option  # type:ignore
def get(key: str) -> None:
    """Print the version."""
    from . import get_version

    click.echo(get_version(key))


@main.command()  # type:ignore
@click.option("--terse", "-t", is_flag=True)
def ls(terse: bool) -> None:
    """List versions."""
    from . import get_rows

    if terse:
        click.echo(
            tabulate(
                sorted(
                    (bv.bioregistry_id or "", bv.classname, bv.version)
                    for bv in get_rows(use_tqdm=True)
                ),
                headers=["Prefix", "Class", "Version"],
            )
        )
    else:
        click.echo(
            tabulate(
                (
                    (bv.bioregistry_id, bv.name, bv.version, bv.date, bv.homepage)
                    for bv in get_rows(use_tqdm=True)
                ),
                headers=["Prefix", "Name", "Version", "Release Date", "Homepage"],
            )
        )


if __name__ == "__main__":
    main()
