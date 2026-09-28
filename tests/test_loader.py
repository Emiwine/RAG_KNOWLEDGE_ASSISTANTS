from app.ingestion.loader import load_pdf

path_pdf = "data/raw/ebay_user_agreement.pdf"

documents = load_pdf(path_pdf)

print("Number of documents:", len(documents))


print("\n========== FIRST DOCUMENT ==========")

print(documents[0])


print("\n========== CONTENT ==========")

print(documents[0].page_content)


print("\n========== METADATA ==========")

print(documents[0].metadata)
