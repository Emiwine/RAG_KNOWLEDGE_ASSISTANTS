from app.ingestion.loader import load_pdf
from app.ingestion.splitter import split_documents



pdf_path = "data/raw/ebay_user_agreement.pdf"

doc = load_pdf(pdf_path)
chunks = split_documents(doc)

print("Number of documents:", len(doc))

print("Number of chunks:", len(chunks))


print("\n========== FIRST CHUNK ==========")

print(chunks[0].page_content)


print("\n========== FIRST CHUNK METADATA ==========")

print(chunks[0].metadata)


print("\n========== CHUNK LENGTH ==========")

print(len(chunks[0].page_content))