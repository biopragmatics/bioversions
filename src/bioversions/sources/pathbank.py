"""A getter for PathBank."""

from bioversions.utils import Getter, VersionType, find, get_soup

__all__ = [
    "PathBankGetter",
]

URL = "https://pathbank.org/"


class PathBankGetter(Getter):
    """A getter for PathBank."""

    bioregistry_id = "pathbank"
    name = "PathBank"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest PathBank version number."""
        soup = get_soup(URL)
        main = find(soup, id="main")
        footer = find(main, name="footer")
        clear = find(footer, **{"class": "wishart-clear"})
        strong = find(clear, name="strong")
        return strong.text


if __name__ == "__main__":
    PathBankGetter.print()
