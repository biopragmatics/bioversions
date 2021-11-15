# -*- coding: utf-8 -*-

"""A getter for ChEBI."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "ChEBIGetter",
]

URL = "https://ftp.ebi.ac.uk/pub/databases/chebi/archive/"


class ChEBIGetter(Getter):
    """A getter for ChEBI."""

    bioregistry_id = "chebi"
    name = "ChEBI"
    version_type = VersionType.sequential
    date_fmt = "%d-%b-%Y"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/chebi/archive/rel{version}/"

    def get(self):
        """Get the latest ChEBI version number."""
        soup = get_soup(URL)
        anchors = soup.find("pre").find_all("a")
        last = list(anchors)[-1]
        date = last.next_sibling.strip().split()[0]
        version = last.text.rstrip("/")[len("rel") :]
        return dict(version=version, date=date)


if __name__ == "__main__":
    ChEBIGetter.print()
