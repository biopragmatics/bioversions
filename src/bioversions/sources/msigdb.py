"""A getter for MSigDB."""

from bioversions.utils import Getter, VersionType, find_soup_tag, get_soup

__all__ = [
    "MSigDBGetter",
]

URL = "http://www.gsea-msigdb.org/gsea/msigdb/index.jsp"


class MSigDBGetter(Getter):
    """A getter for MSigDB."""

    bioregistry_id = "msigdb"
    name = "MSigDB"
    homepage_fmt = "https://data.broadinstitute.org/gsea-msigdb/msigdb/release/{version}"
    version_type = VersionType.year_minor

    def get(self) -> str:
        """Get the latest MSigDB version number."""
        soup = get_soup(URL)
        x = find_soup_tag(soup, text="Current Version")
        if x.parent is None:
            raise ValueError
        paragraph = x.parent.find_next_sibling("p")
        if paragraph is None:
            raise ValueError
        if not isinstance(paragraph.text, str):
            raise ValueError
        version = paragraph.text.strip().split()[2][len("v") : -len(".Hs")]
        return version


if __name__ == "__main__":
    MSigDBGetter.print()
