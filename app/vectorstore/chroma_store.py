from langchain_chroma import Chroma
from app.core.config import settings
from app.embeddings.embedding_model import get_embedding_model

def get_vector_store():
    vector_store = Chroma(
        collection_name=settings.chroma_collection,
        embedding_function=get_embedding_model(),  ## telling to chroma that whenevver need to convert text into vector using this model
        persist_directory=settings.chroma_persist_dir,
    )

    return vector_store