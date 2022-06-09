# -*- coding: utf-8 -*-

"""Resources."""

import datetime
import json
from pathlib import Path

import yaml

__all__ = [
    "VERSIONS_PATH",
    "EXPORT_PATH",
    "load_versions",
    "write_versions",
    "write_export",
]

HERE = Path(__file__).parent.resolve()
VERSIONS_PATH = HERE.joinpath(HERE, "versions.json")

ROOT = HERE.parent.parent.parent.resolve()
DOCS = ROOT.joinpath("docs")
EXPORTS_DIRECTORY = DOCS.joinpath("_data")
EXPORT_PATH = EXPORTS_DIRECTORY.joinpath("versions.yml")
FAILURES_PATH = DOCS.joinpath("failures.md")


def load_versions():
    """Load Bioversions data."""
    with open(VERSIONS_PATH) as file:
        return json.load(file)


def _date_converter(o):
    if isinstance(o, (datetime.datetime, datetime.date)):
        return o.strftime("%Y-%m-%d")


def write_versions(versions, indent: int = 2, **kwargs):
    """Write Bioversions data."""
    with open(VERSIONS_PATH, "w") as file:
        json.dump(versions, file, indent=indent, default=_date_converter, **kwargs)


def write_export(versions):
    """Write Bioversions data to the export directory."""
    with open(EXPORT_PATH, "w") as file:
        yaml.safe_dump(versions, file)
