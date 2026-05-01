import json
from pathlib import Path
from typing import Any, Dict


def load_settings(path: str = "config/settings.json") -> Dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Settings file not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as fp:
        return json.load(fp)
