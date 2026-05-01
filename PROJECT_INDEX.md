# Project Index: AI Productivity Impact Dashboard

Use this index as the main navigation file for the entire project.

## 1) Start Here

1. `README.md`  
   Setup, dependencies, run commands, and expected input/output files.

2. `HANDOVER_NOTE.md`  
   Quick takeover guide for new analysts and operators.

## 2) Build and Run (Python Pipeline)

1. `config/settings.json`  
   Rollout date and baseline assumptions.

2. `main.py`  
   Entry point for end-to-end processing.

3. `src/` modules  
   - `src/etl.py` -> fact table construction  
   - `src/metrics.py` -> KPI generation  
   - `src/stats.py` -> statistical analysis  
   - `src/roi.py` -> ROI calculations  
   - `src/export.py` -> output exports  
   - `src/sample_data.py` -> demo data generator

## 3) Power BI Build Assets

1. `powerbi/DATA_DICTIONARY.md`  
   Field-level semantic definitions.

2. `powerbi/MEASURE_LIBRARY.md`  
   Full copy-paste DAX measure set.

3. `powerbi/VISUAL_BUILD_GUIDE.md`  
   Exact visual mappings and interactions.

4. `powerbi/DASHBOARD_CHECKLIST.md`  
   Page-level dashboard design checklist.

5. `powerbi/DAX_MEASURES.md`  
   Core DAX starter set.

## 4) QA and Validation

1. `powerbi/QA_VALIDATION_CHECKS.md`  
   Data, KPI, ROI, slicer, and interaction validation gates.

2. `MONTHLY_CLOSE_CHECKLIST.md`  
   Monthly operational close checklist.

## 5) Reporting and Leadership Communication

1. `EXEC_SUMMARY_TEMPLATE.md`  
   Standard one-page monthly leadership memo.

2. `EXEC_SUMMARY_EXAMPLE.md`  
   Sample completed memo using generated pipeline outputs.

## 6) Operations and Governance

1. `RUNBOOK.md`  
   End-to-end monthly operating procedure and cadence.

2. `HANDOVER_NOTE.md`  
   Ownership model, onboarding, and escalation triggers.

## 7) Data Contract

### Input folder
- `data/raw/`
  - `task_logs.csv`
  - `developer_metrics.csv`
  - `bug_tracking.csv`
  - `employee_costs.csv`
  - `ai_usage.csv`

### Output folder
- `data/processed/`
  - `fact_productivity.csv`
  - `fact_quality.csv`
  - `fact_costs.csv`
  - `fact_stats_results.csv`
  - `kpi_summary.csv`
  - `roi_summary.csv`

## 8) Recommended Monthly Execution Order

1. Update `data/raw/` with latest extracts.  
2. Run `python main.py`.  
3. Verify outputs in `data/processed/`.  
4. Refresh Power BI model and measures.  
5. Complete QA checklist.  
6. Draft executive summary memo.  
7. Publish dashboard and circulate leadership update.

## 9) Fast Command Reference

Install dependencies:

```bash
pip install -r requirements.txt
```

Run with real data:

```bash
python main.py
```

Run with sample data:

```bash
python main.py --generate-sample
```

## 10) Maintenance Rule

Whenever metric logic, ROI assumptions, or dashboard visuals change:
- update docs in this index section
- update QA checks
- update reporting templates if impacted
