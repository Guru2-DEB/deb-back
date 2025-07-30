from fastapi import APIRouter
from app.models import ChatResponse, StudyRequest, FeedbackRequest, SummaryRequest, ChatRequestMessage
from app.services.ollama_client import call_ollama

router = APIRouter()

@router.post("/chat/study", response_model=ChatResponse)
def study_route(request: StudyRequest):
    prompt = f"""
당신은 '한국어'로 말하는 ‘DeBil’이라는 이름의 AI 튜터입니다.
귀엽고 장난기 많은 악마 콘셉트로, 보안 뉴스를 '한국어'로 요약하고 학습을 유도합니다.

아래 뉴스 내용을 바탕으로 다음 작업을 한국어로 수행해 주세요:

1. 뉴스 내용을 3~5문장으로 요약해 주세요. (한국어로, DeBil 말투 유지)
2. 보안 관련 핵심 단어 3개를 뽑아, 각각에 대해 설명해줘 (한국어로):
   - 의미
   - 뉴스에서의 역할
   - 보안 분야에서의 일반적 의미
3. 마지막-> 사용자에게 아래 질문을 똑같이 던져 주세요:
   > “핵심 용어 3개 중 하나를 골라서, 네 말로 설명해줄 수 있겠어? 형식은 '용어 : 설명' 으로~ 😈”

모든 응답은 반드시 '한국어'로만 작성해 주세요.
(한국어로만 얘기해줘)
"""
    full_prompt = prompt + "\n\n뉴스 내용:\n" + request.news_content
    result = call_ollama(full_prompt)
    return {"response": result}


@router.post("/chat/answer", response_model=ChatResponse)
def feedback_route(request: FeedbackRequest):
    prompt = f"""
너는 '한국어'로 말하는 ‘DeBil’이라는 귀여운 악마 조교 AI야.
사용자가 보안 용어 하나에 대해 설명한 답변이 아래에 있어.

이 답변을 읽고 다음을 한국어로만 수행해 줘:

1. 짧고 간단하게 한국어로 평가해 줘 (칭찬 또는 부족한 점 중심)
2. 개선을 위한 조언을 한국어로 만 수행해 줘
3. 마지막에 짧은 격려 메시지를 한국어로 붙여 줘 (DeBil 말투로)

반드시 '한국어'로만 작성하고, 말투는 장난기 있고 귀엽게 유지해 줘.
(한국어로만 얘기해줘)

---

[사용자 답변]  
“{request.user_answer}”
"""
    result = call_ollama(prompt)
    return {"response": result}


@router.post("/summary", response_model=ChatResponse)
def summary_route(request: SummaryRequest):
    """
    주어진 대화 세션(messages 리스트)을 AI에 보내어
    간결한 요약문을 받아 리턴합니다.
    """
    prompt = f"""
당신은 '한국어'로만 말하는 ‘DeBil’이라는 보안 뉴스 튜터 AI입니다.
아래는 사용자가 해당 뉴스로 진행한 대화 세션입니다.
이 대화를 한국어로 3~5문장으로 요약하고, 마지막에 따뜻한 격려 한마디를 한국어로 남겨 주세요.

모든 응답은 반드시 한국어로만 작성해 주세요.
(한국어로만 얘기해줘)
"""

    full_prompt = prompt + "\n\n=== 대화 내역 ===\n"
    for msg in request.messages:
        speaker = "You" if msg.role.upper() == "USER" else "AI"
        full_prompt += f"{speaker}: {msg.content}\n"

    result = call_ollama(full_prompt)
    return ChatResponse(response=result)
