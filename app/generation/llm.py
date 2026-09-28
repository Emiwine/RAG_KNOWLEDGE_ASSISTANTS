from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    return ChatGroq(
        model = settings.rag_llm_model,
        temperature = 0,
        api_key=settings.groq_api_key,
    )
