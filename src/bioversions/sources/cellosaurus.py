"""A getter for Cellosaurus."""

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "CellosaurusGetter",
]

URL = "https://ftp.expasy.org/databases/cellosaurus/cellosaurus.obo"


class CellosaurusGetter(Getter):
    """A getter for Cellosaurus."""

    bioregistry_id = "cellosaurus"
    name = "Cellosaurus"
    version_type = VersionType.sequential
    date_fmt = "%m:%d:%Y %H:%M"

    #   12:15:2022 12:00
    def get(self):
        """Get the latest Cellosaurus version number."""
        res = requests.get(URL, stream=True, timeout=15)
        data = {}
        for line in res.iter_lines(decode_unicode=True):
            line = line.strip().decode("utf8")
            if not line:
                break
            key, value = (part.strip() for part in line.split(":", 1))
            data[key] = value
        return {"version": data["data-version"], "date": data["date"]}


if __name__ == "__main__":
    CellosaurusGetter.print()
