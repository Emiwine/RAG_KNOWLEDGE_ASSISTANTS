from app.vectorstore.chroma_store import get_vector_store
from app.core.config import settings

def get_retriever():
    vector_store = get_vector_store()
    reteriver = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs ={
            "k" : settings.top_k
        },
    )
    return reteriver

# keyword matching 
# REranking 

# uploader 
# metadata ( file name, fiketype source=  ebay, flipkart , amazon )
# Hi 
# Do you want to know your ebay purchases 
# (intent capture)
# Yes (RAG)
# Response +intent+ Input 
# Can you clarify + intent +Response 
