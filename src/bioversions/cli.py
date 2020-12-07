# -*- coding: utf-8 -*-

"""Command line interface for bioversions."""

import click
from click_default_group import DefaultGroup


@click.group(cls=DefaultGroup, default='web', default_if_no_args=True)
def main():
    """The bioversions CLI."""


@main.command()
def web():
    """Run the bioversions web application."""
    from .wsgi import app
    app.run()


if __name__ == '__main__':
    main()
