"""Get versions from the OLS."""

import logging
from typing import ClassVar, cast

import bioregistry
from bioregistry.external.ols import get_ols_processing
from class_resolver import ClassResolver

from bioversions.utils import Getter, VersionType

logger = logging.getLogger(__name__)

ols_processing = get_ols_processing()


def _get_version_type(resource: bioregistry.Resource, ols_id: str) -> VersionType | None:
    ols_config = ols_processing.get(ols_id)
    if ols_config is None:
        raise ValueError(
            f"Missing OLS configuration for bioregistry:{resource.prefix} / ols:{ols_id}"
        )

    ols_version_type = ols_config.version_type
    ols_version_date_format = ols_config.version_date_format
    if ols_version_date_format:
        return VersionType.date
    elif ols_version_type:
        return VersionType[ols_version_type.name]
    else:
        logger.warning("[%s] missing version type", resource.prefix)
        return None


def make_ols_getter(resource: bioregistry.Resource) -> type[Getter] | None:
    """Make a getter from OLS."""
    ols_id = resource.get_ols_prefix()
    if ols_id is None:
        return None

    if resource.ols is None:
        raise RuntimeError(f"{resource.prefix} is mapped to OLS  {ols_id} but is missing OLS data")

    version = resource.ols.get("version")
    if version is None:
        logger.debug("[%s] no OLS version", resource)
        return None
    _name = resource.get_name()
    if _name is None:
        return None
    _version_type = _get_version_type(resource, ols_id=ols_id)
    if _version_type is None:
        return None

    class OlsGetter(Getter):
        """A getter for OLS data from the Bioregistry."""

        bioregistry_id: ClassVar[str] = resource.prefix
        name: ClassVar[str] = cast(str, _name)
        version_type: ClassVar[VersionType] = cast(VersionType, _version_type)

        def get(self) -> str:
            """Get the version from the Bioregistry."""
            return cast(str, version)

    class_name = f"{resource.prefix.title()}Getter"
    return type(class_name, (OlsGetter,), locals())


def extend_ols(version_getter_resolver: ClassResolver[Getter]) -> None:
    """Add OLS lookup."""
    for resource in bioregistry.resources():
        if resource.provides or resource.has_canonical or resource.part_of:
            continue
        try:
            version_getter_resolver.lookup(resource.prefix)
        except KeyError:
            pass
        else:
            continue
        getter = make_ols_getter(resource)
        if getter is None:
            continue
        version_getter_resolver.register(getter)
