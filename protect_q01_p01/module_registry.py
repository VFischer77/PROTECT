"""P05.4 immutable conceptual module registry; only Q01/Q02 have live pilot analytics."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ModuleSpec:
    code: str
    name: str
    status: str
    source: str

MODULES = (
    ModuleSpec("Q01","Deviation Management","PILOT_DATA_AVAILABLE","P05.2"),
    ModuleSpec("Q02","CAPA Management & Effectiveness","PILOT_DATA_AVAILABLE","P05.2"),
    ModuleSpec("Q03","Internal Audits","DESIGN_ONLY","NONE"),
    ModuleSpec("Q04","External Audits & Inspections","DESIGN_ONLY","NONE"),
    ModuleSpec("Q04-G01","Audit Governance","DESIGN_ONLY","NONE"),
    ModuleSpec("Q05","Additional Quality/Inspection Domain","SCOPE_PENDING","NONE"),
    ModuleSpec("O01","Maintenance","DESIGN_ONLY","NONE"),
    ModuleSpec("Q09","Training","DESIGN_ONLY","NONE"),
    ModuleSpec("O06","Change Control","DESIGN_ONLY","NONE"),
    ModuleSpec("Q10","Management Review","DESIGN_ONLY","NONE"),
    ModuleSpec("Q11","Opportunities for Improvement","DESIGN_ONLY","NONE"),
    ModuleSpec("RI01","Regulatory Intelligence","DESIGN_ONLY","NONE"),
)
def registry():
    codes=[m.code for m in MODULES]
    if len(codes)!=len(set(codes)):
        raise ValueError("Duplicate module code")
    return MODULES
