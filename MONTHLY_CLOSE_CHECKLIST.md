# Monthly Close Checklist (AI Productivity Reporting)

Use this checklist at each reporting cycle close.

## A) Data Readiness

- [ ] Confirm all source exports are delivered:
  - [ ] `task_logs.csv`
  - [ ] `developer_metrics.csv`
  - [ ] `bug_tracking.csv`
  - [ ] `employee_costs.csv`
  - [ ] `ai_usage.csv`
- [ ] Confirm files are for correct reporting period.
- [ ] Confirm no duplicate file versions in `data/raw/`.
- [ ] Confirm mandatory columns exist (date, employee/team/project identifiers, metrics).

## B) Pipeline Execution

- [ ] Activate environment and dependencies:
  - [ ] `python -m venv .venv` (if needed)
  - [ ] `source .venv/Scripts/activate`
  - [ ] `pip install -r requirements.txt`
- [ ] Run analytics pipeline:
  - [ ] `python main.py`
- [ ] Confirm generated outputs in `data/processed/`:
  - [ ] `fact_productivity.csv`
  - [ ] `fact_quality.csv`
  - [ ] `fact_costs.csv`
  - [ ] `fact_stats_results.csv`
  - [ ] `kpi_summary.csv`
  - [ ] `roi_summary.csv`

## C) Data Quality and Reconciliation

- [ ] Row counts are non-zero for all fact files.
- [ ] `period` is only `pre_ai` and `post_ai`.
- [ ] `year_month` includes latest month expected.
- [ ] KPI values are within expected variance vs prior cycle.
- [ ] ROI values are plausible (costs not zero unless intended).
- [ ] Investigate any major deltas before report refresh.

## D) Power BI Refresh and Build

- [ ] Refresh all model tables from `data/processed/`.
- [ ] Verify measures compile successfully.
- [ ] Validate dashboard pages:
  - [ ] Executive Overview
  - [ ] Productivity Deep Dive
  - [ ] Quality and Risk
- [ ] Confirm slicers filter all intended visuals.
- [ ] Confirm trend charts show correct month ordering.

## E) QA Sign-Off

- [ ] Complete checks from `powerbi/QA_VALIDATION_CHECKS.md`.
- [ ] Reconcile KPIs with `kpi_summary.csv`.
- [ ] Reconcile ROI metrics with `roi_summary.csv`.
- [ ] Validate over-reliance watchlist logic.
- [ ] Validate statistical labels and significance indicators.

## F) Leadership Pack

- [ ] Update `EXEC_SUMMARY_TEMPLATE.md` for current month.
- [ ] Include:
  - [ ] Headline KPIs
  - [ ] ROI and payback
  - [ ] Risk callouts
  - [ ] Decisions required
  - [ ] 30-day actions with owners
- [ ] Review narrative for business clarity and actionability.

## G) Publish and Communicate

- [ ] Publish dashboard to Power BI Service.
- [ ] Confirm scheduled refresh settings.
- [ ] Share dashboard link with stakeholder group.
- [ ] Send executive summary memo.
- [ ] Log release timestamp and owner.

## H) Post-Publish Controls

- [ ] Archive source files for audit trail.
- [ ] Snapshot key KPI/ROI outputs for next-month comparison.
- [ ] Document anomalies and resolutions.
- [ ] Capture improvement ideas for next cycle.

## Close Approval

- Report Owner: `________________`
- QA Reviewer: `________________`
- Leadership Reviewer: `________________`
- Close Date: `________________`
- Status: `[ ] Approved  [ ] Rework Required`
