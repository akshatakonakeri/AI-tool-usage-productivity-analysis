# Release Notes

## v1.0.0 - Initial Public Release

Date: 2026-05-01

### Highlights

- Built a full hybrid analytics solution for AI productivity impact measurement.
- Added end-to-end Python pipeline from raw data to reporting-ready outputs.
- Added KPI, statistical testing, and ROI modeling with business-focused outputs.
- Added Power BI implementation pack with DAX measures, visual mapping, and QA checks.
- Added Streamlit app for web dashboard access.
- Added operations assets for monthly reporting, leadership summaries, and handover.

### Included Components

- Data pipeline: `main.py`, `src/`
- Config: `config/settings.json`
- Processed output contract: `data/processed/`
- Dashboard app: `app.py`, `.streamlit/config.toml`, `Procfile`
- Power BI docs: `powerbi/`
- Operations docs:
  - `RUNBOOK.md`
  - `MONTHLY_CLOSE_CHECKLIST.md`
  - `HANDOVER_NOTE.md`
  - `PROJECT_INDEX.md`
  - `EXEC_SUMMARY_TEMPLATE.md`
  - `EXEC_SUMMARY_EXAMPLE.md`

### Business Value Delivered

- Clear before-vs-after AI impact visibility
- Role-level productivity and quality insights
- Quantified financial return from AI adoption
- Repeatable monthly governance and reporting flow

### Next Planned Improvements

- Add configurable control-group comparison (difference-in-differences)
- Add scenario simulation inputs in Streamlit UI
- Add automated scheduled pipeline run support
- Add CI checks for data schema validation
