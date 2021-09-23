# -*- coding: utf-8 -*-

"""A getter for RxNorm."""

from datetime import datetime

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "RxNormGetter",
]

URL = "https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html"


class RxNormGetter(Getter):
    """A getter for RxNorm."""

    bioregistry_id = "rxnorm"
    name = "RxNorm"
    homepage_fmt = "https://download.nlm.nih.gov/umls/kss/rxnorm/RxNorm_full_{version}.zip"
    version_type = VersionType.date
    date_fmt = "%m%d%Y"

    def get(self) -> str:
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        raw_version = soup.find("th", {"class": "current"}).contents[2]
        raw_fmt = "%B %d, %Y"
        dt = datetime.strptime(raw_version, raw_fmt)
        version = datetime.strftime(dt, "%m%d%Y")
        return version


if __name__ == "__main__":
    RxNormGetter.print()
