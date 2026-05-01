from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd


def _safe_read_csv(path: Path, required: bool = True) -> pd.DataFrame:
    if path.exists():
        return pd.read_csv(path)
    if required:
        raise FileNotFoundError(f"Required input file missing: {path}")
    return pd.DataFrame()


def load_raw_data(raw_dir: str = "data/raw") -> Dict[str, pd.DataFrame]:
    base = Path(raw_dir)
    return {
        "tasks": _safe_read_csv(base / "task_logs.csv"),
        "dev": _safe_read_csv(base / "developer_metrics.csv"),
        "bugs": _safe_read_csv(base / "bug_tracking.csv"),
        "costs": _safe_read_csv(base / "employee_costs.csv"),
        "ai": _safe_read_csv(base / "ai_usage.csv"),
    }


def build_facts(data: Dict[str, pd.DataFrame], settings: Dict) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rollout_date = pd.Timestamp(settings["rollout_date"])
    default_hourly_cost = float(settings.get("default_hourly_cost", 50.0))

    tasks = data["tasks"].copy()
    dev = data["dev"].copy()
    ai = data["ai"].copy()
    costs = data["costs"].copy()
    bugs = data["bugs"].copy()

    for df in [tasks, dev, ai, costs, bugs]:
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"])

    fact_productivity = (
        tasks.merge(dev, on=["date", "employee_id"], how="left")
        .merge(ai, on=["date", "employee_id"], how="left")
        .merge(costs[["date", "employee_id", "hourly_cost"]], on=["date", "employee_id"], how="left")
    )

    if "hourly_cost" not in fact_productivity.columns:
        fact_productivity["hourly_cost"] = default_hourly_cost
    fact_productivity["hourly_cost"] = fact_productivity["hourly_cost"].fillna(default_hourly_cost)
    fact_productivity["ai_usage_events"] = fact_productivity.get("ai_usage_events", 0).fillna(0)
    fact_productivity["period"] = np.where(fact_productivity["date"] < rollout_date, "pre_ai", "post_ai")
    fact_productivity["year_month"] = fact_productivity["date"].dt.to_period("M").astype(str)
    fact_productivity["tasks_completed"] = fact_productivity.get("tasks_completed", 0).fillna(0)
    fact_productivity["features_delivered"] = fact_productivity.get("features_delivered", 0).fillna(0)
    fact_productivity["test_cases_written"] = fact_productivity.get("test_cases_written", 0).fillna(0)
    fact_productivity["task_hours"] = fact_productivity.get("task_hours", 0).fillna(0)

    quantiles = fact_productivity["ai_usage_events"].quantile([0.33, 0.66]).values
    low, high = quantiles[0], quantiles[1]
    fact_productivity["ai_usage_level"] = np.select(
        [
            fact_productivity["ai_usage_events"] <= low,
            fact_productivity["ai_usage_events"] <= high,
        ],
        ["Low", "Medium"],
        default="High",
    )

    fact_quality = bugs.copy()
    fact_quality["period"] = np.where(fact_quality["date"] < rollout_date, "pre_ai", "post_ai")
    fact_quality["year_month"] = fact_quality["date"].dt.to_period("M").astype(str)

    fact_costs = costs.copy()
    fact_costs["period"] = np.where(fact_costs["date"] < rollout_date, "pre_ai", "post_ai")
    fact_costs["year_month"] = fact_costs["date"].dt.to_period("M").astype(str)

    return fact_productivity, fact_quality, fact_costs
