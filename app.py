from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="AI Productivity Impact Dashboard", layout="wide")

DATA_DIR = Path("data/processed")


@st.cache_data
def load_data():
    fp = pd.read_csv(DATA_DIR / "fact_productivity.csv")
    fq = pd.read_csv(DATA_DIR / "fact_quality.csv")
    fs = pd.read_csv(DATA_DIR / "fact_stats_results.csv")
    ks = pd.read_csv(DATA_DIR / "kpi_summary.csv")
    rs = pd.read_csv(DATA_DIR / "roi_summary.csv")
    fp["date"] = pd.to_datetime(fp["date"])
    fq["date"] = pd.to_datetime(fq["date"])
    return fp, fq, fs, ks, rs


def metric_value(df: pd.DataFrame, key_col: str, val_col: str, key: str, default: float = 0.0) -> float:
    matches = df.loc[df[key_col] == key, val_col]
    return float(matches.iloc[0]) if not matches.empty else default


def main():
    st.title("AI Productivity Impact Dashboard")
    st.caption("Hybrid analytics view for AI adoption impact on productivity, quality, and ROI.")

    if not DATA_DIR.exists():
        st.error("Processed data folder not found. Run `python main.py` first.")
        st.stop()

    fp, fq, fs, ks, rs = load_data()

    with st.sidebar:
        st.header("Filters")
        teams = st.multiselect("Team", sorted(fp["team"].dropna().unique().tolist()))
        projects = st.multiselect("Project", sorted(fp["project"].dropna().unique().tolist()))
        roles = st.multiselect("Role", sorted(fp["role"].dropna().unique().tolist()))
        usage = st.multiselect("AI Usage Level", sorted(fp["ai_usage_level"].dropna().unique().tolist()))
        date_min = min(fp["date"].min(), fq["date"].min())
        date_max = max(fp["date"].max(), fq["date"].max())
        date_range = st.date_input("Date Range", value=(date_min, date_max), min_value=date_min, max_value=date_max)

    fp_filtered = fp.copy()
    fq_filtered = fq.copy()

    if teams:
        fp_filtered = fp_filtered[fp_filtered["team"].isin(teams)]
        fq_filtered = fq_filtered[fq_filtered["team"].isin(teams)]
    if projects:
        fp_filtered = fp_filtered[fp_filtered["project"].isin(projects)]
        fq_filtered = fq_filtered[fq_filtered["project"].isin(projects)]
    if roles:
        fp_filtered = fp_filtered[fp_filtered["role"].isin(roles)]
    if usage:
        fp_filtered = fp_filtered[fp_filtered["ai_usage_level"].isin(usage)]
    if isinstance(date_range, tuple) and len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        fp_filtered = fp_filtered[(fp_filtered["date"] >= start_date) & (fp_filtered["date"] <= end_date)]
        fq_filtered = fq_filtered[(fq_filtered["date"] >= start_date) & (fq_filtered["date"] <= end_date)]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Time Saved %", f"{metric_value(ks, 'kpi_name', 'value', 'Time Saved %'):.2f}%")
    c2.metric("Productivity Increase %", f"{metric_value(ks, 'kpi_name', 'value', 'Productivity Increase %'):.2f}%")
    c3.metric("Error Reduction %", f"{metric_value(ks, 'kpi_name', 'value', 'Error Reduction %'):.2f}%")
    c4.metric("ROI %", f"{metric_value(rs, 'metric', 'value', 'roi_pct'):.2f}%")

    st.subheader("Trend Analysis")
    t1, t2 = st.columns(2)
    prod_trend = (
        fp_filtered.groupby(["year_month", "period"], as_index=False)[["features_delivered", "test_cases_written"]].sum()
    )
    prod_trend["output_units"] = prod_trend["features_delivered"] + prod_trend["test_cases_written"]
    fig_prod = px.line(
        prod_trend,
        x="year_month",
        y="output_units",
        color="period",
        markers=True,
        title="Output Trend (Pre vs Post AI)",
    )
    t1.plotly_chart(fig_prod, use_container_width=True)

    qual_trend = fq_filtered.groupby(["year_month", "period"], as_index=False)["defects_total"].sum()
    fig_qual = px.line(
        qual_trend,
        x="year_month",
        y="defects_total",
        color="period",
        markers=True,
        title="Defect Trend (Pre vs Post AI)",
    )
    t2.plotly_chart(fig_qual, use_container_width=True)

    st.subheader("Role Productivity Breakdown")
    role_breakdown = fp_filtered.groupby(["role", "period"], as_index=False)[["features_delivered", "test_cases_written"]].sum()
    role_breakdown["output_units"] = role_breakdown["features_delivered"] + role_breakdown["test_cases_written"]
    fig_role = px.bar(
        role_breakdown,
        x="role",
        y="output_units",
        color="period",
        barmode="group",
        title="Output by Role",
    )
    st.plotly_chart(fig_role, use_container_width=True)

    st.subheader("Quality and Risk")
    q1, q2 = st.columns(2)
    fig_rework = px.line(
        fq_filtered.groupby(["year_month", "period"], as_index=False)["rework_hours"].sum(),
        x="year_month",
        y="rework_hours",
        color="period",
        markers=True,
        title="Rework Hours Trend",
    )
    q1.plotly_chart(fig_rework, use_container_width=True)

    scatter_df = fp_filtered.groupby(["employee_id", "role"], as_index=False).agg(
        ai_usage_events=("ai_usage_events", "mean"),
        output_units=("features_delivered", "sum"),
        test_units=("test_cases_written", "sum"),
    )
    scatter_df["output_units"] = scatter_df["output_units"] + scatter_df["test_units"]
    fig_scatter = px.scatter(
        scatter_df,
        x="ai_usage_events",
        y="output_units",
        color="role",
        title="AI Usage vs Output",
    )
    q2.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("ROI Panel")
    r1, r2, r3 = st.columns(3)
    r1.metric("Total Benefits", f"${metric_value(rs, 'metric', 'value', 'total_benefits'):,.2f}")
    r2.metric("Total Costs", f"${metric_value(rs, 'metric', 'value', 'total_costs'):,.2f}")
    r3.metric("Payback (Months)", f"{metric_value(rs, 'metric', 'value', 'payback_months'):.2f}")

    bridge = pd.DataFrame(
        {
            "component": ["Time Saved", "Productivity Gain", "Rework Savings", "AI Tool Costs"],
            "value": [
                metric_value(rs, "metric", "value", "time_saved_value"),
                metric_value(rs, "metric", "value", "productivity_gain_value"),
                metric_value(rs, "metric", "value", "rework_savings_value"),
                -metric_value(rs, "metric", "value", "total_costs"),
            ],
        }
    )
    fig_bridge = px.bar(bridge, x="component", y="value", title="Benefits vs Costs Bridge")
    st.plotly_chart(fig_bridge, use_container_width=True)

    st.subheader("Statistical Results")
    st.dataframe(fs, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
