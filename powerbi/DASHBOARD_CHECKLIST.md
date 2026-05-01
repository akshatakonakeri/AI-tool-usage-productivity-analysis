# Dashboard Build Checklist

## Data Import
- Import all CSV files from `data/processed/`
- Confirm `date` columns are Date type
- Create relationships:
  - `fact_productivity[employee_id]` -> `fact_costs[employee_id]`
  - `fact_productivity[date]` -> `fact_costs[date]`
  - `fact_productivity[team]` -> `fact_quality[team]`
  - `fact_productivity[project]` -> `fact_quality[project]`
  - `fact_productivity[date]` -> `fact_quality[date]`

## Page 1: Executive Overview
- KPI cards:
  - Time Saved %
  - Productivity Increase %
  - Error Reduction %
  - ROI %
- Trend chart: `year_month` vs output units and defects
- Waterfall chart: benefits vs costs

## Page 2: Productivity Detail
- Clustered bar by role/team:
  - features delivered
  - test cases written
  - task hours
- Scatter plot:
  - X: AI usage events
  - Y: output units
  - Legend: role
- Table:
  - team/project level productivity change

## Page 3: Quality and Risk
- Line chart: defects trend by severity
- Line chart: rework hours trend
- Matrix:
  - high AI usage + defect/reopen signals

## Global Filters
- Date range
- Team
- Project
- Role
- AI usage level
- Period (`pre_ai`, `post_ai`)

## Executive Notes Panel
- Pull values from `fact_stats_results`:
  - p-value
  - effect size
- Add conditional formatting for significance threshold (0.05)
