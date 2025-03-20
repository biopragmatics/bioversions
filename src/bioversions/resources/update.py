"""Update the web page."""

import getpass
import sys
from datetime import datetime

import click
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from bioversions.resources import (
    EXPORT_PATH,
    FAILURES_PATH,
    load_versions,
    write_export,
    write_versions,
)
from bioversions.sources import FailureTuple, _iter_versions
from bioversions.version import get_git_hash

__all__ = [
    "update",
]


def _get_clean_dict(d):
    return {k: v for k, v in d.to_dict().items() if k and v}


@click.command()
@click.option("--force", is_flag=True)
def update(force: bool) -> None:
    """Update the data file."""
    with logging_redirect_tqdm():
        _update(force=force)


def _update(force: bool):  # noqa:C901
    if not get_git_hash():
        click.secho("Not on development installation", fg="red")
        return sys.exit(1)

    data = load_versions()

    revision = data["annotations"]["revision"]
    versions = {entry["name"]: entry for entry in data["database"]}

    today = datetime.now().strftime("%Y-%m-%d")

    changes = False
    failure_tuples = []
    for bv in _iter_versions(use_tqdm=True):
        if isinstance(bv, FailureTuple):
            failure_tuples.append(bv)
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
        tqdm.write(click.style(f"No changes to {EXPORT_PATH}", fg="yellow", bold=True))
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
        tqdm.write(click.style(f"Writing new {EXPORT_PATH}", fg="green", bold=True))
        write_export(rv)
        write_versions(rv)

    if failure_tuples:
        click.secho(f"Writing failure summary to {FAILURES_PATH}")
        text = "# Summary of Errors\n\n"
        for t in failure_tuples:
            text += f"- {t.name} - {t.message}\n"
        text += "\n"
        for t in failure_tuples:
            text += f"## {t.name}\n\nUsing class: `{t.clstype}`\n\n"
            text += f"```python-traceback\n{t.trace}\n```\n\n"
        FAILURES_PATH.write_text(text.rstrip() + "\n")


def _log_update(bv) -> None:
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
