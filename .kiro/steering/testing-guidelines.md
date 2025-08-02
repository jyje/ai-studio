---
inclusion: fileMatch
fileMatchPattern: 'test*'
---

# 테스팅 가이드라인

## 테스트 구조
```
tests/
├── unit/                   # 단위 테스트
│   ├── test_api/
│   ├── test_rag/
│   ├── test_mcp/
│   └── test_models/
├── integration/            # 통합 테스트
│   ├── test_api_integration/
│   └── test_system_integration/
├── fixtures/               # 테스트 픽스처
└── conftest.py            # pytest 설정
```

## pytest 설정 예시
```python
# conftest.py
import pytest
import asyncio
from httpx import AsyncClient
from app.server.main import app

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
def sample_query():
    return "What is artificial intelligence?"

@pytest.fixture
def mock_vector_store():
    class MockVectorStore:
        async def search(self, query: str, top_k: int = 5):
            return [("Sample document", 0.95), ("Another document", 0.87)]
    return MockVectorStore()
```

## 단위 테스트 패턴
```python
import pytest
from unittest.mock import AsyncMock, patch
from app.rag.system import RAGSystem

class TestRAGSystem:
    @pytest.fixture
    def rag_system(self, mock_vector_store):
        return RAGSystem({"store_a": mock_vector_store})
    
    @pytest.mark.asyncio
    async def test_retrieve_and_compare(self, rag_system, sample_query):
        # Given
        expected_results = {"store_a": [("Sample document", 0.95)]}
        
        # When
        results = await rag_system.retrieve_and_compare(sample_query)
        
        # Then
        assert "store_a" in results
        assert len(results["store_a"]) > 0
        assert results["store_a"][0][1] > 0.8  # 점수 확인
    
    @pytest.mark.asyncio
    async def test_retrieve_with_empty_query(self, rag_system):
        # Given
        empty_query = ""
        
        # When & Then
        with pytest.raises(ValueError, match="Query cannot be empty"):
            await rag_system.retrieve_and_compare(empty_query)
```

## API 테스트 패턴
```python
import pytest
from httpx import AsyncClient

class TestAPIEndpoints:
    @pytest.mark.asyncio
    async def test_query_endpoint(self, client: AsyncClient):
        # Given
        payload = {
            "query": "What is machine learning?",
            "user_role": "developer"
        }
        
        # When
        response = await client.post("/api/query", json=payload)
        
        # Then
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "execution_trace" in data["data"]  # 개발자용 상세 정보
    
    @pytest.mark.asyncio
    async def test_query_endpoint_evaluator_role(self, client: AsyncClient):
        # Given
        payload = {
            "query": "What is machine learning?",
            "user_role": "evaluator"
        }
        
        # When
        response = await client.post("/api/query", json=payload)
        
        # Then
        assert response.status_code == 200
        data = response.json()
        assert "infographics" in data["data"]  # 평가자용 시각화
        assert "execution_trace" not in data["data"]  # 기술적 세부사항 제외
```

## MCP 테스트 패턴
```python
import pytest
from unittest.mock import AsyncMock
from app.mcp.manager import MCPManager

class TestMCPManager:
    @pytest.fixture
    def mcp_manager(self):
        manager = MCPManager()
        # Mock tool 등록
        mock_tool = AsyncMock()
        mock_tool.execute.return_value = {"result": "success"}
        manager.tools["test_tool"] = mock_tool
        return manager
    
    @pytest.mark.asyncio
    async def test_call_tool_success(self, mcp_manager):
        # Given
        tool_name = "test_tool"
        params = {"input": "test"}
        
        # When
        result = await mcp_manager.call_tool(tool_name, params)
        
        # Then
        assert result["result"] == "success"
        mcp_manager.tools[tool_name].execute.assert_called_once_with(params)
    
    @pytest.mark.asyncio
    async def test_call_nonexistent_tool(self, mcp_manager):
        # Given
        tool_name = "nonexistent_tool"
        params = {"input": "test"}
        
        # When & Then
        with pytest.raises(ValueError, match="Tool nonexistent_tool not found"):
            await mcp_manager.call_tool(tool_name, params)
```

## 성능 테스트 패턴
```python
import pytest
import time
from app.rag.system import RAGSystem

class TestPerformance:
    @pytest.mark.asyncio
    async def test_query_response_time(self, rag_system, sample_query):
        # Given
        max_response_time = 2.0  # 2초
        
        # When
        start_time = time.time()
        await rag_system.retrieve_and_compare(sample_query)
        end_time = time.time()
        
        # Then
        response_time = end_time - start_time
        assert response_time < max_response_time, f"Response time {response_time}s exceeds {max_response_time}s"
    
    @pytest.mark.asyncio
    async def test_concurrent_queries(self, rag_system):
        # Given
        queries = ["Query 1", "Query 2", "Query 3"]
        
        # When
        start_time = time.time()
        tasks = [rag_system.retrieve_and_compare(q) for q in queries]
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        
        # Then
        assert len(results) == len(queries)
        total_time = end_time - start_time
        assert total_time < 5.0  # 동시 처리로 5초 이내 완료
```

## 테스트 실행 명령어
```bash
# 모든 테스트 실행
uv run pytest

# 특정 디렉토리 테스트
uv run pytest tests/unit/

# 커버리지와 함께 실행
uv run pytest --cov=studio --cov-report=html

# 비동기 테스트만 실행
uv run pytest -m asyncio

# 성능 테스트 제외하고 실행
uv run pytest -m "not performance"

# 개발 서버 실행
uv run ais run

# CLI 도움말 확인
uv run ais --help

# 특정 모듈 실행 (절대 python -m 사용 금지)
uv run -m app.cli.main
```

## 중요한 명령어 사용 규칙
- **절대 사용 금지**: `python -m ...`, `python script.py`
- **항상 사용**: `uv run ...`, `studio ...`
- **패키지 관리**: `uv add`, `uv remove`, `uv sync`
- **가상환경**: uv가 자동으로 관리하므로 별도 활성화 불필요