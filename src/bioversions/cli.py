# -*- coding: utf-8 -*-

"""Command line interface for bioversions."""

import click
from click_default_group import DefaultGroup
from more_click import make_web_command, verbose_option
from tabulate import tabulate

from .update import update


@click.group(cls=DefaultGroup, default='web', default_if_no_args=True)
def main():  # noqa:D401
    """The bioversions CLI."""


main.add_command(update)

web = make_web_command(
    app='bioversions.wsgi:app',
    group=main,
    command_kwargs=dict(
        help='Run the bioversions web application.',
    ),
)


@main.command()
@click.argument('key')
@verbose_option
def get(key: str):
    """Print the version."""
    from . import get_version
    click.echo(get_version(key))


@main.command()
def ls():
    """List versions."""
    from . import get_rows
    click.echo(tabulate(get_rows()))


if __name__ == '__main__':
    main()
