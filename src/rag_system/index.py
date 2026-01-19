from __future__ import annotations

from dataclasses import dataclass

import faiss
import numpy as np
import ollama

from rag_system.config import EMBEDDING_MODEL


@dataclass
class FaissStore:
    index: faiss.Index
    chunks: list[str]


def embed_texts(texts: list[str]) -> np.ndarray:
    resp = ollama.embed(model=EMBEDDING_MODEL, input=texts)
    embs = np.array(resp["embeddings"], dtype="float32")  # (N, D)
    return embs


def build_faiss_store(chunks: list[str]) -> FaissStore:
    print("Building FAISS store...")

    vectors = embed_texts(chunks)  # (N, D)

    if vectors.ndim != 2 or vectors.shape[0] == 0:
        raise ValueError("No embeddings returned.")

    dim = vectors.shape[1]

    # cosine similarity
    faiss.normalize_L2(vectors)
    index = faiss.IndexFlatIP(dim)

    index.add(vectors)

    return FaissStore(index=index, chunks=chunks)


def search(store: FaissStore, query: str, k: int = 5) -> list[tuple[str, float]]:
    print(f'Searching store with query: "{query}"')
    print(f"Retrieving top {k} results...")

    q = embed_texts([query])  # (1, D)
    faiss.normalize_L2(q)

    scores, ids = store.index.search(q, k)

    results: list[tuple[str, float]] = []

    for idx, score in zip(ids[0].tolist(), scores[0].tolist(), strict=True):
        if idx == -1:
            continue
        results.append((store.chunks[idx], float(score)))

    print(f"Retrieved {len(results)} result(s).")

    return results
