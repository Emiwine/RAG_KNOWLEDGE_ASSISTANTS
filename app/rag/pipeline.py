from app.retireval.retriever import get_retriever
from app.generation.llm import get_llm
from app.generation.prompts import RAG_PROMPTS

def ask_question(question:str):
    reteriver = get_retriever()
    llm = get_llm()

    documents = reteriver.invoke(question)

    context = "\n\n".join(
        document.page_content
        for document in documents
        )
    prompt = RAG_PROMPTS.format(            # this is filling a predefined prompt templates in promt file 
        context = context,
        question = question,
    )

    response = llm.invoke(prompt)  ## send it to groq
    return{
        "answer" : response.content,
        "sources" : documents,
    }




"""
flow of the model

user = what is abritration -> rag pipeline - retriever - embedding - chroma db - top 5 chunks in doc - build context - build prompt 

                         pipeline.py
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
   Retriever               Prompt                  LLM
        │                     │                     │
        ▼                     │                     ▼
    ChromaDB                  │                   Groq
        │                     │                     │
        ▼                     │                     │
   5 chunks ───────────────→ Context ────────────→ Answer

"""