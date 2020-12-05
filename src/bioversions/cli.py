# -*- coding: utf-8 -*-

"""Command line interface for bioversions."""

import click


@click.command()
def main():
    """Run the bioversions web application."""
    from .wsgi import app
    app.run()


if __name__ == '__main__':
    main()
