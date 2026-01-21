# Retrieval-Augmented Generation (RAG) System

A **Retrieval-Augmented Generation (RAG)** chatbot built in Python using **FAISS** for vector similarity search and **Ollama** for embeddings and LLM inference.

---

## Project Overview

**Retrieval-Augmented Generation (RAG)** combines classical information retrieval with large language models. Instead of relying solely on the LLM’s internal knowledge, the system retrieves relevant chunks from an external corpus and injects them as context for generation.

This project includes:

- Dataset ingestion and text chunking
- Embedding generation via Ollama
- Vector indexing and similarity search using FAISS
- Persistent FAISS index with manifest-based validation
- Interactive terminal-based chatbot
- Unit tests for each module
- Continuous Integration (CI) workflow
- Pre-commit hooks

---

## Technology Stack

- **FAISS** — vector similarity search
- **Ollama** — embeddings and LLM inference
- **UV** — dependency and environment management
- **Pytest** — testing
- **Ruff** — linting and formatting
- **Pre-commit** — local enforcement of quality checks

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/peterschenk01/rag-system.git
cd rag-system
```

---

### 2. Install dependencies (UV)

```bash
uv sync
```

---

### 3. Ollama Setup

Install Ollama: [https://ollama.com/download](https://ollama.com/download)

Pull the models used by the system:

```bash
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```

---

### 4. Dataset

Example dataset (cat facts):

```bash
mkdir -p data
curl -L -o data/cat-facts.txt https://huggingface.co/ngxson/demo_simple_rag_py/resolve/main/cat-facts.txt
```

---

### 5. Running the Chatbot

```bash
uv run rag-system
```

---

## Development

### Install development dependencies

```bash
uv sync --dev
```

---

### Pre-commit hooks

```bash
uv run pre-commit install
```

Pre-commit runs formatting, linting, and other checks automatically before commits.

---

### Linting & formatting (Ruff)

```bash
uv run ruff check .
uv run ruff format .
```

---

### Running tests

```bash
uv run pytest
```

---

### Continuous Integration

A CI workflow is included to ensure:

* Tests pass
* Ruff linting succeeds
* Code quality matches local pre-commit checks

---

## License
This project is licensed under the [MIT License](LICENSE).
