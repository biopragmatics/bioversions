# -*- coding: utf-8 -*-

"""Get versions from the OLS."""

from typing import Iterable, Mapping, Optional, Type, Union

import bioregistry
from bioregistry.resolve import get_name, get_version

from bioversions.utils import Getter


def make_ols_getter(bioregistry_id: str) -> Optional[Type[Getter]]:
    """Make a getter from OLS."""
    version = get_version(bioregistry_id)
    if version is None:
        return

    _brid = bioregistry_id

    class OlsGetter(Getter):
        """A getter for OLS data from the Bioregistry."""

        bioregistry_id = _brid
        name = get_name(_brid)

        def get(self) -> Union[str, Mapping[str, str]]:
            """Get the version from the Bioregistry."""
            return version

    return OlsGetter


def iter_ols_getters() -> Iterable[Type[Getter]]:
    """Iterate over OLS getters."""
    for bioregistry_id, bioregistry_entry in bioregistry.read_bioregistry().items():
        if 'ols' not in bioregistry_entry:
            continue
        yv = make_ols_getter(bioregistry_id)
        if yv is not None:
            yield yv


def extend_ols_getters(getters):
    """Extend the getters, without adding duplicates."""
    for ols_getter in iter_ols_getters():
        if any(getter.bioregistry_id == ols_getter.bioregistry_id for getter in getters):
            continue
        getters.append(ols_getter)
