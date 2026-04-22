"""A getter for Ensembl."""

from bioversions.utils import Getter, VersionType, find_text, get_soup

__all__ = [
    "EnsemblGetter",
]

URL = "https://www.ensembl.org/index.html"


class EnsemblGetter(Getter):
    """A getter for Ensembl."""

    bioregistry_id = "ensembl"
    name = "Ensembl"
    homepage_fmt = "https://www.ensembl.org"
    date_fmt = "%B %Y"
    version_type = VersionType.sequential

    def get(self) -> dict[str, str]:
        """Get the latest Ensembl version number."""
        soup = get_soup(URL)
        text = find_text(soup, class_="box-header")
        version, date = text.rstrip(")").split("(", 1)
        return {"version": version.split()[-1], "date": date}


if __name__ == "__main__":
    EnsemblGetter.print()
