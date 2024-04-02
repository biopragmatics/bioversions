"""Get the version for CiVIC."""

import requests

from bioversions.utils import Getter, VersionType

URL = "https://civicdb.org/releases/main"
API = "https://civicdb.org/api/graphql"
GRAPHQL_QUERY = """\
query dataReleases {
  dataReleases {
    geneTsv {
      filename
      path
    }
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
    collection = ["civic.gid", "civic.eid"]

    def get(self):
        """Get the latest ChEMBL version number."""
        res = requests.post(API, json={"query": GRAPHQL_QUERY})
        # 0 element is always nightly, 1 is latest
        return res.json()["data"]["dataReleases"][1]["name"]


if __name__ == "__main__":
    CiVICGetter.print()
