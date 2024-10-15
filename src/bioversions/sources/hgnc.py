# -*- coding: utf-8 -*-

"""A getter for HGNC."""

import datetime
import logging

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "HGNCGetter",
]

logger = logging.getLogger(__name__)

PATH = "https://storage.googleapis.com/public-download-files/hgnc/archive/archive/monthly/json/"
PREFIX = "hgnc_complete_set_"
SUFFIX = ".json"


class HGNCGetter(Getter):
    """A getter for HGNC."""

    bioregistry_id = "hgnc"
    name = "HGNC"
    homepage_fmt = PATH + "hgnc_complete_set_{version}.json"

    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest HGNC version number."""
        today = datetime.date.today()
        maybe = today.strftime("%Y-%m-01")
        res = requests.head(self.homepage_fmt.format(version=maybe))
        if res.status_code == 200:
            return maybe
        raise ValueError(f"HGNC hasn't posted new data for this month under version {maybe}")


if __name__ == "__main__":
    HGNCGetter.print()
