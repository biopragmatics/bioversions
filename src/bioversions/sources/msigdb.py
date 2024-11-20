"""A getter for MSigDB."""

from bioversions.utils import Getter, VersionType, get_soup

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

    def get(self):
        """Get the latest MSigDB version number."""
        soup = get_soup(URL)

        x = soup.find(text="Current Version")
        paragraph = x.parent.find_next_sibling("p")
        version = paragraph.text.strip().split()[2][len("v") : -len(".Hs")]
        return version


if __name__ == "__main__":
    MSigDBGetter.print()
