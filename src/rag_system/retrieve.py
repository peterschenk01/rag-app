from __future__ import annotations

import faiss

from rag_system.index import FaissStore, embed_texts


def retrieve(store: FaissStore, query: str, k: int = 2) -> list[tuple[str, float]]:
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
