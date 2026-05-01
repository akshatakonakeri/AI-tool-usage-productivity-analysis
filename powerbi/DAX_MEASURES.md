# Power BI DAX Starter Measures

```DAX
Total Task Hours = SUM(fact_productivity[task_hours])

Baseline Task Hours =
CALCULATE(
    MEDIAN(fact_productivity[task_hours]),
    fact_productivity[period] = "pre_ai"
)

Time Saved Hours =
SUMX(
    fact_productivity,
    MAX(0, [Baseline Task Hours] - fact_productivity[task_hours])
)

Time Saved % =
DIVIDE([Time Saved Hours], [Baseline Task Hours] * COUNTROWS(fact_productivity))

Output Units =
SUM(fact_productivity[features_delivered]) + SUM(fact_productivity[test_cases_written])

Output Units Pre =
CALCULATE([Output Units], fact_productivity[period] = "pre_ai")

Output Units Post =
CALCULATE([Output Units], fact_productivity[period] = "post_ai")

Productivity Increase % =
DIVIDE([Output Units Post] - [Output Units Pre], [Output Units Pre])

Defects Total = SUM(fact_quality[defects_total])

Defects Pre =
CALCULATE([Defects Total], fact_quality[period] = "pre_ai")

Defects Post =
CALCULATE([Defects Total], fact_quality[period] = "post_ai")

Error Reduction % =
DIVIDE([Defects Pre] - [Defects Post], [Defects Pre])

AI Tool Costs =
SUM(fact_costs[ai_license_cost_allocated]) + SUM(fact_costs[training_cost_allocated])

Rework Savings Value =
VAR PreRework =
    CALCULATE(SUM(fact_quality[rework_hours]), fact_quality[period] = "pre_ai")
VAR PostRework =
    CALCULATE(SUM(fact_quality[rework_hours]), fact_quality[period] = "post_ai")
VAR AvgHourly = AVERAGE(fact_costs[hourly_cost])
RETURN MAX(0, PreRework - PostRework) * AvgHourly

Total Benefits Value =
VAR TimeSavingsVal = [Time Saved Hours] * AVERAGE(fact_costs[hourly_cost])
VAR ProdGainVal = MAX(0, [Output Units Post] - [Output Units Pre]) * 0.25 * AVERAGE(fact_costs[hourly_cost])
RETURN TimeSavingsVal + ProdGainVal + [Rework Savings Value]

ROI % =
DIVIDE([Total Benefits Value] - [AI Tool Costs], [AI Tool Costs])
```
