"""P02 offline shared workspace and Q01/Q02 linkage. No source mutation."""
from dataclasses import dataclass
from datetime import date
from typing import Tuple
from .analysis import analyze_deviations

INDUSTRIES = frozenset({"Pharmaceuticals","Biotechnology","Medical Devices","General Manufacturing","Professional & Business Services","Other Industries"})
DOMAINS = frozenset({"GMP/Quality","Operational Excellence","Enterprise Risk Management","Business Continuity & Resilience","Combined Services"})
OUTCOMES = frozenset({"Effective","Not Effective","Pending"})

@dataclass(frozen=True)
class WorkspaceProfile:
    industry: str
    service_domain: str
    version: int = 1
    baseline: str = "ISO 9001"

@dataclass(frozen=True)
class LinkedEvent:
    event_id: str
    event_type: str
    occurred_on: str

@dataclass(frozen=True)
class CapaReference:
    capa_id: str
    linked_deviation_ids: Tuple[str, ...]
    client_effectiveness: str = "Pending"

class Workspace:
    """Configuration selected once; changing it requires separate authorized change control."""
    def __init__(self, industry, service_domain):
        if industry not in INDUSTRIES or service_domain not in DOMAINS:
            raise ValueError("unsupported workspace profile; multi-profile extension not implemented")
        self._profile = WorkspaceProfile(industry, service_domain)
    @property
    def profile(self):
        return self._profile
    def module_profile(self, module):
        if module not in {"Q01","Q02"}:
            raise ValueError("unsupported module")
        return self._profile
    def reconfigure(self, *args, **kwargs):
        raise PermissionError("GC-005: change-control and impact assessment required")

def analyze_workspace(workspace, deviations, capas=(), audit_events=()):
    """Link references, never infer or modify client CAPA effectiveness."""
    if not isinstance(workspace, Workspace):
        raise ValueError("workspace required")
    result = analyze_deviations(deviations)
    ids = {r["id"] for r in deviations}
    if len(ids) != len(deviations):
        raise ValueError("duplicate deviations")
    capa_ids = set()
    links = []
    for capa in capas:
        if not isinstance(capa, CapaReference) or not capa.capa_id or capa.capa_id in capa_ids:
            raise ValueError("invalid or duplicate CAPA reference")
        capa_ids.add(capa.capa_id)
        if capa.client_effectiveness not in OUTCOMES:
            raise ValueError("invalid client effectiveness outcome")
        if len(set(capa.linked_deviation_ids)) != len(capa.linked_deviation_ids):
            raise ValueError("duplicate link")
        for deviation_id in capa.linked_deviation_ids:
            if deviation_id not in ids:
                raise ValueError("dangling deviation link")
            links.append({"capa_id":capa.capa_id,"deviation_id":deviation_id})
    audit_ids = set()
    for event in audit_events:
        if not isinstance(event, LinkedEvent) or event.event_type not in {"Internal Audit","External Audit","Authority Inspection"}:
            raise ValueError("unsupported audit event")
        if not event.event_id or event.event_id in audit_ids:
            raise ValueError("invalid or duplicate audit event")
        audit_ids.add(event.event_id)
        if not isinstance(event.occurred_on,str) or date.fromisoformat(event.occurred_on).isoformat()!=event.occurred_on:
            raise ValueError("invalid audit date")
    return {
        "workspace_profile":workspace.profile,
        "q01":result,
        "q02_capa_references":tuple({"capa_id":c.capa_id,"client_effectiveness":c.client_effectiveness} for c in capas),
        "capa_deviation_links":tuple(sorted(links,key=lambda x:(x["capa_id"],x["deviation_id"]))),
        "audit_event_count":len(audit_ids),
        "cross_module_causality":"NOT_ASSESSED",
        "classification_mapping":"DRAFT_REVIEW_REQUIRED",
        "iso9001_conformity":"NOT_ASSESSED",
    }
