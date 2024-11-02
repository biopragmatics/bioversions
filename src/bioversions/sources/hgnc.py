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
        this_year = int(today.strftime("%Y"))
        this_month = int(today.strftime("%m"))
        maybe = today.strftime("%Y-%m-01")
        res = requests.head(self.homepage_fmt.format(version=maybe))
        if res.status_code == 200:
            return maybe
        if this_month == 1:
            maybe_last_month = f"{this_year - 1}-12-01"
        else:
            maybe_last_month = f"{this_year}-{this_month - 1}-01"
        return maybe_last_month


if __name__ == "__main__":
    HGNCGetter.print()
