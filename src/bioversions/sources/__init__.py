"""Sources for Bioversions."""

from __future__ import annotations

import ftplib
import traceback
from collections.abc import Iterable, Mapping
from functools import lru_cache
from typing import Literal, NamedTuple, overload

from tqdm import tqdm
from tqdm.contrib.logging import logging_redirect_tqdm

from .antibodyregistry import AntibodyRegistryGetter
from .bigg import BiGGGetter
from .biogrid import BioGRIDGetter
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
from .mesh import MeshGetter
from .mgi import MGIGetter
from .mirbase import MirbaseGetter
from .moalmanac import MOAlmanacGetter
from .msigdb import MSigDBGetter
from .ncit import NCItGetter
from .npass import NPASSGetter
from .obo import iter_obo_getters
from .ols import extend_ols_getters
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
from .rxnorm import RxNormGetter
from .sgd import SgdGetter
from .signor import SignorGetter
from .silva import SILVAGetter
from .slm import SwissLipidGetter
from .stringdb import StringDBGetter
from .umls import UMLSGetter
from .uniprot import UniProtGetter
from .wikipathways import WikiPathwaysGetter
from .zfin import ZfinGetter
from ..utils import Getter, VersionResult, norm, refresh_daily

__all__ = [
    "VersionFailure",
    "clear_cache",
    "get_rows",
    "get_version",
    "iter_versions",
    "resolve",
]

#: These are broken beyond fixing at the moment
SKIPPED = [
    DrugBankGetter,
    PathwayCommonsGetter,
    DisGeNetGetter,
]


@lru_cache(maxsize=1)
def get_getters() -> list[type[Getter]]:
    """Get a list of getters."""
    # TODO replace with entrypoint lookup
    getters: list[type[Getter]] = [
        BioGRIDGetter,
        ChEMBLGetter,
        ComplexPortalGetter,
        DrugCentralGetter,
        ExPASyGetter,
        IntActGetter,
        InterProGetter,
        ReactomeGetter,
        RfamGetter,
        WikiPathwaysGetter,
        MirbaseGetter,
        MSigDBGetter,
        PfamGetter,
        UniProtGetter,
        KEGGGetter,
        PathBankGetter,
        NCBIGeneGetter,
        NPASSGetter,
        RheaGetter,
        StringDBGetter,
        HomoloGeneGetter,
        MeshGetter,
        DGIGetter,
        FlybaseGetter,
        PombaseGetter,
        SgdGetter,
        ZfinGetter,
        NCItGetter,
        RxNormGetter,
        ChemIDplusGetter,
        GuideToPharmacologyGetter,
        OncoTreeGetter,
        MOAlmanacGetter,
        AntibodyRegistryGetter,
        EnsemblGetter,
        BiGGGetter,
        ChEBIGetter,
        PRGetter,
        PubChemGetter,
        SwissLipidGetter,
        ITISGetter,
        DepMapGetter,
        UMLSGetter,
        HGNCGetter,
        RGDGetter,
        CellosaurusGetter,
        MGIGetter,
        OMIMGetter,
        ICFGetter,
        ICD10Getter,
        ICD11Getter,
        CiVICGetter,
        GTDBGetter,
        SILVAGetter,
        SignorGetter,
    ]
    getters.extend(iter_obo_getters())
    extend_ols_getters(getters)
    getters = sorted(getters, key=lambda cls: (cls.bioregistry_id or "", cls.__name__.casefold()))
    return getters


def get_getter_dict() -> Mapping[str, type[Getter]]:
    """Get a dict of getters."""
    rv = {}
    for getter in get_getters():
        if getter.bioregistry_id:
            rv[getter.bioregistry_id] = getter
            rv[norm(getter.bioregistry_id)] = getter
        rv[getter.name] = getter
        rv[norm(getter.name)] = getter
        for pp in getter.collection or []:
            rv[pp] = getter
            rv[norm(pp)] = getter
    return rv


def resolve(name: str, use_cache: bool = True) -> VersionResult:
    """Resolve the database name to a :class:`Bioversion` instance."""
    if use_cache:
        return _resolve_helper_cached(name)
    else:
        return _resolve_helper(name)


@refresh_daily
def _resolve_helper_cached(name: str) -> VersionResult:
    return _resolve_helper(name)


def clear_cache() -> None:
    """Clear the cache."""
    _resolve_helper_cached.clear_cache()


def _resolve_helper(name: str) -> VersionResult:
    norm_name = norm(name)
    getter: type[Getter] = get_getter_dict()[norm_name]
    return getter.resolve()


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
        it = tqdm(get_getters(), disable=not use_tqdm, desc="Getting versions", unit="resource")
        for cls in it:
            it.set_postfix(name=cls.name)
            try:
                yv = resolve(cls.name)
            except (OSError, AttributeError, ftplib.error_perm):
                msg = f"[{cls.bioregistry_id or cls.name}] failed to resolve"
                tqdm.write(msg)
                yield VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
            except (ValueError, KeyError) as e:
                msg = f"[{cls.bioregistry_id or cls.name}] issue parsing: {e}"
                tqdm.write(msg)
                yield VersionFailure(cls.name, cls.__name__, msg, traceback.format_exc())
            else:
                yield yv
