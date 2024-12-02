"""Sources for Bioversions."""

from __future__ import annotations

import ftplib
import logging
import traceback
from collections.abc import Iterable, Mapping
from functools import lru_cache
from typing import NamedTuple

from tqdm import tqdm

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
from .slm import SwissLipidGetter
from .stringdb import StringDBGetter
from .umls import UMLSGetter
from .uniprot import UniProtGetter
from .wikipathways import WikiPathwaysGetter
from .zfin import ZfinGetter
from ..utils import Bioversion, Getter, norm, refresh_daily

__all__ = [
    "get_rows",
    "get_version",
    "resolve",
]

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_getters() -> list[type[Getter]]:
    """Get a list of getters."""
    # TODO replace with entrypoint lookup
    getters: list[type[Getter]] = [
        BioGRIDGetter,
        ChEMBLGetter,
        ComplexPortalGetter,
        DrugBankGetter,
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
        DisGeNetGetter,
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
        PathwayCommonsGetter,
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
    getter: type[Getter] = get_getter_dict()[norm_name]
    return getter.resolve()


def get_version(name: str) -> str:
    """Resolve a database name to its version string."""
    return resolve(name).version


def get_rows(use_tqdm: bool | None = False) -> list[Bioversion]:
    """Get the rows, refreshing once per day."""
    return [
        bioversion
        for bioversion in _iter_versions(use_tqdm=use_tqdm)
        if isinstance(bioversion, Bioversion)
    ]


class FailureTuple(NamedTuple):
    """Holds information about failures."""

    name: str
    clstype: str
    message: str
    trace: str


def _iter_versions(
    use_tqdm: bool | None = False,
) -> Iterable[Bioversion | FailureTuple]:
    it = tqdm(get_getters(), disable=not use_tqdm)

    for cls in it:
        it.set_postfix(name=cls.name)
        try:
            yv = resolve(cls.name)
        except (OSError, AttributeError, ftplib.error_perm):
            msg = f"failed to resolve {cls.name}"
            tqdm.write(msg)
            yield FailureTuple(cls.name, cls.__name__, msg, traceback.format_exc())
        except ValueError as e:
            msg = f"issue parsing {cls.name}: {e}"
            tqdm.write(msg)
            yield FailureTuple(cls.name, cls.__name__, msg, traceback.format_exc())
        else:
            yield yv
