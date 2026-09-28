from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_documents
from app.vectorstore.chroma_store import get_vector_store


PDF_PATH = "data/raw/ebay_user_agreement.pdf"


documents = load_pdf(PDF_PATH)

chunks = split_documents(documents)

print("Documents:", len(documents))
print("Chunks:", len(chunks))


vector_store = get_vector_store()

vector_store.add_documents(chunks)

print("Successfully added chunks to ChromaDB.")