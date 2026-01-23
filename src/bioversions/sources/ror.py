"""A getter for ROR."""

from bioversions.utils import Getter, VersionType

__all__ = [
    "RORGetter",
]


class RORGetter(Getter):
    """A getter for ROR."""

    bioregistry_id = "ror"
    name = "Research Organization Registry"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> dict[str, str]:
        """Get the latest ROR version."""
        import ror_downloader

        version_info = ror_downloader.get_version_info(download=False)
        return {"version": version_info.version, "date": version_info.date.isoformat()}


if __name__ == "__main__":
    RORGetter.print()
