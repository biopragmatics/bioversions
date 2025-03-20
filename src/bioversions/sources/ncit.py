"""A getter for the NCI Thesaurus."""

import re

from ..utils import Getter, VersionType, get_soup

__all__ = [
    "NCItGetter",
]

URL = "https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/"
PATTERN = re.compile(r"ThesaurusInf_(\d+\.\d+[a-z]?)\.OWL\.zip")


class NCItGetter(Getter):
    """A getter for the NCI Thesaurus."""

    bioregistry_id = "ncit"
    name = "National Cancer Institute Thesaurus"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.other

    def get(self) -> dict[str, str]:
        """Get the latest NCIt version number."""
        soup = get_soup(URL)

        # We extract all versions along with dates
        versions_with_dates = []
        for row in soup.find_all("tr"):
            link = row.find("a", href=True)
            date_cell = row.find("td", class_="indexcollastmod")

            if link and date_cell:
                match = pattern.search(link["href"])
                if match:
                    version = match.group(1)
                    date = date_cell.text.strip().split(" ")[0]
                    versions_with_dates.append((version, date))

        # Sort to get the highest version
        latest_version, latest_date = max(
            versions_with_dates,
            key=lambda v: [int(v[0].split(".")[0]), float(v[0].split(".")[1][:-1])],
        )

        return {
            "version": latest_version,
            "date": latest_date,
        }


if __name__ == "__main__":
    NCItGetter.print()
