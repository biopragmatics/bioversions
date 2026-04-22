"""Resources."""

from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict
from pystow.utils.pydantic_utils import read_pydantic_yaml

from bioversions.utils import VersionType

__all__ = [
    "EXPORT_PATH",
    "VERSIONS_PATH",
    "load_versions",
    "write_json",
    "write_yaml",
]

HERE = Path(__file__).parent.resolve()
VERSIONS_PATH = HERE.joinpath(HERE, "versions.json")

ROOT = HERE.parent.parent.parent.resolve()
PYPROJECT_TOML_PATH = ROOT.joinpath("pyproject.toml")
DOCS = ROOT.joinpath("docs")
EXPORTS_DIRECTORY = DOCS.joinpath("_data")
EXPORT_PATH = EXPORTS_DIRECTORY.joinpath("versions.yml")
FAILURES_PATH = DOCS.joinpath("failures.md")


class Metadata(BaseModel):
    """Represents metadata on the database."""

    revision: int
    date: datetime.date
    author: str


class Release(BaseModel):
    """Represents a release of a resource tracked by the database."""

    retrieved: datetime.date
    version: str
    homepage: str | None = None
    date: datetime.date | None = None


class Record(BaseModel):
    """Represents a resource tracked by the database."""

    model_config = ConfigDict(use_enum_values=False)

    name: str
    prefix: str | None = None
    releases: list[Release]
    vtype: VersionType


class Database(BaseModel):
    """Represents a version database."""

    annotations: Metadata
    database: list[Record]


def load_versions() -> Database:
    """Load Bioversions data."""
    if not VERSIONS_PATH.is_file():
        raise RuntimeError(
            f"bioversions was not packaged/built/installed properly -"
            f"{VERSIONS_PATH.name} was not found inside the distribution"
        )
    return read_pydantic_yaml(VERSIONS_PATH, Database)


def write_json(versions: Database, indent: int = 2, **kwargs: Any) -> None:
    """Write Bioversions data."""
    _ensure_editable()
    VERSIONS_PATH.write_text(versions.model_dump_json(indent=indent, exclude_none=True, **kwargs))


def write_yaml(versions: Database) -> None:
    """Write Bioversions data to the export directory."""
    _ensure_editable()
    EXPORT_PATH.write_text(yaml.safe_dump(versions.model_dump(exclude_none=True, mode="json")))


def _ensure_editable() -> None:
    if not PYPROJECT_TOML_PATH.is_file():
        raise RuntimeError("can not make export when bioversions is not installed in editable mode")
