# -*- coding: utf-8 -*-

"""Get versions from the OLS."""

import logging
from typing import Iterable, Mapping, Optional, Type, Union

import bioregistry
from bioregistry.external.ols import get_ols
from bioregistry.resolve import _clean_version, get_name

from bioversions.utils import Getter, VersionType

logger = logging.getLogger(__name__)

bioregistry_id_to_ols_id = {
    bioregistry_id: bioregistry_entry['ols']['prefix']
    for bioregistry_id, bioregistry_entry in bioregistry.read_bioregistry().items()
    if 'ols' in bioregistry_entry
}


def _get_version_type(bioregistry_id) -> Optional[VersionType]:
    ols_entry = bioregistry.get(bioregistry_id)
    ols_version_type = ols_entry.get('ols_version_type')
    ols_version_date_format = ols_entry.get('ols_version_date_format')
    if ols_version_date_format:
        return VersionType.date
    elif ols_version_type:
        return getattr(VersionType, ols_version_type)
    else:
        logger.warning('[%s] missing version type', bioregistry_id)


def make_ols_getter(ols, bioregistry_id: str) -> Optional[Type[Getter]]:
    """Make a getter from OLS."""
    ols_id = bioregistry_id_to_ols_id.get(bioregistry_id)
    if ols_id is None:
        logger.warning('[%s] no OLS id', bioregistry_id)
        return

    version = ols[ols_id]['config'].get('version')
    if version is None:
        logger.warning('[%s] no OLS version', bioregistry_id)
        return

    version = _clean_version(bioregistry_id, version)
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


def iter_ols_getters(*, force_download: bool = True) -> Iterable[Type[Getter]]:
    """Iterate over OLS getters."""
    ols = get_ols(force_download=force_download, mappify=True)

    for bioregistry_id in bioregistry_id_to_ols_id:
        yv = make_ols_getter(ols=ols, bioregistry_id=bioregistry_id)
        if yv is not None:
            yield yv


def extend_ols_getters(getters, *, force_download: bool = True):
    """Extend the getters, without adding duplicates."""
    for ols_getter in iter_ols_getters(force_download=force_download):
        if any(getter.bioregistry_id == ols_getter.bioregistry_id for getter in getters):
            continue
        getters.append(ols_getter)


if __name__ == '__main__':
    list(iter_ols_getters())
