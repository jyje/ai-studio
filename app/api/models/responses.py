"""
API response models for AI Studio.

This module contains Pydantic models for API responses and data structures
used throughout the application.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from enum import Enum


class UserRole(str, Enum):
    """User role enumeration."""
    DEVELOPER = "developer"
    EVALUATOR = "evaluator"
    USER = "user"


class Document(BaseModel):
    """Document model for RAG results."""
    content: str
    metadata: Dict[str, Any] = {}
    score: float = 0.0


class VectorStoreResult(BaseModel):
    """Vector store search result."""
    store_name: str
    documents: List[Document]
    scores: List[float]
    retrieval_time: float
    quality_score: float


class RAGResponse(BaseModel):
    """RAG query response model."""
    query: str
    answer: str
    sources: List[Document]
    retrieval_metrics: Dict[str, float]
    execution_time: float
    vector_store_results: Dict[str, VectorStoreResult]


class ExecutionStep(BaseModel):
    """Execution step for tracing."""
    step_id: str
    step_type: str
    description: str
    timestamp: float
    duration: float
    success: bool
    details: Dict[str, Any] = {}


class MCPCall(BaseModel):
    """MCP tool call information."""
    tool_name: str
    parameters: Dict[str, Any]
    result: Dict[str, Any]
    execution_time: float
    success: bool


class ExecutionTrace(BaseModel):
    """Complete execution trace."""
    steps: List[ExecutionStep]
    mcp_calls: List[MCPCall]
    total_time: float
    success: bool


class ModelResult(BaseModel):
    """Individual model test result."""
    model_name: str
    response: str
    response_time: float
    quality_score: Optional[float] = None
    cost: Optional[float] = None
    success: bool
    error_message: Optional[str] = None


class ModelComparison(BaseModel):
    """Model comparison results."""
    query: str
    results: Dict[str, ModelResult]
    best_model: Optional[str] = None
    summary_metrics: Dict[str, float] = {}


class EvaluationResult(BaseModel):
    """AI response evaluation result."""
    query: str
    response: str
    overall_score: float
    criteria_scores: Dict[str, float]
    summary: str
    recommendations: List[str] = []


class APIResponse(BaseModel):
    """Generic API response wrapper."""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: str = ""
    error_code: Optional[str] = None