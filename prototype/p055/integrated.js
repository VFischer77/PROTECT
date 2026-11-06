"use strict";
const $ = id => document.getElementById(id);
function node(tag, value, cls) {const n=document.createElement(tag);if(value!==undefined)n.textContent=String(value);if(cls)n.className=cls;return n;}
function render(data) {
  if (data.schema_version!=="P05.5-PILOT-1" || data.data_origin!=="SYNTHETIC" ||
      data.cross_module_scope!=="Q01_Q02_ONLY" || data.human_decision!=="REQUIRED" ||
      data.risk_prediction!=="NOT_PERFORMED") throw Error("Unsupported or unsafe dashboard data");
  const active=data.modules.filter(m=>m.status==="PILOT_DATA_AVAILABLE");
  if(active.map(m=>m.code).sort().join(",")!=="Q01,Q02" ||
     data.modules.some(m=>m.status!=="PILOT_DATA_AVAILABLE" && m.metrics!==null))
     throw Error("Module data availability mismatch");
  const nav=$("modules");
  function select(code) {
    for(const b of nav.querySelectorAll("button"))b.setAttribute("aria-pressed",String(b.dataset.code===code));
    const m=data.modules.find(x=>x.code===code);
    $("sectionTitle").textContent=m ? m.code+" — "+m.name : "Management overview";
    $("sectionDescription").textContent=m ? (m.status==="PILOT_DATA_AVAILABLE" ?
      "Pilot descriptive data available. Cross-module worklist remains limited to Q01/Q02." :
      "Not implemented: no data, analytics or qualification available for this module.") :
      "Integrated module overview; only Q01 and Q02 have pilot data.";
  }
  const overview=node("button","All modules");overview.dataset.code="ALL";overview.addEventListener("click",()=>select("ALL"));nav.append(overview);
  for(const m of data.modules) {
    const b=node("button");b.dataset.code=m.code;
    b.append(node("span",m.code,"modulecode"),node("span",m.name),node("span",m.status==="PILOT_DATA_AVAILABLE"?"Pilot data available":m.status==="SCOPE_PENDING"?"Scope pending":"Design only","state"));
    b.addEventListener("click",()=>select(m.code));nav.append(b);
  }
  select("ALL");
  const source=data.source_dashboard;
  $("deviations").textContent=source.summary.deviation_records;
  $("capas").textContent=source.summary.capa_records;
  $("reviews").textContent=source.summary.human_review_items;
  const trend=$("trend");const max=Math.max(1,...source.deviation_trend.map(x=>x.count));
  for(const p of source.deviation_trend) {
    const col=node("div",undefined,"barcol"),bar=node("div",undefined,"bar");
    bar.style.height=Math.max(2,90*p.count/max)+"px";bar.setAttribute("aria-label",p.period+": "+p.count);
    col.append(node("strong",p.count),bar,node("span",p.period));trend.append(col);
  }
  if(!source.deviation_trend.length)trend.append(node("span","No periods","muted"));
  for(const o of source.capa_outcome_distribution) {
    const row=node("div",undefined,"row");row.append(node("span",o.outcome),node("span",o.count,"pill"));$("outcomes").append(row);
  }
  for(const s of source.review_worklist) {
    const tr=node("tr");
    for(const value of [s.signal_type,s.deviation_ids.join(", "),s.linked_capa_ids.join(", "),s.review_status])tr.append(node("td",value));
    $("signals").append(tr);
  }
  $("limitations").textContent=data.limitations;
  $("status").textContent="Synthetic integrated dashboard loaded. No source records can be changed.";
}
fetch("./synthetic-integrated.json",{cache:"no-store"}).then(r=>{if(!r.ok)throw Error("Missing data");return r.json();}).then(render)
.catch(()=>{$("status").textContent="Unable to load synthetic dashboard data. Use the documented local HTTP server.";});
