"""A getter for WikiPathways."""

from bioversions.utils import Getter, VersionType, find_text, get_soup

__all__ = [
    "WikiPathwaysGetter",
    "get_wikidata_version",
]

URL = "http://data.wikipathways.org/current/gmt/"


def get_wikidata_version() -> str:
    """Get the latest WikiPathways version number."""
    soup = get_soup(URL)
    if soup is None:
        raise ValueError(f"could not get WikiPathways data from {URL}")
    text = find_text(soup, id="File")
    return text.split("-")[1]


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
