from fastapi import APIRouter, HTTPException

from app.api.schemas import (
    AskRequest,
    AskResponse,
    SourceResponse,
)
from app.rag.pipeline import ask_question


router = APIRouter(
    prefix="/api/v1",
    tags=["RAG"],
)


@router.post(
    "/ask",
    response_model=AskResponse,
    summary="Ask a question",
    description="Ask a question to the RAG knowledge assistant.",
)
def ask(request: AskRequest) -> AskResponse:

    try:
        # Call the existing RAG pipeline
        result = ask_question(request.question)

        # Convert retrieved documents into API-friendly objects
        sources = [
            SourceResponse(
                page=document.metadata.get("page"),
                source=document.metadata.get("source"),
            )
            for document in result["sources"]
        ]

        # Return validated response
        return AskResponse(
            answer=result["answer"],
            sources=sources,
        )

    except Exception as exc:
        # Do not expose internal exception details to the client
        raise HTTPException(
            status_code=500,
            detail="Failed to process the question.",
        ) from exc