"""A getter for WikiPathways."""

from bioversions.utils import Getter, VersionType

__all__ = [
    "WikiPathwaysGetter",
    "get_wikidata_version",
]

URL = "http://data.wikipathways.org/current/gmt/"


def get_wikidata_version() -> str:
    """Get the latest WikiPathways version number."""
    from pystow.utils import get_soup

    soup = get_soup(URL)
    if soup is None:
        raise ValueError(f"could not get WikiPathways data from {URL}")
    anchor = soup.find(id="File")
    if anchor is None or not isinstance(anchor.text, str):
        raise ValueError(f"could could not parse WikiPathways data from {URL}")
    return anchor.text.split("-")[1]


class WikiPathwaysGetter(Getter):
    """A getter for WikiPathways."""

    bioregistry_id = "wikipathways"
    name = "WikiPathways"
    homepage_fmt = "http://data.wikipathways.org/{version}/"
    date_version_fmt = "%Y%m%d"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest WikiPathways version number."""
        return get_wikidata_version()


if __name__ == "__main__":
    WikiPathwaysGetter.print()
