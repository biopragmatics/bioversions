"""A getter for LOINC."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = ["LOINCGetter"]


class LOINCGetter(Getter):
    """A getter for LOINC."""

    bioregistry_id = "loinc"
    name = "Logical Observation Identifiers Names and Codes"
    version_type = VersionType.semver_minor
    date_fmt = "%Y-%m-%d"

    def get(self) -> dict[str, str]:
        """Get the latest LOINC version number."""
        soup = get_soup("https://loinc.org")
        current_version_div = soup.find(id="current-version")
        if current_version_div is None:
            raise ValueError

        h3 = current_version_div.find("h3")
        if h3 is None or not h3.text:
            raise ValueError

        version = h3.text.removeprefix("LOINC Version ")

        paragraph = current_version_div.find("p")
        if paragraph is None or not paragraph.text:
            raise ValueError

        date = paragraph.text.split("Released ")[1].strip()
        return {"version": version, "date": date}


if __name__ == "__main__":
    LOINCGetter.print()
