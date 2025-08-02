"""
CLI Commands Implementation

This module contains the implementation of all CLI commands for AI Studio.
"""

import typer
from typing import Optional
import uvicorn


def run_server(host: str, port: int, debug: bool, reload: bool) -> None:
    """Run the FastAPI server with FastUI interface"""
    try:
        typer.echo(f"🚀 Starting AI Studio on http://{host}:{port}")
        typer.echo("📱 FastUI interface will be available at the above URL")
        
        if debug:
            typer.echo("🐛 Debug mode enabled")
        
        if reload:
            # Use import string for reload functionality
            uvicorn.run(
                "app.server.app:create_app",
                factory=True,
                host=host,
                port=port,
                reload=reload,
                log_level="debug" if debug else "info",
            )
        else:
            # Use app object for normal operation
            from app.server.app import create_app
            app = create_app()
            uvicorn.run(
                app,
                host=host,
                port=port,
                reload=False,
                log_level="debug" if debug else "info",
            )
        
    except ImportError as e:
        typer.echo(f"❌ Error importing server components: {e}", err=True)
        typer.echo("💡 Make sure all dependencies are installed with: uv sync", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"❌ Error starting server: {e}", err=True)
        raise typer.Exit(1)


def check_health() -> None:
    """Check system health and dependencies"""
    typer.echo("🏥 AI Studio Health Check")
    typer.echo("=" * 40)
    
    # Check Python version
    import sys
    typer.echo(f"🐍 Python version: {sys.version}")
    
    # Check core dependencies
    dependencies = [
        ("fastapi", "FastAPI"),
        ("fastui", "FastUI"),
        ("plotly", "Plotly"),
        ("typer", "Typer"),
        ("uvicorn", "Uvicorn"),
    ]
    
    missing_deps = []
    
    for module_name, display_name in dependencies:
        try:
            __import__(module_name)
            typer.echo(f"✅ {display_name}: Available")
        except ImportError:
            typer.echo(f"❌ {display_name}: Missing")
            missing_deps.append(module_name)
    
    if missing_deps:
        typer.echo("\n💡 To install missing dependencies:")
        typer.echo("   uv sync")
        raise typer.Exit(1)
    else:
        typer.echo("\n🎉 All core dependencies are available!")


def manage_config(api_key: Optional[str], model: Optional[str], show: bool) -> None:
    """Manage configuration settings"""
    if show:
        typer.echo("📋 Current Configuration")
        typer.echo("=" * 30)
        typer.echo("🔧 Configuration management will be implemented in task 6")
        return
    
    if api_key:
        typer.echo("🔑 API key configuration will be implemented in task 6")
    
    if model:
        typer.echo("🤖 Model configuration will be implemented in task 6")
    
    if not any([api_key, model, show]):
        typer.echo("💡 Use --help to see available configuration options")