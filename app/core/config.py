from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    groq_api_key : str
    rag_llm_model : str = "openai/gpt-oss-120b"
    embedding_model : str = "BAAI/bge-small-en-v1.5"
    chroma_persist_dir: str = "./chroma_db"
    chroma_collection : str = "documents"
    top_k : int = 5 
    chunk_size : int = 800
    chunk_overlap : int = 120 

    model_config = SettingsConfigDict(
    env_file=PROJECT_ROOT / ".env",     # Load the repository's .env
    env_file_encoding="utf-8",          # Read .env as UTF-8
    extra="ignore",                     # Ignore unknown .env variables
    )

settings = Settings()
