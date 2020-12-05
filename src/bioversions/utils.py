# -*- coding: utf-8 -*-

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
    return s.lower().replace(' ', '').replace('-', '').replace('.', '')


def get_soup(url: str) -> BeautifulSoup:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    return soup


class classproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)


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
        return cls().get()

    @property
    def homepage(cls) -> Optional[str]:
        if cls.homepage_fmt:
            return cls.homepage_fmt.format(version=cls.version)


@dataclass_json
@dataclass
class Bioversion:
    name: str
    version: str
    homepage: Optional[str]


class Getter(metaclass=MetaGetter):
    name: ClassVar[str]
    homepage_fmt: ClassVar[Optional[str]] = None

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
        return Bioversion(
            name=cls.name,
            version=cls.version,
            homepage=cls.homepage,
        )

    @classmethod
    def to_dict(cls) -> Mapping[str, Any]:
        return cls.resolve().to_dict()
