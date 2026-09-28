from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """
    Request body for the RAG question endpoint.
    """

    question: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Question to ask the knowledge assistant",
        examples=["What is eBay's arbitration policy?"],
    )


class SourceResponse(BaseModel):
    """
    Source information returned with the answer.
    """

    page: int | None = None
    source: str | None = None


class AskResponse(BaseModel):
    """
    Response returned by the RAG question endpoint.
    """

    answer: str
    sources: list[SourceResponse]