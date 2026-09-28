"""Quick configuration smoke test.

Run from the repository root with ``python -m app.core.test_config``.
It can also be run directly from this directory.
"""

import sys
from pathlib import Path


# A directly executed file uses its own directory as Python's import base.
# Add the repository root so the top-level ``app`` package is discoverable.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.core.config import settings

print("Groq API Key Loaded:", bool(settings.groq_api_key))
print("LLM Model:", settings.rag_llm_model)
print("Embedding Model:", settings.embedding_model)
print("Chroma Directory:", settings.chroma_persist_dir)
print("Top K:", settings.top_k)
print("Chunk Size:", settings.chunk_size)
print("Chunk Overlap:", settings.chunk_overlap)

