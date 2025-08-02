# AI Studio - Cursor Rules

## 프로젝트 개요
AI Studio는 FastUI와 Plotly를 통합한 RAG(Retrieval-Augmented Generation)와 MCP(Model Context Protocol) 대화형 AI 스튜디오입니다.

- **버전**: 0.1.0
- **Python**: >=3.13
- **패키지 관리**: uv (pip/conda 사용 금지)
- **진입점**: `studio/main.py` (유일한 main.py)

## 핵심 기술 스택
- **웹 프레임워크**: FastAPI + FastUI (모든 UI 관리)
- **CLI**: Typer
- **시각화**: Plotly (FastUI 내 임베드)
- **데이터 검증**: Pydantic
- **서버**: Uvicorn
- **테스팅**: pytest, pytest-asyncio

## 절대 금지 명령어
```bash
# 절대 사용 금지
python -m ...
python script.py
pip install ...
```

## 필수 사용 명령어
```bash
# 항상 사용해야 함
uv run ais --help           # 도움말
uv run ais run              # 웹 인터페이스 시작
uv run pytest              # 테스트 실행
uv add <package>            # 의존성 추가
uv remove <package>         # 의존성 제거
```

## 아키텍처 원칙
1. **모듈화**: 각 기능을 독립적인 모듈로 분리
2. **의존성 주입**: 설정과 의존성을 명시적으로 주입
3. **비동기 처리**: I/O 바운드 작업에 async/await 사용
4. **FastUI 우선**: 모든 UI는 FastUI 컴포넌트로 구현
5. **Plotly 임베드**: 시각화는 FastUI 내 Plotly 임베드

## 사용자 역할별 인터페이스
1. **AI 개발자**: 상세한 모니터링, 디버깅, 성능 분석
2. **AI 평가자**: 간단하고 명확한 결과 평가 인터페이스
3. **AI 사용자**: 단순한 프롬프트 인터페이스

## 코딩 표준
- **스타일**: PEP 8 준수
- **타입 힌팅**: 모든 함수와 클래스에 필수
- **Docstring**: Google 스타일
- **에러 처리**: 명확한 예외 처리와 로깅
- **테스트 커버리지**: 최소 80% 이상

## 보안 규칙
- **API 키**: cryptography로 암호화 저장
- **입력 검증**: Pydantic 모델로 모든 입력 검증
- **환경 변수**: 민감한 정보는 .env 파일로 관리

## 프로젝트 구조
```
ai-studio/
├── app/                   # 메인 패키지
│   ├── api/              # FastAPI 엔드포인트
│   ├── cli/              # Typer CLI
│   ├── frontend/         # FastUI + Plotly 인터페이스
│   ├── mcp/              # MCP 통합
│   ├── models/           # Pydantic 모델
│   ├── rag/              # RAG 시스템
│   ├── server/           # 서버 구성
│   └── main.py           # 유일한 진입점
├── tests/                # 테스트 코드
└── pyproject.toml        # 프로젝트 설정
```

## 핵심 기능
- RAG 시스템과 벡터 스토어 비교 (A, B, C)
- MCP 네트워크 홉 시각화
- 다중 언어/임베딩 모델 테스트
- OpenAI API 키 암호화 저장
- ReAct/LangGraph 구조 시각화

## FastAPI + FastUI 패턴
```python
# 표준 응답 모델
class ResponseModel(BaseModel):
    success: bool
    data: Optional[dict] = None
    message: str = ""

# 비동기 엔드포인트
@app.post("/api/endpoint", response_model=ResponseModel)
async def endpoint(request: RequestModel):
    try:
        result = await service.process(request)
        return ResponseModel(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## 테스트 패턴
```python
# 비동기 테스트
@pytest.mark.asyncio
async def test_endpoint(client: AsyncClient):
    response = await client.post("/api/test", json=payload)
    assert response.status_code == 200
```

이 규칙들을 따라 AI Studio를 개발해주세요. 