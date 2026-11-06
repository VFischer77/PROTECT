"use strict";
// No external scripts, network telemetry, storage, mutation or server actions.
const el = id => document.getElementById(id);
const make = (tag, text, cls) => {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = String(text);
  if (cls) node.className = cls;
  return node;
};
function rows(target, entries, nameKey, valueKey) {
  target.replaceChildren();
  if (!entries.length) { target.append(make("p", "No records", "muted")); return; }
  for (const item of entries) {
    const row = make("div", undefined, "legendrow");
    row.append(make("span", item[nameKey]), make("span", item[valueKey], "pill"));
    target.append(row);
  }
}
function render(data) {
  if (!data || data.chart_semantics !== "DESCRIPTIVE_COUNTS_ONLY" ||
      data.risk_prediction !== "NOT_PERFORMED" || data.human_decision !== "REQUIRED" ||
      !Array.isArray(data.review_worklist)) throw Error("Unsupported or unsafe dashboard contract");
  el("deviations").textContent = data.summary.deviation_records;
  el("capas").textContent = data.summary.capa_records;
  el("reviews").textContent = data.summary.human_review_items;
  const trend = el("trend"); trend.replaceChildren();
  const maximum = Math.max(1, ...data.deviation_trend.map(x => x.count));
  for (const item of data.deviation_trend) {
    const wrap = make("div", undefined, "baritem");
    const count = make("strong", item.count);
    const bar = make("div", undefined, "bar");
    bar.style.height = (Math.max(2, 105 * item.count / maximum)) + "px";
    bar.setAttribute("aria-label", item.period + ": " + item.count);
    wrap.append(count, bar, make("span", item.period, "barlabel"));
    trend.append(wrap);
  }
  if (!data.deviation_trend.length) trend.append(make("p", "No deviation periods", "muted"));
  rows(el("outcomes"), data.capa_outcome_distribution, "outcome", "count");
  rows(el("signals"), data.review_signal_distribution, "signal_type", "count");
  const filter = el("filter");
  for (const kind of [...new Set(data.review_worklist.map(x => x.signal_type))].sort()) {
    const option = make("option", kind); option.value = kind; filter.append(option);
  }
  function update() {
    const filtered = data.review_worklist.filter(x => filter.value === "ALL" || x.signal_type === filter.value);
    const body = el("worklist"); body.replaceChildren();
    for (const item of filtered) {
      const tr = make("tr");
      for (const value of [item.signal_type, item.deviation_ids.join(", "), item.linked_capa_ids.join(", "), item.review_status]) {
        tr.append(make("td", value));
      }
      body.append(tr);
    }
    if (!filtered.length) { const tr=make("tr"),td=make("td","No review signals");td.colSpan=4;tr.append(td);body.append(tr); }
    el("visibleCount").textContent = filtered.length + " of " + data.review_worklist.length + " signals";
  }
  filter.addEventListener("change", update); update();
  el("limits").textContent = data.limitations;
  el("status").textContent = "Synthetic dashboard loaded. No records can be modified.";
}
fetch("./synthetic-dashboard.json", {cache:"no-store"})
  .then(response => {if(!response.ok) throw Error("Data unavailable");return response.json();})
  .then(render)
  .catch(() => {el("status").textContent = "Unable to load verified synthetic data. Serve this directory using a local HTTP server.";});
