"""
Test FastUI structure and basic functionality.
"""

import pytest
from fastapi.testclient import TestClient
from app.server.app import create_app
from app.frontend.app import create_fastui_app
from app.frontend.pages.developer import create_developer_page
from app.frontend.pages.evaluator import create_evaluator_page
from app.frontend.pages.user import create_user_page


def test_create_app():
    """Test that the FastAPI app can be created successfully."""
    app = create_app()
    assert app is not None
    assert app.title == "AI Studio"


def test_fastui_app_creation():
    """Test that the main FastUI app components can be created."""
    components = create_fastui_app()
    assert len(components) > 0
    assert components[0].type == "Page"


def test_developer_page_creation():
    """Test that the developer page components can be created."""
    components = create_developer_page()
    assert len(components) > 0
    assert components[0].type == "Page"


def test_evaluator_page_creation():
    """Test that the evaluator page components can be created."""
    components = create_evaluator_page()
    assert len(components) > 0
    assert components[0].type == "Page"


def test_user_page_creation():
    """Test that the user page components can be created."""
    components = create_user_page()
    assert len(components) > 0
    assert components[0].type == "Page"


def test_api_endpoints():
    """Test that the API endpoints are accessible."""
    app = create_app()
    client = TestClient(app)
    
    # Test health endpoint
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    
    # Test homepage
    response = client.get("/")
    assert response.status_code == 200
    
    # Test role-specific pages
    for role in ["developer", "evaluator", "user"]:
        response = client.get(f"/{role}")
        assert response.status_code == 200