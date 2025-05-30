"""A getter for NPASS."""

from bioversions.utils import Getter, VersionType, find, get_soup

__all__ = [
    "NPASSGetter",
]

URL = "http://bidd.group/NPASS/"


class NPASSGetter(Getter):
    """A getter for NPASS."""

    bioregistry_id = "npass"
    name = "NPASS"
    version_type = VersionType.semver_minor

    def get(self) -> str:
        """Get the latest NPASS version number."""
        return "2.0"


def _dynamic_get() -> str:
    # this has been retired since the website is so slow and this
    # resource is effectively static
    soup = get_soup(URL)
    footer = find(soup, name="footer")
    ul = find(footer, name="ul")
    for li in ul.find_all(name="li"):
        if li.text.startswith("Version:"):
            return li.text[len("Version: ") :]
    raise ValueError(f"could not parse NPASS version from {URL}")


if __name__ == "__main__":
    NPASSGetter.print()
