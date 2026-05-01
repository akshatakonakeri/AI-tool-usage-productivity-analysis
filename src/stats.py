from typing import List

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, ttest_rel, wilcoxon


def _cohens_d(x: pd.Series, y: pd.Series) -> float:
    diff = x - y
    std = diff.std(ddof=1)
    if std == 0 or np.isnan(std):
        return 0.0
    return diff.mean() / std


def run_before_after_tests(fact_productivity: pd.DataFrame, group_key: str = "employee_id") -> pd.DataFrame:
    per_unit = (
        fact_productivity.groupby([group_key, "period"], as_index=False)["task_hours"]
        .mean()
        .pivot(index=group_key, columns="period", values="task_hours")
        .dropna()
    )
    if per_unit.empty or "pre_ai" not in per_unit.columns or "post_ai" not in per_unit.columns:
        return pd.DataFrame(
            [
                {
                    "metric_name": "task_hours",
                    "group": "overall",
                    "pre_mean": 0.0,
                    "post_mean": 0.0,
                    "pct_change": 0.0,
                    "test": "none",
                    "p_value": 1.0,
                    "effect_size": 0.0,
                }
            ]
        )

    pre = per_unit["pre_ai"]
    post = per_unit["post_ai"]
    _, t_p = ttest_rel(pre, post, nan_policy="omit")
    try:
        _, w_p = wilcoxon(pre, post)
    except ValueError:
        w_p = 1.0

    return pd.DataFrame(
        [
            {
                "metric_name": "task_hours",
                "group": "overall",
                "pre_mean": round(pre.mean(), 4),
                "post_mean": round(post.mean(), 4),
                "pct_change": round(((pre.mean() - post.mean()) / pre.mean() * 100) if pre.mean() else 0, 4),
                "test": "paired_t_and_wilcoxon",
                "p_value": round(float(min(t_p, w_p)), 6),
                "effect_size": round(_cohens_d(pre, post), 4),
            }
        ]
    )


def run_ai_correlation(fact_productivity: pd.DataFrame, group_key: str = "employee_id") -> pd.DataFrame:
    grouped = fact_productivity.groupby(group_key, as_index=False).agg(
        ai_usage_events=("ai_usage_events", "mean"),
        task_hours=("task_hours", "mean"),
        features_delivered=("features_delivered", "mean"),
        test_cases_written=("test_cases_written", "mean"),
    )
    grouped["combined_output"] = grouped["features_delivered"] + grouped["test_cases_written"]

    out_rows: List[dict] = []
    for metric in ["task_hours", "combined_output"]:
        if grouped[metric].nunique() <= 1 or grouped["ai_usage_events"].nunique() <= 1:
            corr, pval = 0.0, 1.0
        else:
            corr, pval = pearsonr(grouped["ai_usage_events"], grouped[metric])
        out_rows.append(
            {
                "metric_name": f"ai_usage_vs_{metric}",
                "group": "overall",
                "pre_mean": 0.0,
                "post_mean": 0.0,
                "pct_change": 0.0,
                "test": "pearson",
                "p_value": round(float(pval), 6),
                "effect_size": round(float(corr), 4),
            }
        )
    return pd.DataFrame(out_rows)
