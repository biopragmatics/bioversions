"""Sources for Bioversions."""

from __future__ import annotations

import ftplib
import traceback
import warnings
from collections.abc import Iterable
from typing import Literal, NamedTuple, overload

from class_resolver import ClassResolver
from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from .antibodyregistry import AntibodyRegistryGetter
from .bigg import BiGGGetter
from .biogrid import BioGRIDGetter
from .ccle import CCLEGetter
from .cellosaurus import CellosaurusGetter
from .chebi import ChEBIGetter
from .chembl import ChEMBLGetter
from .chemidplus import ChemIDplusGetter
from .civic import CiVICGetter
from .complexportal import ComplexPortalGetter
from .daily import NCBIGeneGetter
from .depmap import DepMapGetter
from .dgi import DGIGetter
from .disgenet import DisGeNetGetter
from .drugbank import DrugBankGetter
from .drugcentral import DrugCentralGetter
from .ensembl import EnsemblGetter
from .expasy import ExPASyGetter
from .flybase import FlybaseGetter
from .gtdb import GTDBGetter
from .guidetopharmacology import GuideToPharmacologyGetter
from .hgnc import HGNCGetter
from .homologene import HomoloGeneGetter
from .icd10 import ICD10Getter
from .icd11 import ICD11Getter
from .icf import ICFGetter
from .intact import IntActGetter
from .interpro import InterProGetter
from .itis import ITISGetter
from .kegg import KEGGGetter
from .loinc import LOINCGetter
from .mesh import MeshGetter
from .mgi import MGIGetter
from .mirbase import MirbaseGetter
from .moalmanac import MOAlmanacGetter
from .msigdb import MSigDBGetter
from .ncit import NCItGetter
from .npass import NPASSGetter
from .obo import DoidGetter, GoGetter
from .ols import extend_ols
from .omim import OMIMGetter
from .oncotree import OncoTreeGetter
from .pathbank import PathBankGetter
from .pathwaycommons import PathwayCommonsGetter
from .pfam import PfamGetter
from .pombase import PombaseGetter
from .pr import PRGetter
from .pubchem import PubChemGetter
from .reactome import ReactomeGetter
from .rfam import RfamGetter
from .rgd import RGDGetter
from .rhea import RheaGetter
from .ror import RORGetter
from .rxnorm import RxNormGetter
from .sgd import SgdGetter
from .signor import SignorGetter
from .silva import SILVAGetter
from .slm import SwissLipidGetter
from .spdx import SPDXGetter
from .stringdb import StringDBGetter
from .umls import UMLSGetter
from .uniprot import UniProtGetter
from .wikipathways import WikiPathwaysGetter
from .zfin import ZfinGetter
from ..utils import (
    DailyGetter,
    Getter,
    OBOFoundryGetter,
    UnversionedGetter,
    VersionResult,
    refresh_daily,
)

__all__ = [
    "AntibodyRegistryGetter",
    "BiGGGetter",
    "BioGRIDGetter",
    "CCLEGetter",
    "CellosaurusGetter",
    "ChEBIGetter",
    "ChEMBLGetter",
    "ChemIDplusGetter",
    "CiVICGetter",
    "ComplexPortalGetter",
    "DGIGetter",
    "DepMapGetter",
    "DisGeNetGetter",
    "DoidGetter",
    "DrugBankGetter",
    "DrugCentralGetter",
    "EnsemblGetter",
    "ExPASyGetter",
    "FlybaseGetter",
    "GTDBGetter",
    "GoGetter",
    "GuideToPharmacologyGetter",
    "HGNCGetter",
    "HomoloGeneGetter",
    "ICD10Getter",
    "ICD11Getter",
    "ICFGetter",
    "ITISGetter",
    "IntActGetter",
    "InterProGetter",
    "KEGGGetter",
    "LOINCGetter",
    "MGIGetter",
    "MOAlmanacGetter",
    "MSigDBGetter",
    "MeshGetter",
    "MirbaseGetter",
    "NCBIGeneGetter",
    "NCItGetter",
    "NPASSGetter",
    "OMIMGetter",
    "OncoTreeGetter",
    "PRGetter",
    "PathBankGetter",
    "PathwayCommonsGetter",
    "PfamGetter",
    "PombaseGetter",
    "PubChemGetter",
    "RGDGetter",
    "RORGetter",
    "ReactomeGetter",
    "RfamGetter",
    "RheaGetter",
    "RxNormGetter",
    "SILVAGetter",
    "SPDXGetter",
    "SgdGetter",
    "SignorGetter",
    "StringDBGetter",
    "SwissLipidGetter",
    "UMLSGetter",
    "UniProtGetter",
    "VersionFailure",
    "WikiPathwaysGetter",
    "ZfinGetter",
    "clear_cache",
    "get_rows",
    "get_version",
    "getter_resolver",
    "iter_versions",
    "resolve",
]

