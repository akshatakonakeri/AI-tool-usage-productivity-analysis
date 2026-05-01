import pandas as pd


def compute_kpis(fact_productivity: pd.DataFrame, fact_quality: pd.DataFrame) -> pd.DataFrame:
    pre_prod = fact_productivity[fact_productivity["period"] == "pre_ai"]
    post_prod = fact_productivity[fact_productivity["period"] == "post_ai"]
    pre_qual = fact_quality[fact_quality["period"] == "pre_ai"]
    post_qual = fact_quality[fact_quality["period"] == "post_ai"]

    pre_task_time = pre_prod["task_hours"].median() if not pre_prod.empty else 0
    post_task_time = post_prod["task_hours"].median() if not post_prod.empty else 0
    time_saved_pct = ((pre_task_time - post_task_time) / pre_task_time * 100) if pre_task_time else 0

    pre_output = (
        (pre_prod["features_delivered"].sum() + pre_prod["test_cases_written"].sum()) / max(pre_prod["employee_id"].nunique(), 1)
        if not pre_prod.empty
        else 0
    )
    post_output = (
        (post_prod["features_delivered"].sum() + post_prod["test_cases_written"].sum()) / max(post_prod["employee_id"].nunique(), 1)
        if not post_prod.empty
        else 0
    )
    productivity_pct = ((post_output - pre_output) / pre_output * 100) if pre_output else 0

    pre_defect_rate = pre_qual["defects_total"].mean() if not pre_qual.empty else 0
    post_defect_rate = post_qual["defects_total"].mean() if not post_qual.empty else 0
    error_reduction_pct = ((pre_defect_rate - post_defect_rate) / pre_defect_rate * 100) if pre_defect_rate else 0

    return pd.DataFrame(
        [
            {"kpi_name": "Time Saved %", "value": round(time_saved_pct, 2)},
            {"kpi_name": "Productivity Increase %", "value": round(productivity_pct, 2)},
            {"kpi_name": "Error Reduction %", "value": round(error_reduction_pct, 2)},
            {"kpi_name": "Median Task Time (Pre)", "value": round(pre_task_time, 2)},
            {"kpi_name": "Median Task Time (Post)", "value": round(post_task_time, 2)},
        ]
    )
