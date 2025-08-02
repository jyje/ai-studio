# AI Studio 프로젝트 컨텍스트

## 프로젝트 개요
- **프로젝트명**: AI Studio
- **버전**: 0.1.0
- **설명**: Plotly 기반의 RAG와 MCP 통합 대화형 AI 스튜디오
- **Python 버전**: >=3.12
- **패키지 관리**: uv

## 핵심 기술 스택
- **웹 프레임워크**: FastAPI, Dash
- **CLI**: Typer
- **시각화**: Plotly
- **데이터 검증**: Pydantic
- **서버**: Uvicorn
- **보안**: Cryptography
- **테스팅**: pytest, pytest-asyncio

## 프로젝트 구조
```
ai-studio/
├── studio/                 # 메인 패키지
│   ├── api/                # API 엔드포인트
│   ├── cli/                # CLI 인터페이스 (Typer)
│   ├── frontend/           # 웹 인터페이스 (Dash/Plotly)
│   ├── mcp/                # Model Context Protocol 통합
│   ├── models/             # 데이터 모델 (Pydantic)
│   ├── rag/                # RAG 시스템
│   ├── server/             # 서버 구성
│   └── config.py           # 설정 관리
├── tests/                  # 테스트 코드
├── .kiro/specs/ai-studio/  # 프로젝트 스펙
└── pyproject.toml          # 프로젝트 설정
```

## 사용자 역할
1. **AI 개발자**: 상세한 모니터링, 디버깅, 성능 분석
2. **AI 평가자**: 간단하고 명확한 결과 평가 인터페이스
3. **AI 사용자**: 단순한 프롬프트 인터페이스

## CLI 사용법
- `uv run ais --help`: 도움말 표시
- `uv run ais run`: 웹 인터페이스 시작
- `studio --help`: 설치된 경우 직접 실행
- `studio run`: 설치된 경우 웹 인터페이스 시작

## 개발 및 테스트 명령어
- `uv run pytest`: 테스트 실행
- `uv run ais`: CLI 명령어 실행
- `uv add <package>`: 의존성 추가
- `uv remove <package>`: 의존성 제거
- **주의**: `python -m ...` 명령어 사용 금지, 항상 `uv run` 또는 `studio` 사용

## 핵심 기능
- RAG 시스템과 벡터 스토어 비교 (A, B, C)
- MCP 네트워크 홉 시각화
- 다중 언어/임베딩 모델 테스트
- OpenAI API 키 암호화 저장
- ReAct/LangGraph 구조 시각화