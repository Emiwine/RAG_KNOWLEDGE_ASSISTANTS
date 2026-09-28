from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_documents
from app.ingestion.ids import generate_chunk_id
from app.vectorstore.chroma_store import get_vector_store


def ingest_pdf(file_path: str):
    documents = load_pdf(file_path)

    chunks = split_documents(documents)

    vector_store = get_vector_store()

    ids = [
        generate_chunk_id(chunk, index)
        for index, chunk in enumerate(chunks)
    ]

    vector_store.add_documents(
        documents=chunks,
        ids=ids,
    )

    return len(chunks)