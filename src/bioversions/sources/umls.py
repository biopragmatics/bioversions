"""A getter for UMLS."""

from datetime import datetime

from bs4 import Tag

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "UMLSGetter",
]

URL = "https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html"


class UMLSGetter(Getter):
    """A getter for UMLS."""

    bioregistry_id = "umls"
    name = "UMLS"
    version_type = VersionType.other

    def get(self) -> datetime:
        """Get the latest UMLS version number."""
        soup = get_soup(URL)
        main_tag = soup.find("main")
        if not isinstance(main_tag, Tag):
            raise ValueError
        t1 = main_tag.find("div", {"class": "grid-row grid-gap-1"})  # type:ignore
        if not isinstance(t1, Tag):
            raise ValueError
        t2 = t1.find("div", {"class": "tablet:grid-col-12"})
        if not isinstance(t2, Tag):
            raise ValueError
        version_tag = t2.find("h2")
        if not isinstance(version_tag, Tag):
            raise ValueError
        version = version_tag.text.split()[0]
        return version


if __name__ == "__main__":
    UMLSGetter.print()
