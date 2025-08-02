"""
AI Studio Main Entry Point

This is the single main entry point for the AI Studio application.
No other main.py files should be created in any subdirectories.
"""

import typer
from typing import Optional

app = typer.Typer(
    name="ais",
    help="AI Studio - FastUI와 Plotly를 통합한 RAG와 MCP 대화형 AI 스튜디오",
    add_completion=False,
)


@app.command()
def run(
    host: str = typer.Option("localhost", "--host", "-h", help="Host to bind to"),
    port: int = typer.Option(8000, "--port", "-p", help="Port to bind to"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode"),
    reload: bool = typer.Option(False, "--reload", "-r", help="Enable auto-reload"),
) -> None:
    """Run the AI Studio FastUI web interface"""
    from app.cli.commands import run_server
    
    run_server(host=host, port=port, debug=debug, reload=reload)


@app.command()
def health() -> None:
    """Check system health and dependencies"""
    from app.cli.commands import check_health
    
    check_health()


@app.command()
def config(
    api_key: Optional[str] = typer.Option(None, "--api-key", help="Set OpenAI API key"),
    model: Optional[str] = typer.Option(None, "--model", help="Set default model"),
    show: bool = typer.Option(False, "--show", help="Show current configuration"),
) -> None:
    """Configure API keys and models"""
    from app.cli.commands import manage_config
    
    manage_config(api_key=api_key, model=model, show=show)


@app.command()
def version() -> None:
    """Show AI Studio version"""
    from app import __version__
    typer.echo(f"AI Studio version {__version__}")


@app.callback()
def main() -> None:
    """AI Studio - FastUI와 Plotly를 통합한 RAG와 MCP 대화형 AI 스튜디오"""
    pass


if __name__ == "__main__":
    app()