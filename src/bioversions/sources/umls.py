"""A getter for UMLS."""

from bioversions.utils import Getter, VersionType, find, get_soup

__all__ = [
    "UMLSGetter",
]

URL = "https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html"


class UMLSGetter(Getter):
    """A getter for UMLS."""

    bioregistry_id = "umls"
    name = "UMLS"
    version_type = VersionType.other

    def get(self) -> str:
        """Get the latest UMLS version number."""
        soup = get_soup(URL)
        main_tag = find(soup, "main")
        t1 = find(main_tag, "div", {"class": "grid-row grid-gap-1"})  # type:ignore
        t2 = find(t1, "div", {"class": "tablet:grid-col-12"})
        version_tag = find(t2, "h2")
        version = version_tag.text.split()[0]
        return version


if __name__ == "__main__":
    UMLSGetter.print()
