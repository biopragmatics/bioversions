# -*- coding: utf-8 -*-

"""A getter for the Mouse Genome Database."""

from bioversions.utils import Getter, VersionType, get_soup

__all__ = [
    "MGIGetter",
]


HOMEPAGE = "https://www.informatics.jax.org/"


class MGIGetter(Getter):
    """A getter for MGI."""

    bioregistry_id = "mgi"
    name = "Mouse Genome Database"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest MGI version number."""
        soup = get_soup(HOMEPAGE)
        cells = soup.find_all("td")
        search_string = "MGI"
        for cell in cells:
            text = cell.text
            if text and text.strip().startswith("last database update"):
                idx = text.find(search_string)
                return text[idx + len(search_string) :].strip()
        raise ValueError


if __name__ == "__main__":
    MGIGetter.print()
