# -*- coding: utf-8 -*-

"""Get versions from the OLS."""

import logging
from typing import Iterable, List, Mapping, Optional, Type, Union

import bioregistry
from bioregistry.data import get_ols_processing
from bioregistry.resolve import get_name

from bioversions.utils import Getter, VersionType

logger = logging.getLogger(__name__)

ols_processing = get_ols_processing()


def _get_version_type(bioregistry_id: str) -> Optional[VersionType]:
    ols_id = bioregistry.get_ols_prefix(bioregistry_id)
    ols_config = ols_processing.get(ols_id)
    if ols_config is None:
        raise

    ols_version_type = ols_config.version_type
    ols_version_date_format = ols_config.version_date_format
    if ols_version_date_format:
        return VersionType.date
    elif ols_version_type:
        return getattr(VersionType, ols_version_type)
    else:
        logger.warning("[%s] missing version type", bioregistry_id)


def make_ols_getter(bioregistry_id: str) -> Optional[Type[Getter]]:
    """Make a getter from OLS."""
    ols_id = bioregistry.get_ols_prefix(bioregistry_id)
    if ols_id is None:
        return

    version = bioregistry.get(bioregistry_id).ols.get("version")
    if version is None:
        logger.debug("[%s] no OLS version", bioregistry_id)
        return

    _brid = bioregistry_id

    class OlsGetter(Getter):
        """A getter for OLS data from the Bioregistry."""

        bioregistry_id = _brid
        name = get_name(_brid)
        version_type = _get_version_type(bioregistry_id)

        def get(self) -> Union[str, Mapping[str, str]]:
            """Get the version from the Bioregistry."""
            return version

    return OlsGetter


def iter_ols_getters() -> Iterable[Type[Getter]]:
    """Iterate over OLS getters."""
    for bioregistry_id in bioregistry.read_registry():
        yv = make_ols_getter(bioregistry_id)
        if yv is not None:
            yield yv


def extend_ols_getters(getters: List[Type[Getter]]) -> None:
    """Extend the getters, without adding duplicates."""
    for ols_getter in iter_ols_getters():
        if any(getter.bioregistry_id == ols_getter.bioregistry_id for getter in getters):
            continue
        getters.append(ols_getter)


if __name__ == "__main__":
    list(iter_ols_getters())
