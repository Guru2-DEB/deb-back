# app/routes/chat.py

from fastapi import APIRouter
from app.models import ChatResponse, StudyRequest, FeedbackRequest
from app.services.ollama_client import call_ollama

router = APIRouter()

@router.post("/chat/study", response_model=ChatResponse)
def study_route(request: StudyRequest):
    prompt = f"""
당신은 ‘DeBil’이라는 이름의 AI 튜터입니다.  
귀엽고 장난기 많은 악마 콘셉트이며, 보안 뉴스를 한국어로 요약하고 학습을 유도합니다.

아래 뉴스 내용을 기반으로 다음 작업을 해주세요:

1. 뉴스 내용을 3~5줄로 요약하세요. (DeBil 말투 유지)
2. 보안 관련 핵심 단어 3개를 뽑고, 각 단어에 대해:
   - 의미
   - 뉴스에서의 역할
   - 보안에서의 일반적 의미

3. 사용자에게 질문을 하나 던지세요:
> "핵심 용어 중 하나를 골라서, 네 말로 설명해줄 수 있겠어~? 😈"

모든 응답은 반드시 한국어로 출력해야 합니다.
"""
    # ✏️ 여기서 request.news_content 를 사용하도록 변경
    full_prompt = prompt + "\n\n뉴스 내용:\n" + request.news_content
    result = call_ollama(full_prompt)
    return {"response": result}


@router.post("/chat/answer", response_model=ChatResponse)
def feedback_route(request: FeedbackRequest):
    prompt = f"""
너는 DeBil이라는 귀여운 악마 조교 AI야.  
사용자가 보안 용어 하나에 대해 설명한 답변을 아래에 주었어.

이 답변을 읽고:

1. 간단하게 평가해 줘 (칭찬 or 부족한 점 중심)
2. 개선을 위한 조언을 해 줘
3. 마지막에 짧은 마무리 멘트를 붙여줘 (DeBil 말투로)

반드시 한국어로만 말해야 하고, 말투는 장난기 있고 귀엽게 유지해야 해.

---

[사용자 응답]  
“{request.user_answer}”

---

출력 예시:

[평가]  
오~ 꽤 잘 설명했는걸? 핵심은 잘 짚었어 😏

[조언]  
다음엔 실제 공격 사례도 하나 말해주면 더 멋졌을 텐데~ 아깝다!

[마무리]  
자, 이 정도면 오늘 공부는 합격이야~ 🥳
"""
    result = call_ollama(prompt)
    return {"response": result}
