# -*- coding: utf-8 -*-

"""Update the web page."""

import os

import click
import yaml

__all__ = [
    'update',
]

HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, '_data'))
PATH = os.path.join(DATA, 'versions.yml')


@click.command()
def update():
    """Update the data file."""
    from bioversions.sources import _iter_versions
    with open(PATH, 'w') as file:
        yaml.dump([x.to_dict() for x in _iter_versions()], file)


if __name__ == '__main__':
    update()
