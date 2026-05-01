# AI Productivity Impact Project (Hybrid)

This project implements a hybrid analytics workflow:
- Python for data prep, KPI calculation, statistical tests, and ROI modeling
- Power BI for executive reporting and interactive dashboarding

## Project Structure

- `main.py` - pipeline entry point
- `src/` - ETL, KPI, stats, ROI, export modules
- `config/settings.json` - rollout date, columns, assumptions
- `data/raw/` - input CSV files
- `data/processed/` - curated datasets for BI
- `powerbi/` - data dictionary, DAX starter measures, dashboard checklist

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

5) Use output files in Power BI

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
