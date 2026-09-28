from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = settings.chunk_size,
        chunk_overlap = settings.chunk_overlap
    )

    chunks = splitter.split_documents(documents)
    for index , chunk in enumerate(chunks):
        chunk.metadata["chunk_index"] = index 

    return chunks


# Try different splitting approaches 
# Agentic Splitting 
# tree Structure 
# index structure (PageIndex)
