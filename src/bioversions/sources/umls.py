"""A getter for UMLS."""

from datetime import datetime

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
        version_tag = (
            soup.find("main")
            .find("div", {"class": "grid-row grid-gap-1"})
            .find("div", {"class": "tablet:grid-col-12"})
            .find("h2")
        )
        version = version_tag.text.split()[0]
        return version


if __name__ == "__main__":
    UMLSGetter.print()
