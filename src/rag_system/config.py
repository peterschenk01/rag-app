from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"
DATA_PATH = DATA_DIR / "cat-facts.txt"

STORAGE_DIR = ROOT_DIR / "storage"

DATA_URL = "https://huggingface.co/ngxson/demo_simple_rag_py/resolve/main/cat-facts.txt"

EMBEDDING_MODEL = "hf.co/CompendiumLabs/bge-base-en-v1.5-gguf"
LANGUAGE_MODEL = "hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF"
