"""A getter for HGNC."""

import logging
from typing import ClassVar

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "HGNCGetter",
]

logger = logging.getLogger(__name__)

PATH = "https://storage.googleapis.com/public-download-files/hgnc/archive/archive/monthly/json/"
URL = "https://storage.googleapis.com/storage/v1/b/public-download-files/o?prefix=hgnc/archive/archive/monthly"
PREFIX = "hgnc/archive/archive/monthly/json/hgnc_complete_set_"
SUFFIX = ".json"


class HGNCGetter(Getter):
    """A getter for HGNC."""

    collection: ClassVar[list[str]] = ["hgnc", "hgnc.symbol", "hgnc.genegroup", "hgnc.genesymbol"]
    name = "HGNC"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest monthly HGNC version number."""
        res = requests.get(URL, timeout=5)
        items = res.json()["items"]
        return max(
            item["name"].removeprefix(PREFIX).removesuffix(SUFFIX)
            for item in items
            if (name := item["name"]).startswith(PREFIX) and name.endswith(SUFFIX)
        )


if __name__ == "__main__":
    HGNCGetter.print()
