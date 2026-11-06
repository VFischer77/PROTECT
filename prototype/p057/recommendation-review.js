"use strict";
const decision=document.getElementById("decision"),detail=document.getElementById("detail"),
comment=document.getElementById("comment"),actor=document.getElementById("actor"),
copy=document.getElementById("copy"),area=document.getElementById("detailArea");
function refresh(){
  const needs=["IMPROVEMENT","REFER_CAPA","OTHER"].includes(decision.value);
  area.hidden=!needs;
  copy.disabled=!comment.value.trim()||!actor.value.trim()||(needs&&!detail.value.trim());
}
for(const el of [decision,detail,comment,actor])el.addEventListener("input",refresh);
decision.addEventListener("change",refresh);
copy.addEventListener("click",()=>{
  const record={recommendation_id:"REC-001",decision:decision.value,actor:actor.value.trim(),
    comment:comment.value.trim(),action_detail:area.hidden?"":detail.value.trim(),
    external_capa_created:false,record_status:"DRAFT_NOT_SAVED"};
  navigator.clipboard.writeText(JSON.stringify(record,null,2)).then(()=>{copy.textContent="Draft copied";})
  .catch(()=>{copy.textContent="Clipboard unavailable; use manual copy";});
});
refresh();
