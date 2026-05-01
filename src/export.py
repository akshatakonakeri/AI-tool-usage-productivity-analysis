from pathlib import Path
from typing import Dict

import pandas as pd


def export_tables(tables: Dict[str, pd.DataFrame], out_dir: str = "data/processed") -> None:
    target = Path(out_dir)
    target.mkdir(parents=True, exist_ok=True)
    for name, df in tables.items():
        df.to_csv(target / f"{name}.csv", index=False)
