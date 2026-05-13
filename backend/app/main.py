from fastapi import FastAPI
from app.api.chat import router as chat_router


app = FastAPI(
    title="AI Customer Support Chatbot"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Customer Support Chatbot"}
