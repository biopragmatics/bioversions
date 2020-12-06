# -*- coding: utf-8 -*-

"""Utilities and implementation for bioversions."""

from dataclasses import dataclass
from datetime import timedelta
from typing import Any, ClassVar, Mapping, Optional

import pystow
import requests
from bs4 import BeautifulSoup
from cachier import cachier
from dataclasses_json import dataclass_json

BIOVERSIONS_HOME = pystow.get('bioversions')


def norm(s: str) -> str:
    """Normalize a string for dictionary lookup."""
    return s.lower().replace(' ', '').replace('-', '').replace('.', '')


def get_soup(url: str) -> BeautifulSoup:
    """Get a beautiful soup parsed version of the given web page."""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    return soup


#: A decorator for functions whose return values
#: should be cached and refreshed once per day
refresh_daily = cachier(
    stale_after=timedelta(days=1),
    backend='pickle',
    cache_dir=BIOVERSIONS_HOME,
)


class MetaGetter(type):
    """A metatype to expose two class properties."""

    @property
    def version(cls) -> str:
        """Get the version of the getter based on the inheriting class's implementation."""
        return cls().get()

    @property
    def homepage(cls) -> Optional[str]:
        """Get the homepage's URL if a format string was specified."""
        if cls.homepage_fmt:
            return cls.homepage_fmt.format(version=cls.version)


@dataclass_json
@dataclass
class Bioversion:
    """A dataclass for information about a database and version."""

    #: The database name
    name: str
    #: The database current version
    version: str
    #: The URL for the homepage of the specific version of the database
    homepage: Optional[str]


class Getter(metaclass=MetaGetter):
    """A class for holding the name of a database and implementation of the version getter."""

    #: The name of the database. Specify this in the inheriting class!.
    name: ClassVar[str]
    #: The URL with `{version}` to format in the version. Specify this in the inheriting class.
    homepage_fmt: ClassVar[Optional[str]] = None

    # The following two are automatically calculated based on the metaclass
    version: ClassVar[str]
    homepage: ClassVar[str]

    def get(self) -> str:
        """Get the latest of this database."""
        raise NotImplementedError

    @classmethod
    def print(cls, file=None):
        """Print the latest version of this database."""
        print(cls.version, file=file)

    @classmethod
    def resolve(cls) -> Bioversion:
        """Get a Bioversion data container with the data for this database."""
        return Bioversion(
            name=cls.name,
            version=cls.version,
            homepage=cls.homepage,
        )

    @classmethod
    def to_dict(cls) -> Mapping[str, Any]:
        """Get a dict with the data for this database."""
        return cls.resolve().to_dict()
