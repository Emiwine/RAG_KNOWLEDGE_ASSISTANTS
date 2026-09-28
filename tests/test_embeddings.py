from app.embeddings.embedding_model import get_embedding_model
from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_documents


PDF_PATH = "data/raw/ebay_user_agreement.pdf"


documents = load_pdf(PDF_PATH)

chunks = split_documents(documents)

embedding_model = get_embedding_model()


text = chunks[0].page_content

vector = embedding_model.embed_query(text)


print("Chunk:")
print(text)

print("\nChunk length:")
print(len(text))

print("\nVector length:")
print(len(vector))

print("\nFirst 10 vector values:")
print(vector[:10])