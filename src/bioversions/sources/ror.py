"""A getter for ROR."""

from bioversions.utils import Getter, ReleaseDict, VersionType

__all__ = [
    "RORGetter",
]


class RORGetter(Getter):
    """A getter for ROR."""

    bioregistry_id = "ror"
    name = "Research Organization Registry"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> ReleaseDict:
        """Get the latest ROR version."""
        import ror_downloader
        from ror_downloader.api import VersionInfoShort

        version_info: VersionInfoShort = ror_downloader.get_version_info(download=False)
        rv: ReleaseDict = {"version": version_info.version}
        if version_info.date is not None:
            rv["date"] = version_info.date.isoformat()
        return rv


if __name__ == "__main__":
    RORGetter.print()
