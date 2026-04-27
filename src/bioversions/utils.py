"""Utilities and implementation for bioversions."""

from __future__ import annotations

import datetime
import enum
import gzip
import io
import os
from collections.abc import Generator, Iterable, Mapping
from contextlib import contextmanager
from typing import Any, ClassVar, TextIO, TypedDict, cast

import bioregistry
import pydantic
import pystow.utils
import requests
import requests.exceptions
from bs4 import BeautifulSoup, Tag
from pystow.constants import TimeoutHint
from typing_extensions import NotRequired

from .version import VERSION

__all__ = [
    "BIOVERSIONS_USER_AGENT",
    "DailyGetter",
    "Getter",
    "MetaGetter",
    "OBOFoundryGetter",
    "ReleaseDict",
    "UnversionedGetter",
    "VersionResult",
    "VersionType",
    "find",
    "find_text",
    "get_obo_version",
    "get_obograph_json_version",
    "get_owl_xml_version",
    "get_soup",
    "requests_get",
]

BIOVERSIONS_HOME = pystow.join("bioversions")
HERE = os.path.abspath(os.path.dirname(__file__))
DOCS = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, "docs"))
IMG = os.path.join(DOCS, "img")

BIOVERSIONS_USER_AGENT = f"bioversions v{VERSION}"


def get_soup(
    url: str,
    *,
    verify: bool = True,
    timeout: TimeoutHint | None = None,
    user_agent: str | None = None,
) -> BeautifulSoup:
    """Wrap getting soup with the user agent."""
    if user_agent is None:
        user_agent = BIOVERSIONS_USER_AGENT
    return pystow.utils.get_soup(url, verify=verify, timeout=timeout, user_agent=user_agent)


def requests_get(url: str, *args: Any, timeout: int | float, **kwargs: Any) -> requests.Response:
    """Wrap :func:`requests.get` that automatically adds a User-Agent."""
    if "headers" not in kwargs:
        kwargs["headers"] = {}
    if "User-Agent" not in kwargs["headers"]:
        kwargs["headers"]["User-Agent"] = BIOVERSIONS_USER_AGENT
    res = requests.get(
        url,
        *args,
        timeout=timeout,
        **kwargs,
    )
    return res


class VersionType(str, enum.Enum):
    """Different types of versions."""

    semver = "semver"
    date = "date"
    month = "month"
    year = "year"
    year_minor = "year_minor"
    semver_minor = "semver_minor"
    sequential = "sequential"
    daily = "daily"
    unversioned = "unversioned"
    other = "other"
    missing = "missing"
    static = "static"
    #: Saved for the most shameful of data
    garbage = "garbage"

    @property
    def label(self) -> str:  # noqa:C901
        """Get the human-readable label."""
        match self:
            case self.semver:
                return "SemVer (X.Y.Z)"
            case self.date:
                return "CalVer (YYYY-MM-DD)"
            case self.month:
                return "CalVer (YYYY-MM)"
            case self.year:
                return "CalVer (YYYY)"
            case self.year_minor:
                return "CalVer (YYYY.X)"
            case self.semver_minor:
                return "SemVer (X.Y)"
            case self.sequential:
                return "Sequential (X)"
            case self.daily:
                return "Daily"
            case self.unversioned:
                return "Unversioned"
            case self.other:
                return "Other"
            case self.missing:
                return "Missing"
            case self.static:
                return "Static"
            #: Saved for the most shameful of data
            case self.garbage:
                return "Garbage"


def find(element: Tag, *args: Any, **kwargs: Any) -> Tag:
    """Find a sub-element."""
    tag = element.find(*args, **kwargs)
    if not isinstance(tag, Tag):
        raise ValueError(f"could not find an element matching {args=} and {kwargs=}")
    return tag


def find_text(element: Tag, *args: Any, **kwargs: Any) -> str:
    """Find a sub-element."""
    tag = find(element, *args, **kwargs)
    if not isinstance(tag.text, str) or not tag.text:
        raise ValueError
    return tag.text


