# app/models.py
from pydantic import BaseModel

class StudyRequest(BaseModel):
    news_content: str

class FeedbackRequest(BaseModel):
    user_answer: str
    core_term: str

class ChatResponse(BaseModel):
    response: str
