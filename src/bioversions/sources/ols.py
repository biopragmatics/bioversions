"""Get versions from the OLS."""

import logging
from collections.abc import Iterable, Mapping

import bioregistry
from bioregistry.external.ols import get_ols_processing
from bioregistry.resolve import get_name

from bioversions.utils import Getter, VersionType

logger = logging.getLogger(__name__)

ols_processing = get_ols_processing()


def _get_version_type(bioregistry_id: str) -> VersionType | None:
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
        return None


def make_ols_getter(bioregistry_id: str) -> type[Getter] | None:
    """Make a getter from OLS."""
    ols_id = bioregistry.get_ols_prefix(bioregistry_id)
    if ols_id is None:
        return None

    resource = bioregistry.get_resource(bioregistry_id)
    if resource is None:
        logger.warning(f"Invalid bioregistry prefix: {bioregistry_id}")
        return None
    if resource.ols is None:
        logger.warning("[%s] Missing information in OLS", bioregistry_id)
        return None
    version = resource.ols.get("version")
    if version is None:
        logger.debug("[%s] no OLS version", bioregistry_id)
        return None

    _brid = bioregistry_id
    _name = get_name(_brid)
    if _name is None:
        return None
    _version_type = _get_version_type(bioregistry_id)
    if _version_type is None:
        return None

    class OlsGetter(Getter):
        """A getter for OLS data from the Bioregistry."""

        bioregistry_id = _brid
        name = _name
        version_type = _version_type  # type:ignore

        def get(self) -> str | Mapping[str, str]:
            """Get the version from the Bioregistry."""
            return version

    return OlsGetter


def iter_ols_getters() -> Iterable[type[Getter]]:
    """Iterate over OLS getters."""
    for bioregistry_id in bioregistry.read_registry():
        yv = make_ols_getter(bioregistry_id)
        if yv is not None:
            yield yv


def extend_ols_getters(getters: list[type[Getter]]) -> None:
    """Extend the getters, without adding duplicates."""
    for ols_getter in iter_ols_getters():
        if any(getter.bioregistry_id == ols_getter.bioregistry_id for getter in getters):
            continue
        getters.append(ols_getter)


if __name__ == "__main__":
    list(iter_ols_getters())
