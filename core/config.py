from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONTEXT_PATH = DATA_DIR / "context.json"
USER_PROFILE_PATH = DATA_DIR / "user_profile.json"

with open(CONTEXT_PATH, "r", encoding="utf-8") as f:
    CONTEXT = json.load(f)

with open(USER_PROFILE_PATH, "r", encoding="utf-8") as f:
    USER_PROFILE = json.load(f)