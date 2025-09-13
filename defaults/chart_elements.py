import plotly.graph_objects as go
from .dash_components import slider_default

axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)

# Empty figure template for displaying a blank chart
empty_figure = go.Figure(
    layout={
        "xaxis": {
            "showgrid": False,  # Disable gridlines for the x-axis
            "dtick": 0,  # Set tick spacing to 1
            "zeroline": True,  # Show the zero line
            "zerolinewidth": 1,
            "zerolinecolor":'rgba(255, 255, 255, 0.35)',
            "ticklen":5,     
        },
        "yaxis": {
            "showgrid": False,  # Disable gridlines for the y-axis
            "dtick": 0,  # Set tick spacing to 1
            "zeroline": True,  # Show the zero line
            "zerolinewidth": 1,
            "zerolinecolor":'rgba(255, 255, 255, 0.35)',
            "ticklen":5, 
        },
    }
)

# Update the layout of the empty figure
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
    },
    hovermode='closest',
    newshape=dict(
        line=dict(
            color='yellow',  # Change this to any color you want
            width=3
        )
    ),
    modebar=dict(
        add=['drawline', 'drawopenpath', 'eraseshape'],
    ),
)