class MetaGetter(type):
    """A metatype to expose two class properties."""

    _cache: ClassVar[str | ReleaseDict | datetime.datetime | datetime.date | None] = None

    date_fmt: str | None
    date_version_fmt: str | None
    homepage_fmt: str | None

    @property
    def _cache_prop(cls) -> str | ReleaseDict | datetime.datetime | datetime.date:
        if cls._cache is None:
            cls._cache = cls().get()  # type:ignore
        return cls._cache

    @property
    def version(cls) -> str:
        """Get the version of the getter based on the inheriting class's implementation."""
        if isinstance(cls._cache_prop, str):
            return cls._cache_prop
        elif isinstance(cls._cache_prop, dict):
            return cls._cache_prop["version"]
        elif isinstance(cls._cache_prop, datetime.datetime | datetime.date):
            return cls._cache_prop.strftime("%Y-%m-%d")
        else:
            raise TypeError(f"_cache_prop was a {type(cls._cache_prop)}")

    @property
    def date(cls) -> datetime.date | None:
        """Get the date if it's set."""
        vp = cls.version_date_parsed
        if vp is not None:
            return vp
        if not isinstance(cls._cache_prop, dict):
            return None
        date = cls._cache_prop["date"]
        if isinstance(date, datetime.datetime):
            return date.date()
        elif isinstance(date, datetime.date):
            return date
        if not cls.date_fmt:
            raise TypeError(
                f"Need to set {cls.__name__} class variable `date_fmt` to parse date {date}"
            )
        try:
            return datetime.datetime.strptime(date, cls.date_fmt).date()
        except ValueError:
            raise ValueError(
                f"Issue in {cls.__name__} with date {date} and fmt {cls.date_fmt}"
            ) from None

    @property
    def version_date_parsed(cls) -> datetime.date | None:
        """Get the date as a parsed class there's a format string."""
        if cls.date_version_fmt is None:
            return None
        try:
            return datetime.datetime.strptime(cls.version, cls.date_version_fmt).date()
        except ValueError:
            raise ValueError(
                f"Issue parsing {cls.__name__} version {cls.version} "
                f"with fmt {cls.date_version_fmt}"
            ) from None

    @property
    def homepage(cls) -> str | None:
        """Get the homepage's URL if a format string was specified."""
        if cls.homepage_fmt is None:
            return None

        version = cls.homepage_version_transform(cls.version)
        return cls.homepage_fmt.format(version=version)

    @staticmethod
    def homepage_version_transform(version: str) -> str:
        """Transform the version for formatting into the homepage."""
        return version


class VersionResult(pydantic.BaseModel):
    """A dataclass for information about a database and version."""

    #: The database name
    name: str
    #: The database current version
    version: str
    #: The class that retrieved the version
    classname: str
    #: The version type
    vtype: VersionType
    #: The date of the current release
    date: datetime.date | None
    #: The URL for the homepage of the specific version of the database
    homepage: str | None
    #: The database prefix
    bioregistry_id: str | None


class ReleaseDict(TypedDict):
    """A release dict."""

    version: str
    date: NotRequired[str | datetime.datetime | datetime.date]


class Getter(metaclass=MetaGetter):
    """A class for holding the name of a database and implementation of the version getter."""

    #: The name of the database. Specify this in the inheriting class!.
    name: ClassVar[str]
    #: The type of version string. Required!
    version_type: ClassVar[VersionType]

    #: The URL with `{version}` to format in the version. Specify this in the inheriting class.
    homepage_fmt: ClassVar[str | None] = None

    date_fmt: ClassVar[str | None] = None

    date_version_fmt: ClassVar[str | None] = None

    bioregistry_id: ClassVar[str | None] = None

    # The following are automatically calculated based on the metaclass
    version: ClassVar[str]
    date: ClassVar[str]
    homepage: ClassVar[str]

    #: Prefixes this getter works for
    collection: ClassVar[list[str] | None] = None

    def get(self) -> str | ReleaseDict | datetime.datetime | datetime.date:
        """Get the latest of this database."""
        raise NotImplementedError

    @classmethod
    def print(cls, sep: str = "\t", file: TextIO | None = None) -> None:
        """Print the latest version of this database."""
        x = []
        if cls.bioregistry_id:
            x.append(cls.bioregistry_id)
        elif cls.collection:
            x.append("/".join(cls.collection))
        else:
            x.append("<no prefix>")
        x.append(cls.name)
        x.append(cls.version)
        if cls.date:
            x.append(f"({cls.date})")
        if cls.homepage:
            x.append(cls.homepage)
        print(*x, sep=sep, file=file)

    @classmethod
    def resolve(cls) -> VersionResult:
        """Get a Bioversion data container with the data for this database."""
        return VersionResult(
            name=cls.name,
            version=cls.version,
            classname=cls.__name__,
            vtype=cls.version_type,
            homepage=cls.homepage,
            date=cls.date,
            bioregistry_id=cls.bioregistry_id,
        )

    @classmethod
    def to_dict(cls) -> Mapping[str, Any]:
        """Get a dict with the data for this database."""
        return cls.resolve().model_dump()


