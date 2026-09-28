from langchain_groq import ChatGroq
from app.core.config import settings

llm = ChatGroq(
    model = settings.rag_llm_model,
    temperature=0,
    groq_api_key=settings.groq_api_key
)

result = llm.invoke("explain me about rag in 2 lines ")

print(result.content)

## this is on checcking that this api key is working or not 