from __future__ import annotations

from pathlib import Path
from typing import Any

from rag_app.config import DATA_PATH, EMBEDDING_MODEL, STORAGE_DIR
from rag_app.index import FaissStore, build_faiss_store, search
from rag_app.ingest import load_dataset
from rag_app.manifest import build_manifest, is_compatible, load_manifest, save_manifest
from rag_app.persist import load_store, save_store, store_exists


def make_manifest(*, dataset_path: Path, embedding_dim: int) -> dict[str, Any]:
    return build_manifest(
        dataset_path=dataset_path,
        embedding_model=EMBEDDING_MODEL,
        embedding_dim=embedding_dim,
        metric="cosine",
        chunking_strategy="one-line",
    )


def get_expected_manifest() -> dict[str, Any]:
    return make_manifest(dataset_path=DATA_PATH, embedding_dim=768)


def build_and_persist_store(dataset: list[str]) -> FaissStore:
    store = build_faiss_store(dataset)

    manifest = make_manifest(dataset_path=DATA_PATH, embedding_dim=store.index.d)

    save_store(store, STORAGE_DIR)
    save_manifest(STORAGE_DIR, manifest)
    return store


def get_or_build_store(dataset: list[str]) -> FaissStore:
    expected = get_expected_manifest()

    if store_exists(STORAGE_DIR):
        try:
            stored = load_manifest(STORAGE_DIR)
        except FileNotFoundError:
            print("Manifest missing! Rebuilding FAISS store.")
        else:
            if is_compatible(stored=stored, expected=expected):
                print("Manifest matches! Using persisted FAISS store.")
                return load_store(STORAGE_DIR)

            print("Persisted FAISS store incompatible! Rebuilding...")

    return build_and_persist_store(dataset)


def main():
    dataset = load_dataset()
    store = get_or_build_store(dataset)

    query = "How much do cats sleep?"
    hits = search(store, query, k=5)

    for chunk, score in hits:
        print(f"[{score}] {chunk}")


if __name__ == "__main__":
    main()
