from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

def load_pdf(file_path : str):

    path = Path(file_path)

    if not path.exists():           ## this will check if the file is exist or not 
        raise FileNotFoundError(
            f"file not found : {file_path}"
        )

    if path.suffix.lower() != ".pdf":
        raise ValueError(
            f"Only pdf file is working"
        )

    loader = PyMuPDFLoader(str(path))

    doc = loader.load()

    return doc

# From Ubunt 
# COpy 
# cm pip inst rea 
