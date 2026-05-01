from pathlib import Path
import numpy as np
import pandas as pd


def _date_range():
    return pd.date_range("2024-09-01", "2025-04-30", freq="D")


def generate_sample_data(raw_dir: str = "data/raw") -> None:
    np.random.seed(42)
    root = Path(raw_dir)
    root.mkdir(parents=True, exist_ok=True)

    employees = [f"E{idx:03d}" for idx in range(1, 41)]
    roles = ["Developer", "Tester"]
    teams = ["Platform", "Payments", "CoreApp", "Data"]
    projects = ["Apollo", "Nova", "Orion"]
    dates = _date_range()
    rollout_date = pd.Timestamp("2025-01-01")

    rows = []
    for d in dates:
        for e in employees:
            role = np.random.choice(roles, p=[0.7, 0.3])
            team = np.random.choice(teams)
            project = np.random.choice(projects)
            period_factor = 0.82 if d >= rollout_date else 1.0
            complexity = np.random.choice(["Low", "Medium", "High"], p=[0.3, 0.5, 0.2])
            complexity_factor = {"Low": 0.8, "Medium": 1.0, "High": 1.3}[complexity]
            task_hours = max(0.3, np.random.normal(3.5, 1.2) * period_factor * complexity_factor)
            rows.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "employee_id": e,
                    "team": team,
                    "role": role,
                    "project": project,
                    "complexity": complexity,
                    "task_hours": round(task_hours, 2),
                    "tasks_completed": int(max(1, np.random.poisson(3))),
                }
            )
    task_logs = pd.DataFrame(rows)
    task_logs.to_csv(root / "task_logs.csv", index=False)

    dev_rows = []
    for d in dates:
        for e in employees:
            commits = int(max(0, np.random.poisson(2)))
            prs = int(max(0, np.random.poisson(1)))
            features = int(max(0, np.random.binomial(2, 0.35)))
            test_cases = int(max(0, np.random.poisson(3)))
            dev_rows.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "employee_id": e,
                    "commits": commits,
                    "prs_opened": prs,
                    "features_delivered": features,
                    "test_cases_written": test_cases,
                }
            )
    pd.DataFrame(dev_rows).to_csv(root / "developer_metrics.csv", index=False)

    bug_rows = []
    for d in dates:
        for t in teams:
            base = np.random.poisson(10)
            post_factor = 0.75 if d >= rollout_date else 1.0
            defects = int(max(0, base * post_factor))
            bug_rows.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "team": t,
                    "project": np.random.choice(projects),
                    "defects_total": defects,
                    "defects_sev1": int(np.random.binomial(max(defects, 1), 0.08)),
                    "reopen_count": int(np.random.binomial(max(defects, 1), 0.12)),
                    "rework_hours": round(max(0, np.random.normal(35, 12) * post_factor), 2),
                }
            )
    pd.DataFrame(bug_rows).to_csv(root / "bug_tracking.csv", index=False)

    cost_rows = []
    for d in dates:
        for e in employees:
            role = np.random.choice(roles, p=[0.7, 0.3])
            hourly = 58 if role == "Developer" else 42
            cost_rows.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "employee_id": e,
                    "role": role,
                    "hourly_cost": hourly,
                    "ai_license_cost_allocated": 1.8,
                    "training_cost_allocated": 0.6 if d < rollout_date + pd.Timedelta(days=45) else 0.2,
                }
            )
    pd.DataFrame(cost_rows).to_csv(root / "employee_costs.csv", index=False)

    ai_rows = []
    for d in dates:
        for e in employees:
            usage = np.random.poisson(2 if d < rollout_date else 7)
            ai_rows.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "employee_id": e,
                    "ai_usage_events": int(usage),
                }
            )
    pd.DataFrame(ai_rows).to_csv(root / "ai_usage.csv", index=False)
