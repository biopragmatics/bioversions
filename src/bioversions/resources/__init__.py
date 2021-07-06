# -*- coding: utf-8 -*-

"""Resources."""

import datetime
import json
import os

import yaml

__all__ = [
    "VERSIONS_PATH",
    "EXPORT_PATH",
    "load_versions",
    "write_versions",
    "write_export",
]

HERE = os.path.abspath(os.path.dirname(__file__))
VERSIONS_PATH = os.path.join(HERE, "versions.json")

EXPORTS_DIRECTORY = os.path.abspath(
    os.path.join(HERE, os.pardir, os.pardir, os.pardir, "docs", "_data")
)
EXPORT_PATH = os.path.join(EXPORTS_DIRECTORY, "versions.yml")


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
