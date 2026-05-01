import pandas as pd


def compute_roi(fact_productivity: pd.DataFrame, fact_quality: pd.DataFrame, fact_costs: pd.DataFrame) -> pd.DataFrame:
    baseline_task_hours = (
        fact_productivity[fact_productivity["period"] == "pre_ai"]["task_hours"].median()
        if not fact_productivity.empty
        else 0.0
    )
    fp = fact_productivity.copy()
    fp["baseline_task_hours"] = baseline_task_hours
    fp["time_saved_hours"] = (fp["baseline_task_hours"] - fp["task_hours"]).clip(lower=0)
    time_saved_value = (fp["time_saved_hours"] * fp["hourly_cost"]).sum()

    pre_output = fp[fp["period"] == "pre_ai"]["features_delivered"].sum() + fp[fp["period"] == "pre_ai"]["test_cases_written"].sum()
    post_output = fp[fp["period"] == "post_ai"]["features_delivered"].sum() + fp[fp["period"] == "post_ai"]["test_cases_written"].sum()
    output_gain_units = max(0.0, float(post_output - pre_output))
    avg_hourly = fp["hourly_cost"].mean() if "hourly_cost" in fp.columns else 50.0
    productivity_gain_value = output_gain_units * 0.25 * avg_hourly

    pre_rework = fact_quality[fact_quality["period"] == "pre_ai"]["rework_hours"].sum() if not fact_quality.empty else 0.0
    post_rework = fact_quality[fact_quality["period"] == "post_ai"]["rework_hours"].sum() if not fact_quality.empty else 0.0
    rework_hours_saved = max(0.0, pre_rework - post_rework)
    rework_savings_value = rework_hours_saved * avg_hourly

    total_benefits = time_saved_value + productivity_gain_value + rework_savings_value
    total_costs = fact_costs.get("ai_license_cost_allocated", pd.Series(dtype=float)).sum() + fact_costs.get(
        "training_cost_allocated", pd.Series(dtype=float)
    ).sum()
    roi_pct = ((total_benefits - total_costs) / total_costs * 100) if total_costs else 0.0
    payback_months = (total_costs / (total_benefits / 12.0)) if total_benefits else 0.0

    return pd.DataFrame(
        [
            {"metric": "time_saved_value", "value": round(float(time_saved_value), 2)},
            {"metric": "productivity_gain_value", "value": round(float(productivity_gain_value), 2)},
            {"metric": "rework_savings_value", "value": round(float(rework_savings_value), 2)},
            {"metric": "total_benefits", "value": round(float(total_benefits), 2)},
            {"metric": "total_costs", "value": round(float(total_costs), 2)},
            {"metric": "roi_pct", "value": round(float(roi_pct), 2)},
            {"metric": "payback_months", "value": round(float(payback_months), 2)},
        ]
    )