#: These are broken beyond fixing at the moment
SKIPPED = {
    DrugBankGetter,
    PathwayCommonsGetter,
    DisGeNetGetter,
    # Upper-level classes
    OBOFoundryGetter,
    UnversionedGetter,
    DailyGetter,
}

getter_resolver: ClassResolver[Getter] = ClassResolver.from_subclasses(
    base=Getter,
    suffix="Getter",
    skip=SKIPPED,
    synonym_attribute=["collection"],
)
extend_ols(getter_resolver)


def get_getters() -> list[type[Getter]]:
    """Get a list of getters."""
    warnings.warn("iterate over getter_resolver directly", DeprecationWarning, stacklevel=2)
    return list(getter_resolver)


def resolve(name: str | type[Getter], *, use_cache: bool = True) -> VersionResult:
    """Resolve the database name to a :class:`Bioversion` instance."""
    if use_cache:
        if isinstance(name, type):
            name = name.__name__
        return _resolve_helper_cached(name)
    else:
        if isinstance(name, str):
            name = getter_resolver.lookup(name)
        return name.resolve()


@refresh_daily
def _resolve_helper_cached(name: str) -> VersionResult:
    getter = getter_resolver.lookup(name)
    return getter.resolve()


def clear_cache() -> None:
    """Clear the cache."""
    _resolve_helper_cached.clear_cache()


# docstr-coverage:excused `overload`
@overload
def get_version(name: str, *, strict: Literal[True] = True) -> str: ...


# docstr-coverage:excused `overload`
@overload
def get_version(name: str, *, strict: Literal[False] = False) -> str | None: ...


def get_version(name: str, *, strict: bool = True) -> str | None:
    """Resolve a database name to its version string.

    :param name:
        The name of the resource to get the version from. Often, this is a Bioregistry
        prefix, but sometimes can be an ad-hoc key for a database.
    :param strict:
        Re-raises errors in version resolution by default. Set explicitly to
        ``false`` to return None on errors.
    :return: The version of the resource as a string
    """
    try:
        rv = resolve(name).version
    except Exception:
        if strict:
            raise
        return None
    else:
        return rv


def get_rows(use_tqdm: bool | None = False) -> list[VersionResult]:
    """Get the rows, refreshing once per day."""
    return [
        bioversion
        for bioversion in iter_versions(use_tqdm=use_tqdm)
        if isinstance(bioversion, VersionResult)
    ]


class VersionFailure(NamedTuple):
    """Holds information about failures."""

    name: str
    clstype: str
    message: str
    trace: str


def iter_versions(
    use_tqdm: bool | None = False,
) -> Iterable[VersionResult | VersionFailure]:
    """Iterate over versions, without caching."""
    with logging_redirect_tqdm():
        getters = tqdm(
            list(getter_resolver), disable=not use_tqdm, desc="Getting versions", unit="resource"
        )
        for cls in getters:
            getters.set_postfix(name=cls.name)
            try:
                yv = resolve(cls)
            except (OSError, AttributeError, ftplib.error_perm) as e:
                msg = f"[{cls.bioregistry_id or cls.name}] failed to resolve: {e}"
                tqdm.write(msg)
                yield VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
            except (ValueError, KeyError) as e:
                msg = f"[{cls.bioregistry_id or cls.name}] issue parsing: {e}"
                tqdm.write(msg)
                yield VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
            else:
                yield yv
