# Power BI QA Validation Checks

Use this checklist before sharing the dashboard with leadership.

## 1) Data Load Validation

- Confirm all expected files are loaded:
  - `fact_productivity`
  - `fact_quality`
  - `fact_costs`
  - `fact_stats_results`
  - `kpi_summary`
  - `roi_summary`
- Check row counts are non-zero for all fact tables.
- Verify `date` is Date type in all relevant tables.
- Verify `period` contains only `pre_ai` and `post_ai`.
- Verify no unexpected null spikes in key fields:
  - `task_hours`
  - `features_delivered`
  - `defects_total`
  - `hourly_cost`

Pass criteria:
- No missing required tables.
- No zero-row fact tables.
- Date and period columns typed and populated correctly.

## 2) Relationship Validation

Check model relationships:
- `fact_productivity[date]` -> `fact_quality[date]`
- `fact_productivity[team]` -> `fact_quality[team]`
- `fact_productivity[project]` -> `fact_quality[project]`
- `fact_productivity[date]` -> `fact_costs[date]`
- `fact_productivity[employee_id]` -> `fact_costs[employee_id]`

Pass criteria:
- Relationships are active and filtering works from slicers to visuals.
- No many-to-many ambiguity warnings for planned visuals.

## 3) Core Measure Reconciliation

Compare Power BI measure results with CSV output snapshots.

### Test 3.1: KPI Summary Match
- In Power BI, create a table with:
  - KPI labels and card values for:
    - `Time Saved %`
    - `Productivity Increase %`
    - `Error Reduction %`
- Compare to `kpi_summary.csv`.

Pass criteria:
- Each KPI within tolerance of +/- 0.2 percentage points.

### Test 3.2: ROI Summary Match
- Create a table with:
  - `Time Saved Value`
  - `Productivity Gain Value`
  - `Rework Savings Value`
  - `Total Benefits Value`
  - `AI Tool Costs`
  - `ROI %`
  - `Payback Months`
- Compare to `roi_summary.csv`.

Pass criteria:
- Currency values within +/- 1.0 (rounding tolerance).
- ROI and payback within +/- 0.2.

## 4) Slicer Behavior Validation

Test slicers:
- Date range
- Team
- Project
- Role
- AI usage level
- Period

Steps:
1) Apply one slicer at a time and verify all KPI cards update.
2) Apply multi-slicer combinations (team + project + period).
3) Clear slicers and verify totals return to baseline.

Pass criteria:
- No visual remains static when it should filter.
- No blank dashboard state unless slicers intentionally exclude all data.

## 5) Visual Interaction Validation

Using `Edit interactions`:
- Scatter should filter matrix/watchlist.
- KPI cards should respond to slicers.
- Table row selections should not unexpectedly rewrite KPI totals.

Pass criteria:
- Interactions match design intent from `VISUAL_BUILD_GUIDE.md`.

## 6) Trend and Period Boundary Checks

Checks:
- Pre/post split appears correctly around rollout period.
- `year_month` sorting is chronological, not alphabetical.
- Trend lines do not show broken points due to text/date mismatch.

Pass criteria:
- Rollout transition is visible and logically consistent.
- Monthly trend order is correct.

## 7) Watchlist / Risk Logic Validation

Validate over-reliance flags:
- `High AI Usage Flag`
- `Defect Drift Flag`
- `Over Reliance Flag`

Steps:
1) Build a debug table by employee with all three flags.
2) Spot check at least 5 employees:
  - high AI usage and rising defects -> flagged
  - low AI usage and stable defects -> not flagged

Pass criteria:
- Flag logic aligns with measure definitions in `MEASURE_LIBRARY.md`.

## 8) Statistical Results Validation

Checks:
- `fact_stats_results` table visible in report (or hidden but tested).
- `Min P Value`, `Max Effect Size`, labels populate correctly.

Pass criteria:
- `Stat Significance Label` changes correctly around p-value threshold 0.05.
- Effect strength label follows bucket logic.

## 9) Performance and Usability Validation

Checks:
- Page render under 3-5 seconds on standard filtered views.
- No visual exceeds practical point density (avoid unreadable scatter overload).
- Titles, units, and legends are consistent.

Pass criteria:
- Dashboard remains responsive and interpretable for leadership.

## 10) Final Publish Gate

Approve only when all are true:
- Data and relationships validated
- KPI/ROI reconciled against CSVs
- Slicers/interactions verified
- Watchlist logic tested
- Statistical labels tested
- Visual formatting and load performance acceptable

## Optional Audit Table (Recommended)

Create a hidden QA page with:
- A table of raw measure outputs
- A table of expected benchmark values from CSV
- A delta column (`actual - expected`)

Use this page after each refresh cycle to catch regressions quickly.
