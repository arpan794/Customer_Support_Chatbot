from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.auth import router as auth_router

from app.db.base import Base
from app.db.session import engine

import app.models

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI Customer Support Chatbot"
)

app.include_router(chat_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Customer Support Chatbot"}
