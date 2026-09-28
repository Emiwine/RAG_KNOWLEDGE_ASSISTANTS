from app.rag.pipeline import ask_question

question = "What is eBay's arbitration policy?"

result = ask_question(question)

print("==============================")
print("QUESTION")
print("==============================")
print(question)

print("==============================")
print("ANSWER")
print("==============================")
print(result["answer"])

print("==============================")
print("SOURCES")
print("==============================")

for i, document in enumerate(result["sources"], start=1):
    print(f"\nSource {i}")
    print("Content:", document.page_content)
    print("Metadata:", document.metadata)