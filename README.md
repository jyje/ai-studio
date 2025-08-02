# AI Studio

FastUI와 Plotly를 통합한 RAG와 MCP 대화형 AI 스튜디오

## 개요

AI Studio는 AI 개발자, 평가자, 사용자를 위한 차별화된 인터페이스를 제공하는 현대적인 웹 애플리케이션입니다. FastUI와 Plotly를 통합하여 인터랙티브한 시각화와 함께 RAG(Retrieval-Augmented Generation)와 MCP(Model Context Protocol) 기능을 제공합니다.

## 주요 기능

- 🎯 **역할별 인터페이스**: AI 개발자, 평가자, 사용자를 위한 맞춤형 UI
- 📊 **인터랙티브 시각화**: Plotly를 통한 실시간 데이터 시각화
- 🔍 **RAG 시스템**: 다중 벡터 스토어 비교 및 검색 증강 생성
- 🔗 **MCP 통합**: Model Context Protocol을 통한 도구 실행 및 추적
- ⚡ **FastUI**: 현대적이고 반응형인 웹 인터페이스
- 🛡️ **보안**: API 키 암호화 및 안전한 설정 관리

## 설치 및 실행

### 요구사항

- Python 3.12 이상
- uv 패키지 매니저

### 설치

```bash
# 기본 설치 (AI User)
uv sync

# AI Evaluator용 설치
uv sync --group eval

# AI Developer용 설치 (전체 기능)
uv sync --group dev
```

### 실행

```bash
# 웹 인터페이스 시작
uv run ais run

# CLI 도움말
uv run ais --help

# 시스템 상태 확인
uv run ais health

# 설정 관리
uv run ais config --show
```

## 개발 상태

🚧 **현재 개발 중**

- [x] Task 1: 프로젝트 구조 및 FastUI 의존성 설정
- [ ] Task 2: CLI 인터페이스 구현
- [ ] Task 3: FastAPI 서버 및 FastUI 기반 구현
- [ ] Task 4: 기본 API 엔드포인트 및 FastUI 페이지
- [ ] Task 5: 역할별 UI 레이아웃
- [ ] 기타 작업들...

## 아키텍처

```
studio/
├── main.py              # 유일한 메인 진입점
├── cli/                 # CLI 인터페이스 (Typer)
├── server/              # FastAPI 서버
├── frontend/            # FastUI 컴포넌트
├── api/                 # API 엔드포인트
├── rag/                 # RAG 시스템
└── mcp/                 # MCP 통합
```

## 기술 스택

- **웹 프레임워크**: FastAPI
- **UI 프레임워크**: FastUI
- **CLI**: Typer
- **시각화**: Plotly
- **데이터 검증**: Pydantic
- **서버**: Uvicorn
- **보안**: Cryptography
- **패키지 관리**: uv

## 라이선스

MIT License