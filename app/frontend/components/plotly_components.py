"""
Plotly integration components for FastUI.

This module provides custom FastUI components for embedding Plotly charts
and handling Plotly-FastUI interactions.
"""

from typing import Dict, Any, Optional
from pydantic import BaseModel
from fastui.components import Div
from plotly.graph_objects import Figure
import plotly.io as pio


class PlotlyChart(BaseModel):
    """
    Custom FastUI component for embedding Plotly charts.
    
    This component renders Plotly figures within FastUI containers
    with proper styling and interaction handling.
    """
    figure: Figure
    height: int = 400
    width: Optional[int] = None
    config: Dict[str, Any] = {}
    
    def render(self) -> Div:
        """
        Render the Plotly chart as a FastUI Div component.
        
        Returns:
            Div: FastUI Div component containing the Plotly chart
        """
        chart_config = {
            'displayModeBar': True,
            'responsive': True,
            **self.config
        }
        
        chart_html = pio.to_html(
            self.figure,
            include_plotlyjs='cdn',
            config=chart_config,
            div_id=f"plotly-chart-{id(self)}",
            full_html=False
        )
        
        return Div(
            components=[],
            class_name="plotly-container",
            html_content=chart_html
        )


class MetricsCard(BaseModel):
    """
    Metrics display card component for FastUI.
    
    This component displays key metrics in a card format
    with proper styling and optional descriptions.
    """
    title: str
    value: str
    description: Optional[str] = None
    color: str = "primary"
    
    def render(self) -> Dict[str, Any]:
        """
        Render the metrics card as FastUI component data.
        
        Returns:
            Dict[str, Any]: FastUI component data for the metrics card
        """
        return {
            "type": "Card",
            "components": [
                {"type": "Heading", "text": self.title, "level": 4},
                {
                    "type": "Paragraph", 
                    "text": self.value, 
                    "class_name": f"text-{self.color} h2"
                },
                {
                    "type": "Paragraph", 
                    "text": self.description
                } if self.description else None
            ]
        }