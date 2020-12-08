# -*- coding: utf-8 -*-

"""Sources for Bioversions."""

from typing import List, Mapping, Optional, Tuple, Type

from .biogrid import BioGRIDGetter
from .obo import ChebiGetter, DoidGetter, GoGetter, PrGetter, XaoGetter
from .reactome import ReactomeGetter
from ..utils import Bioversion, Getter, norm, refresh_daily

__all__ = [
    'getters',
    'getter_dict',
    'resolve',
    'get_rows',
    'get_version',
]

# TODO replace with entrypoint lookup
getters = [
    BioGRIDGetter,
    ReactomeGetter,
    ChebiGetter,
    PrGetter,
    DoidGetter,
    GoGetter,
    XaoGetter,
]

getter_dict: Mapping[str, Type[Getter]] = {
    norm(getter.name): getter
    for getter in getters
}


def resolve(name: str, use_cache: bool = True) -> Bioversion:
    """Resolve the database name to a :class:`Bioversion` instance."""
    if use_cache:
        return _resolve_helper_cached(name)
    else:
        return _resolve_helper(name)


@refresh_daily
def _resolve_helper_cached(name: str) -> Bioversion:
    return _resolve_helper(name)


def _resolve_helper(name: str) -> Bioversion:
    norm_name = norm(name)
    getter: Type[Getter] = getter_dict[norm_name]
    return getter.resolve()


def get_version(name: str) -> str:
    """Resolve a database name to its version string."""
    return resolve(name).version


def get_rows() -> List[Tuple[str, str, Optional[str]]]:
    """Get the rows, refreshing once per day."""
    return list(_iter_rows())


def _iter_rows():
    for name in getter_dict:
        bv = resolve(name)
        yield bv.name, bv.version, bv.homepage
