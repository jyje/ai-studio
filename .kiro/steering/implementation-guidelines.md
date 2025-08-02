# 구현 가이드라인

## FastAPI 구현 패턴
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List

# 응답 모델 정의
class ResponseModel(BaseModel):
    success: bool
    data: Optional[dict] = None
    message: str = ""

# 의존성 주입 패턴
async def get_service() -> ServiceClass:
    return ServiceClass()

# 엔드포인트 구현
@app.post("/api/endpoint", response_model=ResponseModel)
async def endpoint(
    request: RequestModel,
    service: ServiceClass = Depends(get_service)
):
    try:
        result = await service.process(request)
        return ResponseModel(success=True, data=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Dash/Plotly 컴포넌트 패턴
```python
import dash
from dash import dcc, html, callback, Input, Output
import plotly.graph_objects as go

# 컴포넌트 팩토리 패턴
def create_visualization_component(data: dict) -> html.Div:
    return html.Div([
        dcc.Graph(
            figure=go.Figure(data=data),
            config={'displayModeBar': True}
        )
    ])

# 콜백 패턴
@callback(
    Output('output-component', 'children'),
    Input('input-component', 'value')
)
def update_component(input_value):
    # 처리 로직
    return create_visualization_component(processed_data)
```

## MCP 통합 패턴
```python
from typing import Protocol, Any, Dict

class MCPTool(Protocol):
    async def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        ...

class MCPManager:
    def __init__(self):
        self.tools: Dict[str, MCPTool] = {}
    
    async def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} not found")
        
        return await self.tools[tool_name].execute(params)
```

## RAG 시스템 패턴
```python
from abc import ABC, abstractmethod
from typing import List, Tuple

class VectorStore(ABC):
    @abstractmethod
    async def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        pass

class RAGSystem:
    def __init__(self, vector_stores: Dict[str, VectorStore]):
        self.vector_stores = vector_stores
    
    async def retrieve_and_compare(self, query: str) -> Dict[str, List[Tuple[str, float]]]:
        results = {}
        for name, store in self.vector_stores.items():
            results[name] = await store.search(query)
        return results
```

## 에러 처리 패턴
```python
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class AIStudioException(Exception):
    def __init__(self, message: str, details: Optional[dict] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

async def safe_execute(func, *args, **kwargs):
    try:
        return await func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Error in {func.__name__}: {str(e)}", exc_info=True)
        raise AIStudioException(f"Failed to execute {func.__name__}", {"error": str(e)})
```

## 설정 관리 패턴
```python
from pydantic import BaseSettings, Field
from typing import Optional

class Settings(BaseSettings):
    # API 설정
    api_host: str = Field(default="localhost", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    
    # OpenAI 설정
    openai_api_key: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    
    # 벡터 스토어 설정
    vector_store_path: str = Field(default="./data/vectors", env="VECTOR_STORE_PATH")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```