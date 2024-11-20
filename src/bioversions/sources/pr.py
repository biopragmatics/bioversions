"""A getter for the Protein Ontology."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "PRGetter",
]

URL = "https://proconsortium.org/cgi-bin/sta_pro"


class PRGetter(Getter):
    """A getter for the Protein Ontology."""

    bioregistry_id = "pr"
    name = "Protein Ontology"
    version_type = VersionType.semver_minor
    date_fmt = "%m/%d/%Y"
    homepage_fmt = "https://ftp.ebi.ac.uk/pub/databases/chebi/archive/rel{version}/"

    def get(self):
        """Get the latest Protein Ontology version number."""
        soup = get_soup(URL)
        rows = soup.find("table", **{"class": "nrm11"}).find_all("tr")
        row = list(rows)[2]
        version_cell, date_cell, *_ = list(row.find_all("td"))
        return {"version": version_cell.text.strip(), "date": date_cell.text.strip()}


if __name__ == "__main__":
    PRGetter.print()
