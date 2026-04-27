"""A getter for UMLS."""

from typing import ClassVar

from bioversions.utils import Getter, VersionType, find_soup_tag, find_soup_text, get_soup

__all__ = [
    "UMLSGetter",
]

URL = "https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html"


class UMLSGetter(Getter):
    """A getter for UMLS."""

    collection: ClassVar[list[str]] = ["umls", "sty", "umls.aui"]
    name = "UMLS"
    version_type = VersionType.other

    def get(self) -> str:
        """Get the latest UMLS version number."""
        soup = get_soup(URL)
        main_tag = find_soup_tag(soup, "main")
        t1 = find_soup_tag(main_tag, "div", {"class": "grid-row grid-gap-1"})
        t2 = find_soup_tag(t1, "div", {"class": "tablet:grid-col-12"})
        version_tag_text = find_soup_text(t2, "h2")
        version = version_tag_text.split()[0]
        return version


if __name__ == "__main__":
    UMLSGetter.print()
