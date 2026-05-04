"""Sources for Bioversions."""

from __future__ import annotations

import ftplib
import traceback
from collections.abc import Iterable
from functools import lru_cache
from typing import Literal, NamedTuple, overload

from class_resolver import ClassResolver
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map
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
from ..utils import DailyGetter, Getter, OBOFoundryGetter, UnversionedGetter, VersionResult

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


# docstr-coverage:excused `overload`
@overload
def resolve(name: str | type[Getter], strict: Literal[False] = ...) -> VersionResult | None: ...


# docstr-coverage:excused `overload`
@overload
def resolve(name: str | type[Getter], strict: Literal[True] = ...) -> VersionResult: ...


@lru_cache(None)
def resolve(name: str | type[Getter], strict: bool = True) -> VersionResult | None:
    """Resolve the database name to a :class:`Bioversion` instance."""
    try:
        # this can throw a key error if it can't be looked up
        getter = getter_resolver.lookup(name)
        # this can throw all sorts of errors during resolution
        rv = getter.resolve()
    except Exception:
        if strict:
            raise
        return None
    else:
        return rv


def clear_cache() -> None:
    """Clear the cache."""
    resolve.cache_clear()  # type: ignore[attr-defined]


# docstr-coverage:excused `overload`
@overload
def get_version(name: str | type[Getter], *, strict: Literal[True] = ...) -> str: ...


# docstr-coverage:excused `overload`
@overload
def get_version(name: str | type[Getter], *, strict: Literal[False] = ...) -> str | None: ...


def get_version(name: str | type[Getter], *, strict: bool = True) -> str | None:
    """Resolve a database name to its version string.

    :param name:
        The name of the resource to get the version from. Often, this is a Bioregistry
        prefix, but sometimes can be an ad-hoc key for a database.
    :param strict:
        Re-raises errors in version resolution by default. Set explicitly to
        ``false`` to return None on errors.
    :return: The version of the resource as a string
    """
    if strict:
        return resolve(name, strict=True).version
    rv = resolve(name, strict=False)
    if rv is None:
        return None
    return rv.version


def get_rows(*, use_tqdm: bool | None = False) -> list[VersionResult]:
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
    *,
    use_tqdm: bool | None = False,
) -> Iterable[VersionResult | VersionFailure]:
    """Iterate over versions, without caching."""
    with logging_redirect_tqdm():
        for yv in thread_map(
            _safe_resolve,
            list(getter_resolver),
            disable=not use_tqdm,
            desc="Getting versions",
            unit="resource",
        ):
            if yv:
                yield yv


def _safe_resolve(cls: type[Getter]) -> VersionResult | VersionFailure | None:
    try:
        yv = resolve(cls, strict=False)
    except (OSError, AttributeError, ftplib.error_perm) as e:
        msg = f"[bioversions:{cls.bioregistry_id or cls.name}] failed to resolve: {e}"
        tqdm.write(msg)
        return VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
    except (ValueError, KeyError) as e:
        msg = f"[bioversions:{cls.bioregistry_id or cls.name}] issue parsing: {e}"
        tqdm.write(msg)
        return VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
    else:
        return yv
