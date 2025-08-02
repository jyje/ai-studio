"""
Evaluator interface pages for AI Studio.

This module contains FastUI page implementations for AI evaluators,
providing simple and clear interfaces for quality assessment.
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


def create_evaluator_page() -> List[AnyComponent]:
    """
    Create the evaluator interface page with quality assessment tools.
    
    Returns:
        List[AnyComponent]: Evaluator page components
    """
    return [
        Page(
            components=[
                Heading(text='AI Evaluator Interface', level=1),
                Paragraph(text='Simple and clear interface for AI response quality assessment'),
                Form(
                    form_fields=[
                        FormFieldInput(
                            name='query', 
                            title='Enter Query to Evaluate', 
                            placeholder='Enter your query to see evaluation results...'
                        )
                    ],
                    submit_url='/api/evaluate',
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
                            components=[Text(text='🔧 Developer Mode')],
                            on_click=GoToEvent(url='/developer'),
                            class_name='btn btn-outline-primary ms-2'
                        )
                    ],
                    class_name='mt-4'
                ),
                Paragraph(text='🚧 Evaluation interface will be implemented in task 5.3', class_name='text-muted mt-4')
            ]
        )
    ]