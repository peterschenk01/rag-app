import urllib.request
from rag_app.config import DATA_PATH

DATA_URL = (
    "https://huggingface.co/ngxson/demo_simple_rag_py/"
    "resolve/main/cat-facts.txt"
)


def ensure_data_exists() -> None:
    if DATA_PATH.exists():
        print(f"Dataset already exists at: {DATA_PATH}")
        return

    print(f"Dataset not found. Downloading from: {DATA_URL}")

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(DATA_URL, DATA_PATH)


def chunk_dataset(dataset: list[str]) -> list[str]:
    chunks = dataset  # one line = one chunk
    return chunks


def load_dataset() -> list[str]:
    print("Loading dataset...")
    ensure_data_exists()

    with DATA_PATH.open("r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    chunks = chunk_dataset(lines)

    print(f"Dataset loaded.")
    return chunks