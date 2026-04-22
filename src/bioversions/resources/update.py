"""Update the web page."""

from __future__ import annotations

import datetime
import getpass
import sys

import click
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from bioversions.resources import (
    EXPORT_PATH,
    FAILURES_PATH,
    Record,
    Release,
    load_versions,
    write_json,
    write_yaml,
)
from bioversions.sources import VersionFailure, iter_versions
from bioversions.utils import VersionResult
from bioversions.version import get_git_hash

__all__ = [
    "update",
]


@click.command()
@click.option("--force", is_flag=True)
def update(force: bool) -> None:
    """Update the data file."""
    with logging_redirect_tqdm():
        _update(force=force)


def _update(force: bool) -> None:
    if not get_git_hash():
        click.secho("Not on development installation", fg="red")
        raise sys.exit(1)

    today = datetime.date.today()
    data = load_versions()
    name_to_version = {entry.name: entry for entry in data.database}

    changes = False
    failure_tuples = []
    for bv in iter_versions(use_tqdm=True):
        if isinstance(bv, VersionFailure):
            failure_tuples.append(bv)
            continue
        new_release = Release(
            retrieved=today,
            version=bv.version,
            homepage=bv.homepage,
            date=bv.date,
        )
        if not (record := name_to_version.get(bv.name)):
            changes = True
            record = Record(
                name=bv.name,
                vtype=bv.vtype,
                releases=[new_release],
                prefix=bv.bioregistry_id,
            )
            data.database.append(record)
            _log_update(bv)
        elif all(bv.version != release.version for release in record.releases):
            changes = True
            _log_update(bv)
            record.releases.append(new_release)

    if not changes and not force:
        tqdm.write(click.style(f"No changes to {EXPORT_PATH}", fg="yellow", bold=True))
    else:
        data.database = sorted(data.database, key=lambda x: x.name.casefold())
        data.annotations.revision += 1
        data.annotations.date = today
        data.annotations.author = getpass.getuser()

        tqdm.write(click.style(f"Writing new {EXPORT_PATH}", fg="green", bold=True))
        write_yaml(data)
        write_json(data)

    if failure_tuples:
        click.secho(f"Writing failure summary to {FAILURES_PATH}")
        text = "# Summary of Errors\n\n"
        for t in failure_tuples:
            text += f"- **{t.name}**\n  `{t.message}`\n"
        text += "\n"
        for t in failure_tuples:
            text += f"## {t.name}\n\nUsing class: `{t.clstype}`\n\n"
            text += f"```python-traceback\n{t.trace}\n```\n\n"
        FAILURES_PATH.write_text(text.rstrip() + "\n")
    else:
        FAILURES_PATH.write_text("# No Errors :)\n")


def _log_update(bv: VersionResult) -> None:
    text = f"{bv.name} was updated to v{bv.version}"
    if bv.homepage:
        text += f". See {bv.homepage}"

    tqdm.write(click.style(text, fg="green", bold=True))

    try:
        from .. import slack_client
    except ImportError:
        pass
    else:
        slack_client.post(text)


if __name__ == "__main__":
    update()