class DailyGetter(Getter):
    """A base getter for daily updated resources."""

    version_type = VersionType.daily

    def get(self) -> str:
        """Return a constant "daily" string."""
        return "daily"


class UnversionedGetter(Getter):
    """A base getter for unversioned resources."""

    version_type = VersionType.unversioned

    #: Has this database been apparently abandoned (true) or is it still updated (false)
    abandoned: ClassVar[bool]

    def get(self) -> str:
        """Return a constant unversioned string."""
        return "unversioned"


def get_obo_version(url: str, *, max_lines: int = 200) -> str | None:
    """Get the data version from an OBO file."""
    with _iterate_lines(url) as file:
        for i, line in enumerate(file):
            if isinstance(line, bytes):
                line = line.decode("utf-8")
            line = line.strip()
            if line.startswith("data-version"):
                return line[len("data-version:") :].strip()
            if not line:
                # this means we got past the exposition section
                return None
            if i > max_lines:
                # this might happen if there are tons of axioms
                # shoved into OBO, but this always comes at the end
                return None
    return None


class OBOFoundryGetter(Getter):
    """An implementation for getting OBO Foundry ontology versions."""

    strip_key_prefix: ClassVar[bool] = False
    strip_version_prefix: ClassVar[bool] = False
    strip_file_suffix: ClassVar[bool] = False

    @property
    def key(self) -> str:
        """Get the OBO Foundry key."""
        if self.bioregistry_id is None:
            raise ValueError("missing bioregistry ID")
        rv = bioregistry.get_obofoundry_prefix(self.bioregistry_id)
        if rv is None:
            raise ValueError
        return rv

    def get(self) -> str:
        """Get the OBO version."""
        url = f"https://purl.obolibrary.org/obo/{self.key}.obo"
        version = get_obo_version(url)
        if version is None:
            raise ValueError(f"No `data-version` line contained in {url}")
        return self.process(version)

    def process(self, version: str) -> str:
        """Post-process the version string."""
        if self.strip_key_prefix:
            version = version[len(f"{self.key}/") :]
        if self.strip_version_prefix:
            version = version[len("releases/") :]
        if self.strip_file_suffix:
            version = version[: -(len(self.key) + 5)]
        return version


def _get_ftp_date_version(host: str, directory: str) -> str:
    url = f"https://{host}/{directory}"
    soup = get_soup(url)
    return max(
        text
        for anchor in soup.find_all("a")
        if isinstance(anchor.text, str)
        and anchor.text
        and _is_iso_8601(text := anchor.text.rstrip("/"))
    )


def _is_iso_8601(s: str) -> bool:
    x = s.split("-")
    return len(x) == 3 and x[0].isnumeric() and x[1].isnumeric() and x[2].isnumeric()


def _is_version(s: str) -> bool:
    x = s.split(".")
    return len(x) == 2 and x[0].isnumeric() and x[1].isnumeric()


def _is_semantic_version(s: str) -> bool:
    x = s.split(".")
    return len(x) == 3 and x[0].isnumeric() and x[1].isnumeric() and x[2].isnumeric()


VERSION_IRI_TAG = "<owl:versionIRI rdf:resource="
VERSION_IRI_TAG_LEN = len(VERSION_IRI_TAG)


def get_owl_xml_version(url: str, *, max_lines: int = 200) -> str | None:
    """Get version from an OWL XML document."""
    try:
        with _iterate_lines(url) as file:
            for i, line in enumerate(file):
                if isinstance(line, bytes):
                    line = line.decode("utf-8")
                line = line.strip()
                if line.startswith(VERSION_IRI_TAG):
                    return line[VERSION_IRI_TAG_LEN:].removesuffix("/>")
                if i > max_lines:
                    return None
    except requests.exceptions.SSLError:
        pass
    return None


@contextmanager
def _iterate_lines(url: str) -> Generator[Iterable[str], None, None]:
    with requests.get(
        url, stream=True, timeout=60, headers={"User-Agent": BIOVERSIONS_USER_AGENT}
    ) as res:
        if url.endswith(".gz"):
            compressed_stream = io.BufferedReader(res.raw)  # type:ignore
            with gzip.open(compressed_stream, "rt", encoding="utf-8") as file:
                yield file
        else:
            yield res.iter_lines(decode_unicode=True)


def get_obograph_json_version(url: str) -> str | None:
    """Get version from an OBO Graph JSON document."""
    res = requests_get(url, timeout=60).json()
    version = res["graphs"][0]["meta"]["version"]
    return cast(str, version)
