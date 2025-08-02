# 명령어 사용 가이드라인

## 필수 명령어 규칙
이 프로젝트에서는 **반드시** uv 패키지 매니저와 studio CLI를 사용해야 합니다.

### ❌ 절대 사용 금지
```bash
python -m studio.cli.main
python -m pytest
python script.py
python -c "import ..."
pip install ...
```

### ✅ 올바른 사용법
```bash
# CLI 실행
uv run studio --help
uv run studio run

# 테스트 실행
uv run pytest
uv run pytest tests/unit/

# 스크립트 실행
uv run python script.py  # 필요한 경우에만

# 패키지 관리
uv add fastapi
uv remove fastapi
uv sync

# 개발 의존성 추가
uv add --dev pytest
```

## 프로젝트별 명령어

### 애플리케이션 실행
```bash
# 웹 인터페이스 시작
uv run studio run

# CLI 도움말
uv run studio --help

# 특정 명령어 실행
uv run studio <command>
```

### 개발 및 테스트
```bash
# 전체 테스트 실행
uv run pytest

# 특정 테스트 파일
uv run pytest tests/test_api.py

# 커버리지 포함 테스트
uv run pytest --cov=studio

# 린팅 (향후 추가 시)
uv run ruff check studio/
uv run black studio/
```

### 패키지 관리
```bash
# 의존성 설치
uv sync

# 새 패키지 추가
uv add requests

# 개발 의존성 추가
uv add --dev pytest-mock

# 패키지 제거
uv remove requests

# 의존성 업데이트
uv lock --upgrade
```

## 디버깅 및 개발
```bash
# 개발 서버 실행 (디버그 모드)
uv run studio run --debug

# 환경 변수와 함께 실행
UV_ENV_FILE=.env.local uv run studio run

# 특정 Python 버전 사용
uv run --python 3.12 studio run
```

## IDE 및 에디터 설정
- VS Code: Python 인터프리터를 `.venv/bin/python`으로 설정
- PyCharm: uv 가상환경을 프로젝트 인터프리터로 설정
- 터미널: 항상 `uv run` 접두사 사용

## 왜 uv를 사용해야 하는가?
1. **일관된 환경**: 모든 개발자가 동일한 의존성 버전 사용
2. **빠른 설치**: pip보다 훨씬 빠른 패키지 설치
3. **자동 가상환경**: 별도 venv 활성화 불필요
4. **락 파일**: uv.lock으로 정확한 의존성 재현
5. **프로젝트 표준**: pyproject.toml 기반 현대적 Python 프로젝트 관리