# -*- coding: utf-8 -*-

"""Sources for Bioversions."""

from typing import Iterable, List, Mapping, Type

from tqdm import tqdm

from .biofacquim import BiofacquimGetter
from .biogrid import BioGRIDGetter
from .chembl import ChEMBLGetter
from .complexportal import ComplexPortalGetter
from .daily import NCBIGeneGetter
from .drugbank import DrugBankGetter
from .drugcentral import DrugCentralGetter
from .expasy import ExPASyGetter
from .intact import IntActGetter
from .interpro import InterProGetter
from .kegg import KEGGGetter
from .mirbase import MirbaseGetter
from .msigdb import MSigDBGetter
from .npass import NPASSGetter
from .obo import iter_obo_getters
from .ols import extend_ols_getters
from .pathbank import PathBankGetter
from .pfam import PfamGetter
from .reactome import ReactomeGetter
from .rfam import RfamGetter
from .uniprot import UniProtGetter
from .wikipathways import WikiPathwaysGetter
from ..utils import Bioversion, Getter, norm, refresh_daily

__all__ = [
    'getters',
    'getter_dict',
    'resolve',
    'get_rows',
    'get_version',
]

# TODO replace with entrypoint lookup
getters = [
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
    BiofacquimGetter,
]
getters.extend(iter_obo_getters())
extend_ols_getters(getters)
getters: List[Type[Getter]] = sorted(getters, key=lambda cls: (cls.bioregistry_id or '', cls.__name__.casefold()))

getter_dict: Mapping[str, Type[Getter]] = {
    norm(getter.name): getter
    for getter in getters
}


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
    getter: Type[Getter] = getter_dict[norm_name]
    return getter.resolve()


def get_version(name: str) -> str:
    """Resolve a database name to its version string."""
    return resolve(name).version


def get_rows(use_tqdm: bool = False) -> List[Bioversion]:
    """Get the rows, refreshing once per day."""
    return list(_iter_versions(use_tqdm=use_tqdm))


def _iter_versions(use_tqdm: bool = False) -> Iterable[Bioversion]:
    for cls in tqdm(getters, disable=not use_tqdm):
        yield resolve(cls.name)
