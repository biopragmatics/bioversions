"""A getter for InterPro."""

import re

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "InterProGetter",
]

SOLVE_RE = re.compile(r"(\d)(st|nd|rd|th)")


class InterProGetter(Getter):
    """A getter for InterPro."""

    bioregistry_id = "interpro"
    name = "InterPro"
    homepage_fmt = "ftp://ftp.ebi.ac.uk/pub/databases/interpro/{version}/"
    date_fmt = "%d %B %Y"
    version_type = VersionType.semver_minor

    def get(self):
        """Get the latest InterPro version number."""
        with requests.Session() as session:
            res = session.get(
                "https://ftp.ebi.ac.uk/pub/databases/interpro/current_release/release_notes.txt"
            )
            for line in res.iter_lines():
                line = line.decode("utf8").strip()
                if line.startswith("Release") and not line.startswith("Release Notes"):
                    line = line[len("Release ") :]
                    version, rest = line.split(",", 1)
                    return {"version": version, "date": _process_line(rest)}
        raise ValueError


def _process_line(s: str) -> str:
    return SOLVE_RE.sub(r"\1", s.strip())


if __name__ == "__main__":
    InterProGetter.print()
