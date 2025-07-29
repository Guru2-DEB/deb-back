# app/main.py
from fastapi import FastAPI
from app.routes.chat import router as chat_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DeBil backend is running!"}

app.include_router(chat_router)
app.include_router(chat_router, prefix="/v1/study")
