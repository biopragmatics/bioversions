# -*- coding: utf-8 -*-

"""A getter for BioGRID."""

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "BioGRIDGetter",
]

URL = "https://downloads.thebiogrid.org/BioGRID/Latest-Release/"


class BioGRIDGetter(Getter):
    """A getter for BioGRID."""

    bioregistry_id = "biogrid"
    name = "BioGRID"
    homepage_fmt = "https://downloads.thebiogrid.org/BioGRID/Release-Archive/BIOGRID-{version}"
    version_type = VersionType.semver

    def get(self) -> str:
        """Get the latest BioGRID version number."""
        soup = get_soup(URL)
        manifest = soup.find(id="manifestDesc")
        header = manifest.find("h2")
        return header.text[len("BioGRID Release ") :]


if __name__ == "__main__":
    BioGRIDGetter.print()
