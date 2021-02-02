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
@click.option('--force', is_flag=True)
def update(force: bool):
    """Update the data file."""
    with open(PATH) as file:
        versions = {
            entry['name']: entry
            for entry in yaml.safe_load(file)
        }

    from bioversions.sources import _iter_versions
    today = datetime.now().strftime('%Y-%m-%d')

    changes = False
    for bv in _iter_versions(use_tqdm=True):
        if bv.name in versions:
            v = versions[bv.name]
        else:
            v = versions[bv.name] = {
                'releases': [],
            }

        if bv.name:
            v['name'] = bv.name
        if bv.bioregistry_id:
            v['prefix'] = bv.bioregistry_id

        if not v['releases'] or v['releases'][-1]['version'] != bv.version:
            _log_update(bv)
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

    if not changes and not force:
        click.secho(f'No changes to {PATH}', fg='yellow', bold=True)
    else:
        rv = sorted(versions.values(), key=lambda version: version['name'].lower())
        click.secho(f'Writing new {PATH}', fg='green', bold=True)
        with open(PATH, 'w') as file:
            yaml.dump(rv, file)


def _log_update(bv) -> None:
    text = f'{bv.name} was updated to v{bv.version}'
    if bv.homepage:
        text += f'. See {bv.homepage}'

    click.secho(text, fg='green', bold=True)

    try:
        from . import slack_client
    except ImportError:
        pass
    else:
        slack_client.post(text)

    try:
        from . import twitter_client
    except ImportError:
        pass
    else:
        twitter_client.post(text)


if __name__ == '__main__':
    update()
