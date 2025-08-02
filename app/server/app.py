"""
FastAPI Application with FastUI Integration

This module creates and configures the FastAPI application that serves
the FastUI interface with embedded Plotly components.

Note: This is NOT a main.py file - studio/main.py is the only main entry point.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastui import FastUI, AnyComponent, prebuilt_html
from fastui.components import Page, Heading, Paragraph, Div
from typing import List

# Import FastUI page modules
from app.frontend.app import create_fastui_app
from app.frontend.pages.developer import create_developer_page
from app.frontend.pages.evaluator import create_evaluator_page
from app.frontend.pages.user import create_user_page


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application with FastUI integration.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title="AI Studio",
        description="FastUI와 Plotly를 통합한 RAG와 MCP 대화형 AI 스튜디오",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )
    
    # Add CORS middleware for development
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Mount static files for FastUI
    try:
        from fastui import static_files
        app.mount("/static", StaticFiles(directory=static_files), name="static")
    except ImportError:
        # If static files are not available, continue without them
        pass
    
    # Health check endpoint
    @app.get("/api/health")
    async def health_check():
        """Health check endpoint for monitoring"""
        return {
            "status": "healthy",
            "service": "AI Studio",
            "version": "0.1.0"
        }
    
    # FastUI API routes (for component data)
    @app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
    async def homepage_api() -> List[AnyComponent]:
        """
        FastUI homepage API with role selection interface
        """
        return create_fastui_app()
    
    # Role-specific API routes
    @app.get("/api/developer", response_model=FastUI, response_model_exclude_none=True)
    async def developer_api() -> List[AnyComponent]:
        """FastUI developer interface API"""
        return create_developer_page()
    
    @app.get("/api/evaluator", response_model=FastUI, response_model_exclude_none=True)
    async def evaluator_api() -> List[AnyComponent]:
        """FastUI evaluator interface API"""
        return create_evaluator_page()
    
    @app.get("/api/user", response_model=FastUI, response_model_exclude_none=True)
    async def user_api() -> List[AnyComponent]:
        """FastUI user interface API"""
        return create_user_page()
    
    # Catch-all route for FastUI HTML page (must be last)
    @app.get("/{path:path}")
    async def html_landing() -> HTMLResponse:
        """Serve the FastUI HTML page for all paths"""
        return HTMLResponse(prebuilt_html(title="AI Studio", api_root_url="/api"))
    
    return app