# -*- coding: utf-8 -*-

"""Update the web page."""

import getpass
import sys
from datetime import datetime

import click
from tqdm.contrib.logging import logging_redirect_tqdm

from bioversions.resources import (
    EXPORT_PATH,
    FAILURES_PATH,
    load_versions,
    write_export,
    write_versions,
)
from bioversions.sources import _iter_versions
from bioversions.version import get_git_hash

__all__ = [
    "update",
]


def _get_clean_dict(d):
    return {k: v for k, v in d.to_dict().items() if k and v}


@click.command()
@click.option("--force", is_flag=True)
def update(force: bool):
    """Update the data file."""
    with logging_redirect_tqdm():
        _update(force=force)


def _update(force: bool):
    if not get_git_hash():
        click.secho("Not on development installation", fg="red")
        return sys.exit(1)

    data = load_versions()

    revision = data["annotations"]["revision"]
    versions = {entry["name"]: entry for entry in data["database"]}

    today = datetime.now().strftime("%Y-%m-%d")

    changes = False
    errors = []
    for bv, error in _iter_versions(use_tqdm=True):
        if error is not None or bv is None:
            errors.append(error)
            continue

        if bv.name in versions:
            v = versions[bv.name]
        else:
            v = versions[bv.name] = {
                "releases": [],
            }

        if bv.name:
            v["name"] = bv.name
        if bv.bioregistry_id:
            v["prefix"] = bv.bioregistry_id
        if bv.vtype:
            v["vtype"] = bv.vtype.name

        if not v["releases"] or v["releases"][-1]["version"] != bv.version:
            _log_update(bv)
            changes = True
            append_dict = {
                "retrieved": today,
                "version": bv.version,
            }
            if bv.homepage:
                append_dict["homepage"] = bv.homepage
            if bv.date:
                append_dict["date"] = bv.date.strftime("%Y-%m-%d")
            v["releases"].append(append_dict)

    if not changes and not force:
        click.secho(f"No changes to {EXPORT_PATH}", fg="yellow", bold=True)
    else:
        rv_database = sorted(versions.values(), key=lambda version: version["name"].lower())
        rv = {
            "annotations": {
                "revision": revision + 1,
                "date": datetime.today().strftime("%Y-%m-%d"),
                "author": getpass.getuser(),
            },
            "database": rv_database,
        }
        click.secho(f"Writing new {EXPORT_PATH}", fg="green", bold=True)
        write_export(rv)
        write_versions(rv)

    FAILURES_PATH.write_text("# Errors\n\n" + "\n".join(f"- {error}" for error in errors))


def _log_update(bv) -> None:
    text = f"{bv.name} was updated to v{bv.version}"
    if bv.homepage:
        text += f". See {bv.homepage}"

    click.secho(text, fg="green", bold=True)

    try:
        from .. import slack_client
    except ImportError:
        pass
    else:
        slack_client.post(text)

    try:
        from .. import twitter_client
    except ImportError:
        pass
    else:
        twitter_client.post(text)


if __name__ == "__main__":
    update()
