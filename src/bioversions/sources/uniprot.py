"""A getter for UniProt."""

from xml.etree import ElementTree

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "UniProtGetter",
]


class UniProtGetter(Getter):
    """A getter for UniProt."""

    bioregistry_id = "uniprot"
    name = "UniProt"
    homepage_fmt = (
        "ftp://ftp.uniprot.org/pub/databases/uniprot/previous_releases/release-{version}/"
    )
    date_version_fmt = "%Y_%m"
    version_type = VersionType.month

    def get(self):
        """Get the latest UniProt version number."""
        session = requests.Session()
        f = session.get(
            "https://ftp.uniprot.org/pub/databases/uniprot/current_release/RELEASE.metalink"
        )
        tree = ElementTree.fromstring(f.text)  # noqa:S314
        version_tag = tree.find("{http://www.metalinker.org/}version")
        return version_tag.text


if __name__ == "__main__":
    UniProtGetter.print()
