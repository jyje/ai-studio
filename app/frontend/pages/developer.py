"""
Developer interface pages for AI Studio.

This module contains FastUI page implementations for AI developers,
providing detailed monitoring, debugging, and analysis capabilities.
"""

from typing import List
from fastui import AnyComponent
from fastui.components import Page, Heading, Paragraph, Link, Div, Text, Button
from fastui.events import GoToEvent

# Rebuild models to ensure proper component definitions
Page.model_rebuild()
Heading.model_rebuild()
Paragraph.model_rebuild()
Link.model_rebuild()
Div.model_rebuild()
Text.model_rebuild()
Button.model_rebuild()


def create_developer_page() -> List[AnyComponent]:
    """
    Create the developer interface page with comprehensive monitoring tools.
    
    Returns:
        List[AnyComponent]: Developer page components
    """
    return [
        Page(
            components=[
                Heading(text='AI Developer Dashboard', level=1),
                Paragraph(text='Comprehensive monitoring and debugging tools for AI developers'),
                Paragraph(text='Available sections:'),
                Div(
                    components=[
                        Link(
                            components=[Text(text='🔍 Query Monitor')],
                            on_click=GoToEvent(url='/developer/monitor'),
                            class_name='btn btn-outline-primary mb-2 me-2'
                        ),
                        Link(
                            components=[Text(text='📊 Vector Store Comparison')],
                            on_click=GoToEvent(url='/developer/vectors'),
                            class_name='btn btn-outline-primary mb-2 me-2'
                        ),
                        Link(
                            components=[Text(text='🔄 Execution Flow')],
                            on_click=GoToEvent(url='/developer/flow'),
                            class_name='btn btn-outline-primary mb-2 me-2'
                        ),
                        Link(
                            components=[Text(text='🧪 Model Testing')],
                            on_click=GoToEvent(url='/developer/models'),
                            class_name='btn btn-outline-primary mb-2 me-2'
                        ),
                        Link(
                            components=[Text(text='⚙️ Configuration')],
                            on_click=GoToEvent(url='/developer/config'),
                            class_name='btn btn-outline-primary mb-2 me-2'
                        ),
                    ],
                    class_name='d-flex flex-wrap gap-2 my-3'
                ),
                Div(
                    components=[
                        Link(
                            components=[Text(text='🏠 Back to Home')],
                            on_click=GoToEvent(url='/'),
                            class_name='btn btn-secondary'
                        )
                    ],
                    class_name='mt-4'
                ),
                Paragraph(text='🚧 Developer interface components will be implemented in task 5.2', class_name='text-muted mt-4')
            ]
        )
    ]