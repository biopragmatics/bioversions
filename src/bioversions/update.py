# -*- coding: utf-8 -*-

"""Update the web page."""

import operator
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
        versions = {
            entry['name']: entry
            for entry in yaml.safe_load(file)
        }

    from bioversions.sources import _iter_versions
    today = datetime.now().strftime('%Y-%m-%d')

    changes = False
    for bv in _iter_versions():
        if bv.name in versions:
            v = versions[bv.name]
        else:
            v = versions[bv.name] = {
                'name': bv.name,
                'releases': [],
            }

        if not v['releases'] or v['releases'][-1]['version'] != bv.version:
            click.secho(f'Updating {bv.name} to {bv.version}', fg='green', bold=True)
            changes = True
            append_dict = {
                'retrieved': today,
                'version': bv.version,
            }
            if bv.homepage:
                append_dict['homepage'] = bv.homepage
            if bv.date:
                append_dict['date'] = bv.date
            v['releases'].append(append_dict)

    if not changes:
        click.secho(f'No changes to {PATH}', fg='yellow', bold=True)
    else:
        rv = sorted(versions.values(), key=operator.itemgetter('name'))
        click.secho(f'Writing new {PATH}', fg='green', bold=True)
        with open(PATH, 'w') as file:
            yaml.dump(rv, file)


if __name__ == '__main__':
    update()
