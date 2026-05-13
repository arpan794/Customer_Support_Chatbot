from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.chatbot import handle_chat
from app.db.db_dependency import get_db
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat")
def chat(req: ChatRequest, db: Session = Depends(get_db)) -> ChatResponse:
    
    return handle_chat(
        user_id=req.user_id,
        message=req.message,
        db=db
    )