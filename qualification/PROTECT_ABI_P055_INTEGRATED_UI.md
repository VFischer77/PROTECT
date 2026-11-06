# P05.5 — Integrated Dashboard User Interface
**Status: Pilot implementation; technical qualification pending; founder acceptance pending**

## Scope
Responsive local static HTML/CSS/JavaScript integrated module navigation and read-only management overview. Registry displays all planned modules, distinguishes Q01/Q02 pilot-data availability from design-only and scope-pending modules. Reuses synthetic Q01/Q02 analytics and worklist. Selecting an unavailable module displays an explicit limitation, not fabricated data. No third-party scripts or client data.

## Boundaries
No backend integration, production authentication, module-specific dashboards for other modules, validated KPI, classification, predictive analytics, automatic quality decision, commercial hosting or release. This is a demonstrator, not a complete integrated product.

## Local demo
From repository root: `python -m protect_q01_p01.integrated_dashboard_demo prototype/p055/synthetic-integrated.json`
Then `cd prototype/p055 && python -m http.server 8000 --bind 127.0.0.1` and open http://127.0.0.1:8000/ . Do not expose this server to a network.

## Qualification plan
Actual-source P01–P05.5 regression; JavaScript syntax; synthetic contract export smoke. Browser visual acceptance and production security qualification not claimed. Classification mappings and Q05 scope remain pending founder approval.
