# Power BI Measure Library (Copy-Paste DAX)

Create these in Power BI under `Modeling -> New measure`.

## 1) Base Measures

```DAX
Total Task Hours =
SUM(fact_productivity[task_hours])
```

```DAX
Tasks Completed =
SUM(fact_productivity[tasks_completed])
```

```DAX
Features Delivered =
SUM(fact_productivity[features_delivered])
```

```DAX
Test Cases Written =
SUM(fact_productivity[test_cases_written])
```

```DAX
Output Units =
[Features Delivered] + [Test Cases Written]
```

```DAX
Defects Total =
SUM(fact_quality[defects_total])
```

```DAX
Critical Defects =
SUM(fact_quality[defects_sev1])
```

```DAX
Reopen Count =
SUM(fact_quality[reopen_count])
```

```DAX
Rework Hours =
SUM(fact_quality[rework_hours])
```

```DAX
Average Hourly Cost =
AVERAGE(fact_costs[hourly_cost])
```

```DAX
AI Tool Costs =
SUM(fact_costs[ai_license_cost_allocated]) + SUM(fact_costs[training_cost_allocated])
```

```DAX
AI Usage Events =
SUM(fact_productivity[ai_usage_events])
```

```DAX
Avg AI Usage Events =
AVERAGE(fact_productivity[ai_usage_events])
```

## 2) Pre/Post Split Measures

```DAX
Output Units Pre =
CALCULATE([Output Units], fact_productivity[period] = "pre_ai")
```

```DAX
Output Units Post =
CALCULATE([Output Units], fact_productivity[period] = "post_ai")
```

```DAX
Task Hours Pre =
CALCULATE([Total Task Hours], fact_productivity[period] = "pre_ai")
```

```DAX
Task Hours Post =
CALCULATE([Total Task Hours], fact_productivity[period] = "post_ai")
```

```DAX
Defects Pre =
CALCULATE([Defects Total], fact_quality[period] = "pre_ai")
```

```DAX
Defects Post =
CALCULATE([Defects Total], fact_quality[period] = "post_ai")
```

```DAX
Rework Hours Pre =
CALCULATE([Rework Hours], fact_quality[period] = "pre_ai")
```

```DAX
Rework Hours Post =
CALCULATE([Rework Hours], fact_quality[period] = "post_ai")
```

## 3) KPI Measures

```DAX
Productivity Increase % =
DIVIDE([Output Units Post] - [Output Units Pre], [Output Units Pre])
```

```DAX
Error Reduction % =
DIVIDE([Defects Pre] - [Defects Post], [Defects Pre])
```

```DAX
Baseline Task Hours Median =
CALCULATE(
    MEDIAN(fact_productivity[task_hours]),
    fact_productivity[period] = "pre_ai"
)
```

```DAX
Time Saved Hours =
SUMX(
    fact_productivity,
    MAX(0, [Baseline Task Hours Median] - fact_productivity[task_hours])
)
```

```DAX
Time Saved % =
DIVIDE(
    [Time Saved Hours],
    [Baseline Task Hours Median] * COUNTROWS(fact_productivity)
)
```

## 4) ROI Measures

```DAX
Time Saved Value =
[Time Saved Hours] * [Average Hourly Cost]
```

```DAX
Productivity Gain Units =
MAX(0, [Output Units Post] - [Output Units Pre])
```

```DAX
Productivity Gain Value =
[Productivity Gain Units] * 0.25 * [Average Hourly Cost]
```

```DAX
Rework Savings Value =
MAX(0, [Rework Hours Pre] - [Rework Hours Post]) * [Average Hourly Cost]
```

```DAX
Total Benefits Value =
[Time Saved Value] + [Productivity Gain Value] + [Rework Savings Value]
```

```DAX
Net Benefit Value =
[Total Benefits Value] - [AI Tool Costs]
```

```DAX
ROI % =
DIVIDE([Net Benefit Value], [AI Tool Costs])
```

```DAX
Payback Months =
DIVIDE([AI Tool Costs], [Total Benefits Value] / 12)
```

## 5) ROI Waterfall Helper

Create a calculated table (`Modeling -> New table`):

```DAX
ROI Bridge =
DATATABLE(
    "Category", STRING,
    {
        {"Time Saved Value"},
        {"Productivity Gain Value"},
        {"Rework Savings Value"},
        {"AI Tool Costs"}
    }
)
```

Then create this measure:

```DAX
ROI Bridge Amount =
SWITCH(
    SELECTEDVALUE('ROI Bridge'[Category]),
    "Time Saved Value", [Time Saved Value],
    "Productivity Gain Value", [Productivity Gain Value],
    "Rework Savings Value", [Rework Savings Value],
    "AI Tool Costs", -1 * [AI Tool Costs],
    BLANK()
)
```

Use:
- Category: `'ROI Bridge'[Category]`
- Y-axis: `[ROI Bridge Amount]`

## 6) Quality Guardrail Measures

```DAX
Reopen Rate =
DIVIDE([Reopen Count], [Defects Total])
```

```DAX
Critical Defect Rate =
DIVIDE([Critical Defects], [Defects Total])
```

```DAX
Post Defect Drift % =
DIVIDE([Defects Post] - [Defects Pre], [Defects Pre])
```

## 7) Over-Reliance Watchlist Flags

```DAX
AI Usage P75 =
PERCENTILEX.INC(
    ALLSELECTED(fact_productivity[employee_id]),
    CALCULATE(AVERAGE(fact_productivity[ai_usage_events])),
    0.75
)
```

```DAX
High AI Usage Flag =
VAR userAI = CALCULATE(AVERAGE(fact_productivity[ai_usage_events]))
RETURN IF(userAI >= [AI Usage P75], 1, 0)
```

```DAX
Defect Drift Flag =
IF([Post Defect Drift %] > 0, 1, 0)
```

```DAX
Over Reliance Flag =
IF([High AI Usage Flag] = 1 && [Defect Drift Flag] = 1, 1, 0)
```

Use `Over Reliance Flag = 1` as a visual-level filter for the watchlist table.

## 8) Statistical Insight Measures (from fact_stats_results)

```DAX
Min P Value =
MIN(fact_stats_results[p_value])
```

```DAX
Max Effect Size =
MAX(fact_stats_results[effect_size])
```

```DAX
Stat Significance Label =
IF([Min P Value] < 0.05, "Significant", "Not Significant")
```

```DAX
Effect Strength Label =
VAR a = ABS([Max Effect Size])
RETURN
SWITCH(
    TRUE(),
    a < 0.1, "Negligible",
    a < 0.3, "Small",
    a < 0.5, "Moderate",
    "Large"
)
```

## 9) Recommended Formatting

- Set all `%` measures to Percentage with 1 decimal.
- Set value measures (`...Value`) to Currency.
- Set `Payback Months` to Decimal Number with 2 decimals.
