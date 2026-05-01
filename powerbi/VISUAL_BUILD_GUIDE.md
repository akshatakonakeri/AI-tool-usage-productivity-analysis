# Power BI Visual Build Guide (Exact Mapping)

Use this guide after importing all `data/processed/*.csv` files.

## 0) Model Setup

Create these relationships (many-to-one where applicable):
- `fact_productivity[date]` -> `fact_quality[date]`
- `fact_productivity[team]` -> `fact_quality[team]`
- `fact_productivity[project]` -> `fact_quality[project]`
- `fact_productivity[date]` -> `fact_costs[date]`
- `fact_productivity[employee_id]` -> `fact_costs[employee_id]`

Set cross-filter direction to Single unless you need bidirectional behavior.

## 1) Page: Executive Overview

Page size: 16:9.  
Top row = KPI cards, middle = trends, bottom = ROI waterfall.

### Visual 1: KPI Card - Time Saved %
- Visual type: Card
- Field: measure `Time Saved %`
- Title: `Time Saved %`
- Format: Percentage with 1 decimal

### Visual 2: KPI Card - Productivity Increase %
- Visual type: Card
- Field: measure `Productivity Increase %`
- Title: `Productivity Increase %`
- Format: Percentage with 1 decimal

### Visual 3: KPI Card - Error Reduction %
- Visual type: Card
- Field: measure `Error Reduction %`
- Title: `Error Reduction %`
- Format: Percentage with 1 decimal

### Visual 4: KPI Card - ROI %
- Visual type: Card
- Field: measure `ROI %`
- Title: `ROI %`
- Format: Percentage with 1 decimal

### Visual 5: Trend - Output Over Time
- Visual type: Line chart
- X-axis: `fact_productivity[year_month]`
- Y-axis: measure `Output Units`
- Legend: `fact_productivity[period]`
- Title: `Output Trend (Pre vs Post AI)`

### Visual 6: Trend - Defects Over Time
- Visual type: Line chart
- X-axis: `fact_quality[year_month]`
- Y-axis: measure `Defects Total`
- Legend: `fact_quality[period]`
- Title: `Defect Trend (Pre vs Post AI)`

### Visual 7: ROI Waterfall
- Visual type: Waterfall chart
- Category: Create a small disconnected table with labels:
  - `Time Saved Value`
  - `Productivity Gain Value`
  - `Rework Savings Value`
  - `AI Tool Costs`
- Y value: mapped measure per category (recommended via SWITCH measure)
- Title: `ROI Bridge: Benefits vs Costs`

## 2) Page: Productivity Deep Dive

### Visual 1: Clustered Column - Output by Role
- Visual type: Clustered column chart
- X-axis: `fact_productivity[role]`
- Y-axis: measure `Output Units`
- Legend: `fact_productivity[period]`
- Title: `Output by Role`

### Visual 2: Clustered Bar - Task Hours by Team
- Visual type: Clustered bar chart
- Y-axis: `fact_productivity[team]`
- X-axis: `Total Task Hours`
- Legend: `fact_productivity[period]`
- Title: `Task Hours by Team`

### Visual 3: Scatter - AI Usage vs Output
- Visual type: Scatter chart
- X-axis: average of `fact_productivity[ai_usage_events]`
- Y-axis: measure `Output Units`
- Details: `fact_productivity[employee_id]`
- Legend: `fact_productivity[role]`
- Size: `fact_productivity[tasks_completed]`
- Title: `AI Usage vs Productivity`

### Visual 4: Matrix - Team Project Productivity
- Visual type: Matrix
- Rows: `fact_productivity[team]`
- Columns: `fact_productivity[project]`
- Values:
  - `Output Units`
  - `Total Task Hours`
  - `Productivity Increase %`
- Conditional formatting:
  - Green for positive productivity increase
  - Red for negative

## 3) Page: Quality and Risk

### Visual 1: Line - Defect Severity Trend
- Visual type: Line chart
- X-axis: `fact_quality[year_month]`
- Y-axis: `Defects Total` and sum of `fact_quality[defects_sev1]`
- Title: `Defect and Critical Defect Trend`

### Visual 2: Line - Rework Hours
- Visual type: Line chart
- X-axis: `fact_quality[year_month]`
- Y-axis: sum of `fact_quality[rework_hours]`
- Legend: `fact_quality[period]`
- Title: `Rework Hours Trend`

### Visual 3: Table - Over-Reliance Watchlist
- Visual type: Table
- Columns:
  - `fact_productivity[employee_id]`
  - `fact_productivity[team]`
  - average `fact_productivity[ai_usage_events]`
  - `Output Units`
  - `Defects Total`
  - sum `fact_quality[reopen_count]`
- Filter logic:
  - AI usage in top quartile
  - Defects or reopen increasing in post period
- Title: `Potential Over-Reliance Signals`

### Visual 4: Stats Summary Table
- Visual type: Table
- Source: `fact_stats_results`
- Columns:
  - `metric_name`
  - `test`
  - `p_value`
  - `effect_size`
- Conditional formatting:
  - `p_value < 0.05` highlight green
  - `|effect_size| < 0.1` highlight gray

## 4) Global Slicers (Add to Every Page)

- `fact_productivity[year_month]` (Between or Dropdown)
- `fact_productivity[team]`
- `fact_productivity[project]`
- `fact_productivity[role]`
- `fact_productivity[ai_usage_level]`
- `fact_productivity[period]`

Sync slicers across all pages (View -> Sync slicers).

## 5) Visual Interaction Rules

Use `Format -> Edit interactions`:
- Slicers should filter all visuals.
- Scatter chart should cross-filter matrix and watchlist.
- KPI cards should respond to slicers but not to row-level table selection.

## 6) Executive-Ready Formatting

- Theme: neutral background, one accent color for post-AI.
- Color standard:
  - Pre-AI = gray
  - Post-AI = blue
  - Risk/negative = red
  - Improvement/positive = green
- Use consistent decimal places:
  - % KPIs = 1 decimal
  - currency = no decimals
  - hours = 1 decimal

## 7) Publish Checklist

- Confirm all measures return values under filters.
- Validate totals against `kpi_summary.csv` and `roi_summary.csv`.
- Check top leadership questions:
  - Is productivity really up?
  - Is quality stable or better?
  - Is ROI positive and sustainable?
- Publish to Power BI Service and schedule refresh after Python pipeline run.
