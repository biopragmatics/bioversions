"""A getter for SGD."""

from itertools import islice
from operator import itemgetter

from bioversions.utils import Getter, ReleaseDict, VersionType, requests_get

__all__ = [
    "SgdGetter",
]

VERSION_FILE = (
    "http://sgd-archive.yeastgenome.org/sequence/S288C_reference/dates_of_genome_releases.tab"
)


class SgdGetter(Getter):
    """A getter for SGD."""

    bioregistry_id = "sgd"
    name = "Saccharomyces Genome Database"
    date_fmt = "%Y-%m-%d"
    version_type = VersionType.date

    def get(self) -> ReleaseDict:
        """Get the latest SGD version number."""
        version_to_date: dict[str, str] = {}
        with requests_get(VERSION_FILE, stream=True, timeout=5) as res:
            for line_bytes in islice(res.iter_lines(decode_unicode=True), 3, None):
                version, date, *_ = line_bytes.decode("utf-8").strip().split()
                # Some lines contain extra information
                version_to_date[version] = date.replace("_", "-")
        max_version, max_date = max(version_to_date.items(), key=itemgetter(1))
        return {"version": max_version, "date": max_date}


if __name__ == "__main__":
    SgdGetter.print()
