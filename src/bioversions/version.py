"""Version information for bioversions."""

import os
from subprocess import CalledProcessError, check_output

__all__ = [
    "VERSION",
]

VERSION = "0.5.562"


def get_git_hash() -> str:
    """Get the bioversions git hash."""
    with open(os.devnull, "w") as devnull:
        try:
            ret = check_output(
                ["git", "rev-parse", "HEAD"],
                cwd=os.path.dirname(__file__),
                stderr=devnull,
            )
        except CalledProcessError:
            return "UNHASHED"
        else:
            return ret.strip().decode("utf-8")[:8]
