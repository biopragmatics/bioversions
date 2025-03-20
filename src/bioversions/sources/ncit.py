"""A getter for the NCI Thesaurus."""

import requests

from ..utils import Getter, VersionType

__all__ = [
    "NCItGetter",
]

URL = "https://evsexplore.semantics.cancer.gov/evsexplore/api/v1/metadata/terminologies"


class NCItGetter(Getter):
    """A getter for the NCI Thesaurus."""

    bioregistry_id = "ncit"
    name = "National Cancer Institute Thesaurus"
    date_fmt = "%B %d, %Y"
    version_type = VersionType.other

    def get(self) -> dict[str, str]:
        """Get the latest NCIt version number."""
        records = requests.get(URL, timeout=5).json()
        ncit_record = next(record for record in records if record["terminology"] == "ncit")
        return {
            "version": ncit_record["version"],
            "date": ncit_record["date"],
        }


if __name__ == "__main__":
    NCItGetter.print()
