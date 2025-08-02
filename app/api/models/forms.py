"""
FastUI form models for AI Studio.

This module contains Pydantic models for FastUI forms used throughout
the application for user input validation and processing.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class RAGQueryForm(BaseModel):
    """Form model for RAG query input."""
    query: str = Field(..., min_length=1, description="The query to process")
    vector_stores: Optional[List[str]] = Field(
        default=None, 
        description="List of vector stores to search"
    )
    max_results: int = Field(default=5, ge=1, le=20, description="Maximum results to return")


class ModelTestForm(BaseModel):
    """Form model for model testing input."""
    query: str = Field(..., min_length=1, description="Query to test across models")
    models: List[str] = Field(..., min_items=1, description="List of models to test")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Model temperature")
    max_tokens: int = Field(default=1000, ge=1, le=4000, description="Maximum tokens")


class ConfigurationForm(BaseModel):
    """Form model for system configuration."""
    api_key: str = Field(..., min_length=1, description="API key for external services")
    model_name: str = Field(..., min_length=1, description="Default model name")
    vector_store_path: Optional[str] = Field(
        default=None, 
        description="Path to vector store data"
    )


class EvaluationForm(BaseModel):
    """Form model for AI response evaluation."""
    query: str = Field(..., min_length=1, description="Query to evaluate")
    expected_answer: Optional[str] = Field(
        default=None, 
        description="Expected answer for comparison"
    )
    evaluation_criteria: List[str] = Field(
        default_factory=list, 
        description="Criteria for evaluation"
    )


class ChatForm(BaseModel):
    """Form model for simple chat interface."""
    message: str = Field(..., min_length=1, description="Chat message")
    session_id: Optional[str] = Field(default=None, description="Chat session ID")