from app.rag.pipeline import ask_question
from tests.evaluation_questions import TEST_QUESTIONS


for i, question in enumerate(TEST_QUESTIONS, start=1):

    print("\n" + "=" * 80)
    print(f"TEST {i}")
    print("=" * 80)

    print("QUESTION:")
    print(question)

    result = ask_question(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")

    for source in result["sources"]:
        print(
            f"Page: {source.metadata.get('page')} | "
            f"Chunk: {source.metadata.get('chunk_index')}"
        )