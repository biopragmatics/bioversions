# -*- coding: utf-8 -*-

"""A getter for PomBase."""

from bioversions.utils import Getter, VersionType, get_soup

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

    def get(self):
        """Get the latest pombase version number."""
        soup = get_soup("https://www.pombase.org/data/releases/")
        tr = soup.find_all("tr")[-2]
        text = tr.find_all("td")[1]
        anchor = text.find("a")
        text = anchor.text
        return text[len("pombase-") :].rstrip("/")


if __name__ == "__main__":
    PombaseGetter.print()
