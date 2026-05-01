# Handover Note: AI Productivity Impact Project

This note helps a new analyst/operator take over the project quickly.

## 1) What This Project Does

This project measures the impact of AI tool adoption (e.g., ChatGPT, Copilot) on:
- Task completion speed
- Productivity output (features/tests)
- Quality outcomes (defects/rework)
- Financial return (ROI, payback)

It uses:
- Python for analytics pipeline
- Power BI for interactive reporting

## 2) 10-Minute Quick Start

1. Place fresh source files into `data/raw/`.
2. Run:
   - `pip install -r requirements.txt`
   - `python main.py`
3. Confirm outputs in `data/processed/`.
4. Refresh Power BI report using processed files.
5. Run QA checks and publish.

## 3) Key Files and Their Purpose

### Pipeline and Config
- `main.py` - pipeline entry point
- `config/settings.json` - rollout date and assumptions
- `src/etl.py` - data merge and fact-table construction
- `src/metrics.py` - KPI summary generation
- `src/stats.py` - before/after tests and correlation
- `src/roi.py` - ROI and payback calculations
- `src/export.py` - processed output exports
- `src/sample_data.py` - synthetic demo data generation

### Operational and Reporting Docs
- `README.md` - setup and usage instructions
- `RUNBOOK.md` - end-to-end monthly operating procedure
- `MONTHLY_CLOSE_CHECKLIST.md` - close checklist
- `EXEC_SUMMARY_TEMPLATE.md` - leadership memo template
- `EXEC_SUMMARY_EXAMPLE.md` - completed example memo

### Power BI Build Assets
- `powerbi/DATA_DICTIONARY.md`
- `powerbi/DAX_MEASURES.md`
- `powerbi/MEASURE_LIBRARY.md`
- `powerbi/DASHBOARD_CHECKLIST.md`
- `powerbi/VISUAL_BUILD_GUIDE.md`
- `powerbi/QA_VALIDATION_CHECKS.md`

## 4) Inputs and Outputs

### Inputs (`data/raw/`)
- `task_logs.csv`
- `developer_metrics.csv`
- `bug_tracking.csv`
- `employee_costs.csv`
- `ai_usage.csv`

### Outputs (`data/processed/`)
- `fact_productivity.csv`
- `fact_quality.csv`
- `fact_costs.csv`
- `fact_stats_results.csv`
- `kpi_summary.csv`
- `roi_summary.csv`

## 5) Critical Assumptions to Review Monthly

- AI rollout date in `config/settings.json`
- Hourly cost assumptions
- KPI and ROI tolerance thresholds
- Any metric definition changes requested by leadership

## 6) Common Failure Points

- Missing columns in raw input files
- Date parsing issues or incorrect period boundaries
- Incomplete data refresh in Power BI
- Slicer/relationship misconfiguration
- KPI mismatch due to stale processed files

## 7) Ownership Model (Suggested)

- Data ingestion owner: `Analytics Ops`
- Pipeline owner: `Data Analyst`
- Dashboard owner: `BI Analyst`
- QA sign-off owner: `Reporting Lead`
- Business sign-off owner: `Engineering/Finance leadership`

## 8) First-Day Onboarding Task for New Analyst

- Run sample flow:
  - `python main.py --generate-sample`
- Build/refresh Power BI using guide files.
- Complete QA checklist once.
- Draft executive summary from template.

If all four complete successfully, onboarding is done.

## 9) Change Management Rule

Any change to KPI logic, ROI model, or dashboard structure must update:
- documentation (`README`, `RUNBOOK`, Power BI docs)
- QA checks
- executive summary assumptions note

## 10) Escalation Trigger

Escalate before publish if:
- ROI swings materially without source explanation
- KPI deltas exceed expected ranges
- defects improve while reopen/critical defects worsen unexpectedly
- data completeness cannot be confirmed
