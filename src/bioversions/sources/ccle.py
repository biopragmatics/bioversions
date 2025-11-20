"""A getter for CCLE."""

from bioversions.utils import Getter, VersionType

__all__ = [
    "CCLEGetter",
]


class CCLEGetter(Getter):
    """A getter for CCLE."""

    bioregistry_id = "ccle"
    version_type = VersionType.static
    name = "Cancer Cell Line Encylopedia"
    date_fmt = "%Y"

    def get(self):
        """Get the CCLE version number."""
        return {"version": "2019", "date": "2019"}


if __name__ == "__main__":
    CCLEGetter.print()
