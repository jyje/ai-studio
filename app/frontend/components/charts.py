"""
Chart factory for creating Plotly visualizations.

This module provides factory functions for creating various types of
Plotly charts used throughout the AI Studio application.
"""

from typing import Dict, List, Any
import plotly.graph_objects as go
from plotly.graph_objects import Figure


class ChartFactory:
    """Factory class for creating standardized Plotly charts."""
    
    @staticmethod
    def create_vector_comparison_chart(data: Dict[str, Any]) -> Figure:
        """
        Create a vector store comparison chart.
        
        Args:
            data: Dictionary containing vector store comparison data
            
        Returns:
            Figure: Plotly figure for vector store comparison
        """
        fig = go.Figure()
        
        # Add placeholder data structure
        stores = data.get('stores', ['Store A', 'Store B', 'Store C'])
        relevance_scores = data.get('relevance_scores', [0.8, 0.7, 0.9])
        
        fig.add_trace(go.Bar(
            x=stores,
            y=relevance_scores,
            name='Relevance Score',
            marker_color='lightblue'
        ))
        
        fig.update_layout(
            title='Vector Store Comparison',
            xaxis_title='Vector Stores',
            yaxis_title='Relevance Score',
            template='plotly_white'
        )
        
        return fig
    
    @staticmethod
    def create_execution_flow_diagram(data: Dict[str, Any]) -> Figure:
        """
        Create an execution flow diagram for MCP operations.
        
        Args:
            data: Dictionary containing execution flow data
            
        Returns:
            Figure: Plotly figure for execution flow visualization
        """
        fig = go.Figure()
        
        # Add placeholder network diagram
        nodes = data.get('nodes', ['Start', 'MCP Call', 'Process', 'End'])
        
        fig.add_trace(go.Scatter(
            x=[1, 2, 3, 4],
            y=[1, 1, 1, 1],
            mode='markers+lines+text',
            text=nodes,
            textposition='top center',
            marker=dict(size=20, color='lightcoral'),
            line=dict(width=2, color='gray')
        ))
        
        fig.update_layout(
            title='MCP Execution Flow',
            showlegend=False,
            template='plotly_white',
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
        
        return fig
    
    @staticmethod
    def create_model_performance_chart(data: Dict[str, Any]) -> Figure:
        """
        Create a model performance comparison chart.
        
        Args:
            data: Dictionary containing model performance data
            
        Returns:
            Figure: Plotly figure for model performance comparison
        """
        fig = go.Figure()
        
        models = data.get('models', ['GPT-4', 'GPT-3.5', 'Claude'])
        response_times = data.get('response_times', [1.2, 0.8, 1.0])
        quality_scores = data.get('quality_scores', [0.9, 0.8, 0.85])
        
        fig.add_trace(go.Scatter(
            x=response_times,
            y=quality_scores,
            mode='markers+text',
            text=models,
            textposition='top center',
            marker=dict(size=15, color='lightgreen')
        ))
        
        fig.update_layout(
            title='Model Performance Comparison',
            xaxis_title='Response Time (seconds)',
            yaxis_title='Quality Score',
            template='plotly_white'
        )
        
        return fig