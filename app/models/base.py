"""
Base models for AI Studio.

This module contains base Pydantic models and common data structures
used throughout the application.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class BaseEntity(BaseModel):
    """Base entity model with common fields."""
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Configuration(BaseModel):
    """Application configuration model."""
    api_host: str = Field(default="localhost", description="API server host")
    api_port: int = Field(default=8000, description="API server port")
    debug: bool = Field(default=False, description="Debug mode")
    
    # OpenAI Configuration
    openai_api_key: Optional[str] = Field(default=None, description="OpenAI API key")
    default_model: str = Field(default="gpt-3.5-turbo", description="Default AI model")
    
    # Vector Store Configuration
    vector_store_path: str = Field(
        default="./data/vectors", 
        description="Path to vector store data"
    )
    
    # MCP Configuration
    mcp_servers: Dict[str, Any] = Field(
        default_factory=dict, 
        description="MCP server configurations"
    )


class MonitoringData(BaseModel):
    """Monitoring data structure for developer interface."""
    active_queries: int = 0
    total_queries: int = 0
    average_response_time: float = 0.0
    error_rate: float = 0.0
    vector_store_status: Dict[str, str] = Field(default_factory=dict)
    mcp_server_status: Dict[str, str] = Field(default_factory=dict)