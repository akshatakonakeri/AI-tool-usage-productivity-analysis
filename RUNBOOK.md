# AI Productivity Dashboard Runbook

This runbook is the standard operating procedure for monthly AI productivity reporting.

## 1) Objective

Deliver a validated leadership dashboard showing:
- Productivity impact from AI adoption
- Quality and defect trend impact
- Financial ROI and payback

## 2) Inputs Required

Place updated files in `data/raw/`:
- `task_logs.csv`
- `developer_metrics.csv`
- `bug_tracking.csv`
- `employee_costs.csv`
- `ai_usage.csv`

## 3) Pipeline Execution (Python)

### 3.1 Setup environment

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### 3.2 Run pipeline

```bash
python main.py
```

### 3.3 Expected outputs

Check `data/processed/` for:
- `fact_productivity.csv`
- `fact_quality.csv`
- `fact_costs.csv`
- `fact_stats_results.csv`
- `kpi_summary.csv`
- `roi_summary.csv`

Stop and investigate if any file is missing or empty.

## 4) Power BI Build/Refresh Procedure

Follow:
- `powerbi/VISUAL_BUILD_GUIDE.md`
- `powerbi/MEASURE_LIBRARY.md`
- `powerbi/DASHBOARD_CHECKLIST.md`

### 4.1 Refresh data
- Open Power BI report.
- Refresh all queries/tables from `data/processed/`.
- Confirm latest reporting month is present.

### 4.2 Validate measures
- Ensure all DAX measures compile with no errors.
- Check KPI cards populate immediately after refresh.

## 5) QA and Sign-off

Run all checks in:
- `powerbi/QA_VALIDATION_CHECKS.md`

Minimum sign-off gates:
- KPI reconciliation complete
- ROI reconciliation complete
- Slicer and interaction behavior verified
- Watchlist flags tested
- Statistical labels validated

## 6) Leadership Narrative Template

Use this short structure in monthly readout:

1) **Impact:**  
   Time saved %, productivity increase %, error reduction %.

2) **Quality guardrails:**  
   Defect trend, reopen trend, critical defect trend.

3) **Financial value:**  
   ROI %, total benefits, payback months.

4) **Risk callouts:**  
   Any over-reliance clusters or quality drift.

5) **Action items:**  
   Team-level enablement, process fixes, governance updates.

## 7) Monthly Operating Cadence

- **Day 1-2:** ingest source exports
- **Day 2:** run Python pipeline
- **Day 3:** refresh Power BI and validate
- **Day 4:** leadership review draft
- **Day 5:** publish final dashboard

## 8) Incident Handling

If results look materially different from prior month:
- Verify source extract completeness
- Check rollout date and period tagging logic
- Re-run pipeline in clean environment
- Compare KPI/ROI deltas against previous processed outputs
- Escalate only after data and model checks are complete

## 9) Versioning and Change Control

Any logic change to metrics, ROI, or flags must include:
- Update to `README.md`
- Update to impacted Power BI docs
- Re-baseline expected values in QA checks

## 10) Fast Commands Reference

Generate sample and run:

```bash
python main.py --generate-sample
```

Normal monthly run:

```bash
python main.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```
