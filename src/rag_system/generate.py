from __future__ import annotations

import ollama

from rag_system.config import LANGUAGE_MODEL


def generate(input_query: str, context: list[tuple[str, float]]) -> None:
    context_lines = "\n".join(f" - {chunk}" for chunk, _ in context)

    instruction_prompt = (
        "Use only the following pieces of context to answer the question. "
        "Don't make up any new information:\n"
        f"{context_lines}"
    )

    stream = ollama.chat(
        model=LANGUAGE_MODEL,
        messages=[
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": input_query},
        ],
        stream=True,
    )

    print("Chatbot response:")
    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)
    print("\n" + "-" * 60)
