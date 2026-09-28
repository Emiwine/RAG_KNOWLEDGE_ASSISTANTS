"""hashing algorithm is a mathematical function that converts some input 
data and converts it into fixed size string characters 

"""

import hashlib


def generate_chunk_id(document , chunk_index:int) -> str:
    source = document.metadata.get("source" , "unknown")
    page = document.metadata.get("page" , 0)

    raw_id = f"{source}:{page}:{chunk_index}"
    return hashlib.sha256(raw_id.encode("utf-8")).hexdigest()