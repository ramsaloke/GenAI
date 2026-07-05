from fastapi import APIRouter

from App.schemas.chat import ChatRequest, ChatResponse
from App.services.llm import get_chat_response

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):

    ai_response = get_chat_response(
        persona=request.persona,
        message=request.message
    )

    return ChatResponse(
        response=ai_response
    )