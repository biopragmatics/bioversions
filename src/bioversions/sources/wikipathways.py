"""A getter for WikiPathways."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "WikiPathwaysGetter",
]

URL = "http://data.wikipathways.org/current/gmt/"


class WikiPathwaysGetter(Getter):
    """A getter for WikiPathways."""

    bioregistry_id = "wikipathways"
    name = "WikiPathways"
    homepage_fmt = "http://data.wikipathways.org/{version}/"
    date_version_fmt = "%Y%m%d"
    version_type = VersionType.date

    def get(self):
        """Get the latest WikiPathways version number."""
        soup = get_soup(URL)
        if soup is None:
            raise ValueError(f"could not get WikiPathways data from {URL}")
        anchor = soup.find(id="File")
        return anchor.text.split("-")[1]


if __name__ == "__main__":
    WikiPathwaysGetter.print()
