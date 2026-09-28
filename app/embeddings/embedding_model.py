from langchain_huggingface import HuggingFaceEmbeddings  ## Hugging face embedding use this to tell the langchiain to convert text into vector

from app.core.config import settings

def get_embedding_model():
    embeddings = HuggingFaceEmbeddings(
        model_name = settings.embedding_model,
        model_kwargs = {
            "device" : "cpu"            ## this tells the model to run on cpu , later we can change it into gpu
        },
        encode_kwargs = { "normalize_embeddings" : True},
    )

    return embeddings
