"""
User interface pages for AI Studio.

This module contains FastUI page implementations for AI users,
providing simple and intuitive interaction interfaces.
"""

from typing import List
from fastui import AnyComponent
from fastui.components import Page, Heading, Form, FormFieldInput, Paragraph, Link, Div, Text
from fastui.events import GoToEvent

# Rebuild models to ensure proper component definitions
Page.model_rebuild()
Heading.model_rebuild()
Form.model_rebuild()
FormFieldInput.model_rebuild()
Paragraph.model_rebuild()
Link.model_rebuild()
Div.model_rebuild()
Text.model_rebuild()


def create_user_page() -> List[AnyComponent]:
    """
    Create the user interface page with simple chat functionality.
    
    Returns:
        List[AnyComponent]: User page components
    """
    return [
        Page(
            components=[
                Heading(text='AI Assistant', level=1),
                Paragraph(text='Simple and intuitive interface for chatting with AI'),
                Form(
                    form_fields=[
                        FormFieldInput(
                            name='query', 
                            title='Ask me anything...', 
                            placeholder='Type your question and press Enter...'
                        )
                    ],
                    submit_url='/api/chat',
                    class_name='my-4'
                ),
                Div(
                    components=[
                        Link(
                            components=[Text(text='🏠 Back to Home')],
                            on_click=GoToEvent(url='/'),
                            class_name='btn btn-secondary'
                        ),
                        Link(
                            components=[Text(text='📊 Evaluator Mode')],
                            on_click=GoToEvent(url='/evaluator'),
                            class_name='btn btn-outline-success ms-2'
                        )
                    ],
                    class_name='mt-4'
                ),
                Paragraph(text='🚧 Chat interface will be implemented in task 5.4', class_name='text-muted mt-4')
            ]
        )
    ]