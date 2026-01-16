from rag_app.config import STORAGE_DIR
from rag_app.ingest import load_dataset
from rag_app.index import build_faiss_index, search
from rag_app.persist import load_store, save_store, store_exists

def main():
    if store_exists(STORAGE_DIR):
        store = load_store(STORAGE_DIR)
    else:
        dataset = load_dataset()

        store = build_faiss_index(dataset)
        save_store(store, STORAGE_DIR)

    hits = search(store, "How much do cats sleep?")


if __name__ == "__main__":
    main()