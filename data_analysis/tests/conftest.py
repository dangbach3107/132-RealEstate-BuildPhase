from pathlib import Path
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ["VALUATION_LLM_ENABLED"] = "0"
os.environ["VALUATION_STORAGE_BACKEND"] = "sqlite"
