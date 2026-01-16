from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"
DATA_PATH = DATA_DIR / "cat-facts.txt"

STORAGE_DIR = ROOT_DIR / "storage"