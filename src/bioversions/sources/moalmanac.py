"""A getter for the Molecular Oncology Almanac."""

from ..utils import Getter, VersionType, find, get_soup

__all__ = [
    "MOAlmanacGetter",
]


class MOAlmanacGetter(Getter):
    """A getter for MOAlmanac."""

    name = "Molecular Oncology Almanac"
    homepage_fmt = "https://github.com/vanallenlab/moalmanac-db/releases/tag/v.{version}"
    date_version_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> str:
        """Get the latest MOAlmanac version number."""
        soup = get_soup("https://moalmanac.org/")
        sub_footer = find(soup, "div", {"class": "text-right"})
        anchor = find(sub_footer, "a")
        version = anchor.text.strip("v").strip(".")
        return version


if __name__ == "__main__":
    MOAlmanacGetter.print()
