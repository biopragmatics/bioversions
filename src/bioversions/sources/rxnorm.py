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

    def get(self) -> datetime:
        """Get the latest RxNorm version number."""
        soup = get_soup(URL)
        raw_version = soup.find("th", {"class": "current"}).contents[2].strip()
        raw_fmt = "%B %d, %Y"
        return datetime.strptime(raw_version, raw_fmt)

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Transform date to match RxNorm download URL."""
        return datetime.strftime(datetime.strptime(version, "%Y-%m-%d"), "%m%d%Y")


if __name__ == "__main__":
    RxNormGetter.print()
