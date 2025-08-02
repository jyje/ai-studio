# 의존성 관리 가이드라인

## 개요
AI Studio는 사용자 역할에 따라 다른 의존성 프로필을 사용합니다. 이는 각 사용자가 필요한 기능에만 집중할 수 있도록 하고, 불필요한 패키지 설치를 방지합니다.

## 역할별 의존성 프로필

### 🎯 AI User (기본)
- **설치 명령어**: `uv sync`
- **포함 패키지**: 기본 런타임 의존성만
- **용도**: 단순한 AI 상호작용, 기본 채팅 인터페이스
- **특징**: 최소한의 의존성으로 빠른 설치

### 📊 AI Evaluator 
- **설치 명령어**: `uv sync --group eval`
- **포함 패키지**: User + 평가 및 시각화 도구
- **추가 의존성**:
  - `scipy`: 과학적 계산
  - `statsmodels`: 통계 분석
  - `plotly`: 인터랙티브 시각화
  - `dash-bootstrap-components`: UI 컴포넌트
- **용도**: AI 응답 품질 평가, 메트릭 시각화
- **특징**: 통계 분석과 시각화에 필요한 도구 포함

### 🔧 AI Developer
- **설치 명령어**: `uv sync --group dev`
- **포함 패키지**: Evaluator + 개발 및 디버깅 도구
- **추가 의존성**:
  - **데이터 분석**: `pandas`, `matplotlib`, `seaborn`, `scikit-learn`
  - **개발 환경**: `jupyter`, `ipython`
  - **프로파일링**: `memory-profiler`, `line-profiler`, `py-spy`
  - **코드 품질**: `black`, `ruff`, `mypy`
  - **테스팅**: `pytest`, `pytest-asyncio`, `pytest-cov`
  - **HTTP 클라이언트**: `httpx`
- **용도**: 전체 시스템 모니터링, 디버깅, 성능 분석
- **특징**: 완전한 개발 환경과 고급 분석 도구

## 의존성 계층 구조
```
[] (User) < [eval] (Evaluator) < [dev] (Developer)
```

각 상위 레벨은 하위 레벨의 모든 의존성을 포함합니다.

## 자동 의존성 체크

### 런타임 체크
- 사용자가 역할을 선택할 때 자동으로 의존성 체크 실행
- 누락된 패키지가 있으면 경고 메시지 표시
- 설치 명령어 자동 제공

### 경고 메시지 예시
```
⚠️  Missing Dependencies for AI Developer Mode

Some features may not work properly because the following packages are not installed:

  • Jupyter Notebook
  • Pandas (Data Analysis)
  • Matplotlib (Plotting)
  • ... and 5 more

To install the required dependencies, run:
    uv sync --group dev

This will install all packages needed for the AI Developer interface.
```

## 구현 세부사항

### 의존성 체크 모듈
- **위치**: `studio/utils/dependencies.py`
- **주요 함수**:
  - `check_role_dependencies()`: 역할별 의존성 체크
  - `create_dependency_warning_message()`: 경고 메시지 생성
  - `log_dependency_status()`: 로그에 의존성 상태 기록

### UI 통합
- 각 역할 인터페이스에서 자동으로 의존성 체크
- 누락된 의존성이 있으면 상단에 경고 배너 표시
- "Install Dependencies" 버튼으로 쉬운 설치 안내

### pyproject.toml 구성
```toml
[dependency-groups]
# AI User dependencies (minimal, basic functionality)
user = []

# AI Evaluator dependencies (metrics and visualization)
eval = [
    "scipy>=1.11.0",
    "statsmodels>=0.14.0",
    "plotly>=5.17.0",
    "dash-bootstrap-components>=1.5.0",
]

# AI Developer dependencies (full development and debugging suite)
dev = [
    # ... evaluator dependencies plus development tools
]
```

## 사용 가이드라인

### 새 의존성 추가 시
1. 해당 역할에 맞는 dependency group에 추가
2. `ROLE_DEPENDENCIES`와 `DEPENDENCY_NAMES` 딕셔너리 업데이트
3. 의존성 체크 로직이 새 패키지를 인식하는지 확인

### 테스팅
- 각 역할별로 깨끗한 환경에서 설치 테스트
- 의존성 체크 로직이 올바르게 작동하는지 확인
- UI 경고 메시지가 적절히 표시되는지 검증

### 성능 고려사항
- 의존성 체크는 역할 선택 시에만 실행
- 임포트 체크는 빠른 `importlib.import_module()` 사용
- 로그 레벨에 따라 상세 정보 조절

## 문제 해결

### 일반적인 문제
1. **패키지가 설치되었는데 체크에서 실패**: 모듈명과 패키지명 불일치 확인
2. **설치 명령어 실행 실패**: uv 버전 및 권한 확인
3. **경고 메시지가 표시되지 않음**: 로그 레벨 및 UI 렌더링 확인

### 디버깅
- `uv run ais health` 명령어로 전체 의존성 상태 확인
- 로그에서 의존성 체크 결과 확인
- 개발자 도구에서 UI 렌더링 오류 확인