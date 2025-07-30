# app/models.py

from pydantic import BaseModel
from typing import List

class StudyRequest(BaseModel):
    news_content: str

class FeedbackRequest(BaseModel):
    user_answer: str
    core_term: str

class ChatResponse(BaseModel):
    response: str


# —————— 요약(Summary)용 DTO 추가 ——————

class ChatRequestMessage(BaseModel):
    """
    대화 메시지 전달용 DTO:
      role: "USER" 또는 "AI"
      content: 실제 텍스트
    """
    role: str
    content: str

class SummaryRequest(BaseModel):
    """
    대화 세션 요약 요청용 DTO:
      session_id: DB에 저장된 대화 세션 고유 ID
      messages:   ChatRequestMessage 리스트
    """
    session_id: int
    messages: List[ChatRequestMessage]
