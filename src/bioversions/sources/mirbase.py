# -*- coding: utf-8 -*-

"""A getter for miRBase."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "MirbaseGetter",
]

PREFIX = "0_THIS_IS_RELEASE_"


class MirbaseGetter(Getter):
    """A getter for miRBase."""

    bioregistry_id = "mirbase"
    name = "miRBase"
    homepage_fmt = "https://www.mirbase.org/ftp/{version}/"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest miRBase version number."""
        url = "https://www.mirbase.org/ftp/CURRENT/"
        soup = get_soup(url)
        rows = list(soup.find_all("tr"))
        cells = list(rows[3].find_all("td"))
        text = cells[1].find("a").text
        return text[len(PREFIX) :]


if __name__ == "__main__":
    MirbaseGetter.print()
