"""A getter for PomBase."""

from bioversions.utils import Getter, VersionType, find_soup_text, get_soup

__all__ = [
    "PombaseGetter",
]


class PombaseGetter(Getter):
    """A getter for PomBase."""

    bioregistry_id = "pombase"
    name = "PomBase"
    date_version_fmt = "%Y-%m-%d"
    homepage_fmt = "https://www.pombase.org/data/releases/pombase-{version}/"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest pombase version number."""
        soup = get_soup("https://www.pombase.org/data/releases/")
        tr = soup.find_all("tr")[-2]
        td = tr.find_all("td")[1]
        anchor_text = find_soup_text(td, "a")
        return anchor_text[len("pombase-") :].rstrip("/")


if __name__ == "__main__":
    PombaseGetter.print()
