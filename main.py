import argparse

import pandas as pd

from src.config import load_settings
from src.etl import build_facts, load_raw_data
from src.export import export_tables
from src.metrics import compute_kpis
from src.roi import compute_roi
from src.sample_data import generate_sample_data
from src.stats import run_ai_correlation, run_before_after_tests


def run_pipeline() -> None:
    settings = load_settings()
    raw_data = load_raw_data()
    fact_productivity, fact_quality, fact_costs = build_facts(raw_data, settings)

    kpi_summary = compute_kpis(fact_productivity, fact_quality)
    stats_before_after = run_before_after_tests(fact_productivity, group_key="employee_id")
    stats_corr = run_ai_correlation(fact_productivity, group_key="employee_id")
    fact_stats_results = pd.concat([stats_before_after, stats_corr], ignore_index=True).reset_index(drop=True)
    roi_summary = compute_roi(fact_productivity, fact_quality, fact_costs)

    export_tables(
        {
            "fact_productivity": fact_productivity,
            "fact_quality": fact_quality,
            "fact_costs": fact_costs,
            "fact_stats_results": fact_stats_results,
            "kpi_summary": kpi_summary,
            "roi_summary": roi_summary,
        }
    )


def parse_args():
    parser = argparse.ArgumentParser(description="AI productivity impact analytics pipeline")
    parser.add_argument(
        "--generate-sample",
        action="store_true",
        help="Generate synthetic raw data in data/raw before running pipeline",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.generate_sample:
        generate_sample_data()
    run_pipeline()
    print("Pipeline completed. Outputs written to data/processed/")
