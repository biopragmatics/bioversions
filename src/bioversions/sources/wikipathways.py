# -*- coding: utf-8 -*-

"""A getter for WikiPathways."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "WikiPathwaysGetter",
]

URL = "http://data.wikipathways.org/current/gmt/"


class WikiPathwaysGetter(Getter):
    """A getter for WikiPathways."""

    bioregistry_id = "wikipathways"
    name = "WikiPathways"
    homepage_fmt = "http://data.wikipathways.org/{version}/"
    date_version_fmt = "%Y%m%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest WikiPathways version number."""
        soup = get_soup(URL)
        element = soup.find("tbody").find("tr").find("td").find("a")
        return element.text.split("-")[1]


if __name__ == "__main__":
    WikiPathwaysGetter.print()
