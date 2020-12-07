# -*- coding: utf-8 -*-

"""Command line interface for bioversions."""

import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default='web', default_if_no_args=True)
def main():  # noqa:D401
    """The bioversions CLI."""


@main.command()
def web():
    """Run the bioversions web application."""
    from .wsgi import app
    app.run()


@main.command()
@click.argument('key')
def get(key: str):
    """Print the version."""
    from . import get_version
    click.echo(get_version(key))


if __name__ == '__main__':
    main()
