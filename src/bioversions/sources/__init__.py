# -*- coding: utf-8 -*-

"""Sources for Bioversions."""

from typing import List, Mapping, Optional, Tuple, Type

from bioversions.sources.biogrid import BioGRIDGetter
from bioversions.sources.reactome import ReactomeGetter
from bioversions.utils import Bioversion, Getter, norm, refresh_daily

__all__ = [
    'getters',
    'getter_dict',
    'resolve',
    'get_rows',
]

# TODO replace with entrypoint lookup
getters = [
    BioGRIDGetter,
    ReactomeGetter,
]
getter_dict: Mapping[str, Type[Getter]] = {
    norm(getter.name): getter
    for getter in getters
}


@refresh_daily
def resolve(name: str) -> Bioversion:
    """Resolve the database name to a :class:`Bioversion` instance."""
    norm_name = norm(name)
    getter: Type[Getter] = getter_dict[norm_name]
    return getter.resolve()


@refresh_daily
def get_rows() -> List[Tuple[str, str, Optional[str]]]:
    """Get the rows, refreshing once per day."""
    rv = [
        (getter.name, getter.version, getter.homepage)
        for getter in getters
    ]
    # TODO sort?
    return rv
