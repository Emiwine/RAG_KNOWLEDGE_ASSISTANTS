from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Production RAG Knowledge Assistant",
    description="A RAG API for answering questions from documents.",
    version="1.0.0",
)

app.include_router(router)


@app.get("/", tags=["Health"])
def root():
    return {
        "name": "Production RAG Knowledge Assistant",
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}