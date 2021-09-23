# -*- coding: utf-8 -*-

"""A getter for the Molecular Oncology Almanac."""

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "MOAlmanacGetter",
]

URL = "https://moalmanac.org/"


class MOAlmanacGetter(Getter):
    """A getter for MOAlmanac."""

    bioregistry_id = "moalmanac"
    name = "Molecular Oncology Almanac"
    homepage_fmt = "https://github.com/vanallenlab/moalmanac-db/releases/tag/v.{version}"
    date_version_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        sub_footer = soup.find("div", {"class": "text-right"})
        version = sub_footer.find("a").text
        return version


if __name__ == "__main__":
    MOAlmanacGetter.print()
