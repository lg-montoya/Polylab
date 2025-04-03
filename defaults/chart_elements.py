import plotly.graph_objects as go
from .dash_components import slider_default

axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)

empty_figure = go.Figure()
empty_figure.update_layout(
    xaxis=axis, 
    yaxis=axis,
    title={
        'y': 0.9, 
        'font': {'size': 15},
        'pad': {'t': 5, 'b': 0},
        },
    legend={
        'x': 1,
        'y': 1,
        'xanchor': 'right',  
        'yanchor': 'top',  
    },
    margin={
        'l': 22, 'r': 22,  
        't': 85, 'b': 20   
    }
)
