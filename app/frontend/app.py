"""
FastUI application main module.

This module contains the main FastUI application setup and configuration.
"""

from typing import List

from fastui import AnyComponent, FastUI
from fastui.components import Button, Div, Heading, Link, Page, Paragraph, Text
from fastui.events import GoToEvent

# Rebuild models to ensure proper component definitions
Page.model_rebuild()
Heading.model_rebuild()
Paragraph.model_rebuild()
Link.model_rebuild()
Div.model_rebuild()
Text.model_rebuild()
Button.model_rebuild()


def create_fastui_app() -> List[AnyComponent]:
    """
    Create and configure the main FastUI application.

    Returns:
        List[AnyComponent]: The main FastUI application components
    """
    return [
        Page(
            components=[
                Heading(text="AI Studio", level=1, class_name="text-center mb-4"),
                Paragraph(
                    text="FastUI + Plotly Integration for RAG and MCP Interactive AI Studio",
                    class_name="text-center text-muted mb-5",
                ),
                Heading(
                    text="Select Your Role", level=2, class_name="text-center mb-4"
                ),
                Div(
                    components=[
                        Link(
                            components=[
                                Div(
                                    components=[
                                        Heading(text="🔧 AI Developer", level=3),
                                        Paragraph(
                                            text="Comprehensive monitoring, debugging, and performance analysis tools"
                                        ),
                                    ],
                                    class_name="text-center",
                                )
                            ],
                            on_click=GoToEvent(url="/developer"),
                            class_name="btn btn-warning btn-lg p-4 m-2 text-decoration-none w-100",
                        ),
                        Link(
                            components=[
                                Div(
                                    components=[
                                        Heading(text="📊 AI Evaluator", level=3),
                                        Paragraph(
                                            text="Simple and clear interface for AI response quality assessment"
                                        ),
                                    ],
                                    class_name="text-center",
                                )
                            ],
                            on_click=GoToEvent(url="/evaluator"),
                            class_name="btn btn-success btn-lg p-4 m-2 text-decoration-none w-100",
                        ),
                        Link(
                            components=[
                                Div(
                                    components=[
                                        Heading(text="💬 AI User", level=3),
                                        Paragraph(
                                            text="Simple and intuitive interface for chatting with AI"
                                        ),
                                    ],
                                    class_name="text-center",
                                )
                            ],
                            on_click=GoToEvent(url="/user"),
                            class_name="btn btn-info btn-lg p-4 m-2 text-decoration-none w-100",
                        ),
                    ],
                    class_name="d-flex flex-column align-items-center gap-3 w-75 mx-auto",
                ),
                Paragraph(
                    text="Navigate between roles seamlessly with the Back to Home button on each page",
                    class_name="text-center text-muted mt-5",
                ),
            ]
        ),
    ]
