# Backend & Android 실행 가이드

이 프로젝트는 백엔드 서버와 Android 앱이 함께 작동합니다.  
**AI 채팅 기능을 사용하려면 반드시 백엔드를 먼저 실행한 후, Android 앱을 실행해야 합니다.**

---

## ✅ 1. 백엔드 실행 준비

### Python 패키지 설치
```bash
pip install -r requirements.txt
```

## ✅ 2. 백엔드 실행 준비

### OS에 관계없이 동일합니다.
### FastAPI 서버가 http://localhost:8000 에서 실행됩니다.
### 이 상태를 유지한 채 Android 앱을 실행해야 AI 기능이 정상 동작합니다.
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
