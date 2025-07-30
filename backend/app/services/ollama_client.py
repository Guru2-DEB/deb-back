import requests

# def call_ollama(messages: list) -> str:
#     """
#     Ollama API에 메시지를 전달하고 응답 텍스트를 반환합니다.
#     """
#     try:
#         response = requests.post("http://localhost:11434/api/chat", json={
#             "model": "llama3",
#             "messages": messages,
#             "stream": False  # 스트리밍을 비활성화합니다.
#         })

#         response.raise_for_status()  # 실패 시 예외 발생
#         json_data = response.json()
#         return json_data.get("message", {}).get("content", "[응답 없음]")

#     except Exception as e:
#         print("[Ollama 호출 오류]:", e)
#         return f"[Ollama 오류] {str(e)}"

def call_ollama(prompt: str):
    url = "http://localhost:11434/api/chat"  # ← 변경됨
    payload = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()["message"]["content"]

