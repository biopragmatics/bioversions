"""A getter for ChEBI."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "ChEBIGetter",
]

URL = "https://ftp.ebi.ac.uk/pub/databases/chebi/archive/"


class ChEBIGetter(Getter):
    """A getter for ChEBI."""

    bioregistry_id = "chebi"
    name = "ChEBI"
    version_type = VersionType.sequential
    date_fmt = "%Y-%m-%d"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/chebi/archive/rel{version}/"

    def get(self):
        """Get the latest ChEBI version number."""
        soup = get_soup(URL)

        versions = []
        for row in soup.find_all("tr"):
            row = list(row)
            if len(row) < 3:
                continue
            anchor = row[1].find("a")
            if anchor is None:
                continue
            version = anchor.attrs["href"].removeprefix("rel").rstrip("/")
            if not version.isnumeric():
                continue
            if not row[2].text:
                continue
            versions.append(
                (
                    version,
                    row[2].text.split()[0],
                )
            )

        version, date = versions[-1]
        return {"version": version, "date": date}


if __name__ == "__main__":
    ChEBIGetter.print()
