# AI Tool Usage Productivity Analysis

End-to-end analytics project to measure how AI tools (for example, ChatGPT and GitHub Copilot) impact workforce productivity, quality, and ROI.

This project combines:
- Python pipeline for data preparation, KPI computation, statistical analysis, and ROI modeling
- Power BI documentation package for executive dashboard implementation
- Streamlit app for a quick live web dashboard

## Why This Project Matters

Most organizations adopt AI tools quickly, but struggle to answer:
- Is work getting faster?
- Is quality improving or dropping?
- Are we getting real financial return from AI spend?

This project provides a practical answer using measurable business outcomes.

## Key Outcomes Measured

- Time saved (before AI vs after AI)
- Productivity change by role/team/project
- Defect and rework trend impact
- Financial impact:
  - total benefits
  - total costs
  - net benefit
  - ROI %
  - payback period

## Project Structure

- `main.py` - pipeline entry point
- `src/` - ETL, KPI, stats, ROI, export modules
- `config/settings.json` - rollout date, columns, assumptions
- `data/raw/` - input CSV files
- `data/processed/` - curated datasets for BI
- `powerbi/` - data dictionary, DAX starter measures, dashboard checklist
- `app.py` - Streamlit dashboard app
- `RUNBOOK.md` - monthly operations runbook
- `PROJECT_INDEX.md` - full navigation map

## Quick Start

1) Create and activate a Python environment

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Generate sample input data (optional)

```bash
python main.py --generate-sample
```

4) Run full pipeline

```bash
python main.py
```

5) Launch Streamlit dashboard (optional)

```bash
streamlit run app.py
```

6) Use output files in Power BI

Import CSVs from `data/processed/` and follow the docs under `powerbi/`.

## Expected Input Files (data/raw)

- `task_logs.csv`
- `developer_metrics.csv`
- `bug_tracking.csv`
- `employee_costs.csv`
- `ai_usage.csv`

## Output Files (data/processed)

- `fact_productivity.csv`
- `fact_quality.csv`
- `fact_costs.csv`
- `fact_stats_results.csv`
- `kpi_summary.csv`
- `roi_summary.csv`

## Notes

- The pipeline is resilient to missing optional columns and uses defaults where possible.
- Replace sample data with real exports from Jira/GitHub/ADO/HRIS/AI tool telemetry.

## Documentation Map

- Start here: `PROJECT_INDEX.md`
- Operating guide: `RUNBOOK.md`
- Monthly close: `MONTHLY_CLOSE_CHECKLIST.md`
- Handover guide: `HANDOVER_NOTE.md`
- Executive summary template: `EXEC_SUMMARY_TEMPLATE.md`
- Example executive summary: `EXEC_SUMMARY_EXAMPLE.md`
- Deployment guide: `DEPLOYMENT.md`

## Deployment

Public deployment options are documented in `DEPLOYMENT.md`:
- Streamlit Community Cloud
- Render

## License

This repository currently has no explicit license file. Add one if you plan to reuse/distribute publicly.
