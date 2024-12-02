"""Resources."""

import datetime
import json
from pathlib import Path

import yaml

__all__ = [
    "EXPORT_PATH",
    "VERSIONS_PATH",
    "load_versions",
    "write_export",
    "write_versions",
]

HERE = Path(__file__).parent.resolve()
VERSIONS_PATH = HERE.joinpath(HERE, "versions.json")

ROOT = HERE.parent.parent.parent.resolve()
PYPROJECT_TOML_PATH = ROOT.joinpath("pyproject.toml")
DOCS = ROOT.joinpath("docs")
EXPORTS_DIRECTORY = DOCS.joinpath("_data")
EXPORT_PATH = EXPORTS_DIRECTORY.joinpath("versions.yml")
FAILURES_PATH = DOCS.joinpath("failures.md")


def load_versions():
    """Load Bioversions data."""
    if not VERSIONS_PATH.is_file():
        raise RuntimeError(
            f"bioversions was not packaged/built/installed properly -"
            f"{VERSIONS_PATH.name} was not found inside the distribution"
        )
    with open(VERSIONS_PATH) as file:
        return json.load(file)


def _date_converter(o):
    if isinstance(o, datetime.datetime | datetime.date):
        return o.strftime("%Y-%m-%d")


def write_versions(versions, indent: int = 2, **kwargs) -> None:
    """Write Bioversions data."""
    _ensure_editable()
    with open(VERSIONS_PATH, "w") as file:
        json.dump(versions, file, indent=indent, default=_date_converter, **kwargs)


def write_export(versions) -> None:
    """Write Bioversions data to the export directory."""
    _ensure_editable()
    with open(EXPORT_PATH, "w") as file:
        yaml.safe_dump(versions, file)


def _ensure_editable() -> None:
    if not PYPROJECT_TOML_PATH.is_file():
        raise RuntimeError("can not make export when bioversions is not installed in editable mode")
