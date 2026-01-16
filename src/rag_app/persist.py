from pathlib import Path
import json
import faiss

from rag_app.index import FaissStore


def store_exists(storage_dir: Path) -> bool:
    index_path = storage_dir / "index.faiss"
    chunks_path = storage_dir / "chunks.json"

    exists = index_path.exists() and chunks_path.exists()

    return exists


def save_store(store: FaissStore, storage_dir: Path) -> None:
    print(f"Storing FAISS store to: {storage_dir}")

    storage_dir.mkdir(parents=True, exist_ok=True)

    faiss.write_index(store.index, str(storage_dir / "index.faiss"))

    (storage_dir / "chunks.json").write_text(
        json.dumps(store.chunks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_store(storage_dir: Path) -> FaissStore:
    print(f"Loading FAISS store from: {storage_dir}")

    index = faiss.read_index(str(storage_dir / "index.faiss"))

    chunks = json.loads(
        (storage_dir / "chunks.json").read_text(encoding="utf-8")
    )

    print(f"Successfully loaded FAISS store.")

    return FaissStore(index=index, chunks=chunks)
