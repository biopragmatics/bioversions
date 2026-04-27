"""A getter for PathBank."""

from bioversions.utils import Getter, VersionType, find_soup_tag, find_soup_text, get_soup

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
        main = find_soup_tag(soup, id="main")
        footer = find_soup_tag(main, name="footer")
        clear = find_soup_tag(footer, class_="wishart-clear")
        strong = find_soup_text(clear, name="strong")
        return strong


if __name__ == "__main__":
    PathBankGetter.print()
