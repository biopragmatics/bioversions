"""Get the version for CiVIC."""

import datetime
from typing import ClassVar

import requests

from bioversions.utils import Getter, VersionType

URL = "https://civicdb.org/releases/main"
API = "https://civicdb.org/api/graphql"
GRAPHQL_QUERY = """\
query DataReleases {
  dataReleases {
    name
  }
}
"""

# see https://griffithlab.github.io/civic-v2/#query-dataReleases
# and https://griffithlab.github.io/civic-v2/#definition-DownloadableFile


class CiVICGetter(Getter):
    """A getter for CiVIC."""

    name = "CiVIC"
    date_fmt = "%d-%b-%Y"
    version_type = VersionType.date
    homepage = "https://civicdb.org"
    collection: ClassVar[list[str]] = ["civic.gid", "civic.eid"]

    def get(self) -> datetime.datetime:
        """Get the latest ChEMBL version number."""
        res = requests.post(API, json={"query": GRAPHQL_QUERY}, timeout=15)
        # 0 element is always nightly, 1 is latest
        value = res.json()["data"]["dataReleases"][1]["name"]
        return datetime.datetime.strptime(value, "%d-%b-%Y")


if __name__ == "__main__":
    CiVICGetter.print()
