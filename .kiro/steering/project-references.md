---
inclusion: manual
---

# 프로젝트 참조 문서

## 스펙 문서 참조
- 요구사항: #[[file:.kiro/specs/ai-studio/requirements.md]]
- 설계 문서: #[[file:.kiro/specs/ai-studio/design.md]]
- 작업 목록: #[[file:.kiro/specs/ai-studio/tasks.md]]

## 설정 파일 참조
- 프로젝트 설정: #[[file:pyproject.toml]]
- 애플리케이션 설정: #[[file:studio/config.py]]
- 환경 변수 예시: #[[file:.env.example]]

## 핵심 모듈 참조
- CLI 메인: #[[file:studio/cli/main.py]]
- 서버 메인: #[[file:studio/server/main.py]]
- 메인 엔트리포인트: #[[file:main.py]]

## 외부 문서 링크
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Dash/Plotly 공식 문서](https://dash.plotly.com/)
- [Typer 공식 문서](https://typer.tiangolo.com/)
- [Pydantic 공식 문서](https://docs.pydantic.dev/)
- [uv 패키지 매니저](https://docs.astral.sh/uv/)

## API 스펙 (향후 추가 예정)
- OpenAPI 스펙: #[[file:docs/api-spec.yaml]]
- GraphQL 스키마: #[[file:docs/graphql-schema.graphql]]

## 데이터 모델 스키마
- 사용자 모델: #[[file:studio/models/user.py]]
- 쿼리 모델: #[[file:studio/models/query.py]]
- 응답 모델: #[[file:studio/models/response.py]]