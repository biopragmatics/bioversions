# -*- coding: utf-8 -*-

"""A getter for BiGG."""

from datetime import datetime

import requests

from bioversions.utils import Getter, VersionType

__all__ = [
    "BiGGGetter",
]

URL = "http://bigg.ucsd.edu/api/v2/database_version"


class BiGGGetter(Getter):
    """A getter for BiGG."""

    name = "BiGG"
    version_type = VersionType.semver

    def get(self):
        """Get the latest BiGG version number."""
        res = requests.get(URL).json()
        date = datetime.fromisoformat(res["last_updated"])
        return dict(
            version=res["bigg_models_version"],
            date=date,
        )


if __name__ == "__main__":
    BiGGGetter.print()
