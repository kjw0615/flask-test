# 작은 하루

Flask로 만든 한국어 소개 페이지와 간단한 데일리 플래너입니다. 모바일 화면에도 대응합니다.

## 실행 (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python app.py
```

브라우저에서 http://127.0.0.1:5000 을 여세요.

할 일을 추가한 뒤 해당 항목을 클릭하면 완료 상태를 전환합니다. 최대 12개까지 추가할 수 있습니다. 데이터는 Flask의 서명된 브라우저 세션 쿠키에 저장되며, 데이터베이스는 사용하지 않습니다. 민감한 정보는 입력하지 마세요. 기본 임시 비밀 키를 사용하면 서버 재시작 시 세션이 초기화됩니다. 세션을 유지하려면 실행 전에 `SECRET_KEY` 환경 변수에 충분히 긴 임의의 값을 설정하세요.

개발 중 자동 재시작이 필요하면 `$env:FLASK_DEBUG = "1"`을 설정하세요. 이 실행 방법은 로컬 개발용입니다.
