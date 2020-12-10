# -*- coding: utf-8 -*-

"""Update the web page."""

import os
from datetime import datetime

import click
import yaml

__all__ = [
    'update',
]

HERE = os.path.abspath(os.path.dirname(__file__))
DATA = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'docs', '_data'))
PATH = os.path.join(DATA, 'versions.yml')


def _get_clean_dict(d):
    return {k: v for k, v in d.to_dict().items() if k and v}


@click.command()
def update():
    """Update the data file."""
    with open(PATH) as file:
        old = yaml.safe_load(file)

    from bioversions.sources import _iter_versions
    today = datetime.now().strftime('%Y-%m-%d')

    rv = []
    for bv in _iter_versions():
        click.echo(str(bv))
        rv.append({
            'retrieved': today,
            **_get_clean_dict(bv),
        })

    if rv == old:
        click.secho(f'No changes to {PATH}', fg='yellow', bold=True)
    else:
        click.secho(f'Writing new {PATH}', fg='green', bold=True)
        with open(PATH, 'w') as file:
            yaml.dump(rv, file)


if __name__ == '__main__':
    update()
