from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONTEXT_PATH = DATA_DIR / "context.json"

with open(CONTEXT_PATH, "r", encoding="utf-8") as f:
    CONTEXT = json.load(f)

