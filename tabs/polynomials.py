import dash_bootstrap_components as dbc
from dash import html, dcc
from defaults import POLYNOMIALS
from dash_bootstrap_templates import load_figure_template
from modals import modal_plolynomial_instructions
import plotly.graph_objects as go
from defaults import chart_default_theme, chart_other_theme, slider_default
from factory import my_slider

load_figure_template([chart_default_theme, chart_other_theme])
axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)
dropdown_polynomial_options = [{'label': key, 'value': key} for key in POLYNOMIALS.keys()]

empty_figure = go.Figure()
empty_figure.update_layout(
    xaxis=axis, 
    yaxis=axis,
    title={
        # 'x':0.05,
        'y':0.9, 
        'font':{'size': 15},
        'pad': {'t': 5, 'b': 0},
        },
    legend={
        'x': 1,  # Position the legend on the far right
        'y': 1,  # Position the legend at the top
        'xanchor': 'right',  # Anchor the legend's left side to the x position
        'yanchor': 'top',  # Anchor the legend's top side to the y position
        # 'orientation': 'h',  # Horizontal orientation
        # 'bordercolor': 'black',  # Black border around the legend
        # 'borderwidth': 1,  # Border width in pixels
    }  ,
    margin={
        'l': 22,  # Reduce left margin
        'r': 22,  # Reduce right margin
        't': 85,  # Reduce top margin
        'b': 20   # Reduce bottom margin
        # 'l': 25,  # Reduce left margin
        # 'r': 22,  # Reduce right margin
        # 't': 90,  # Reduce top margin
        # 'b': 30   # Reduce bottom margin
    }
    )

flex_column_style = {'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}

tab = html.Div([
            # ROW with just the instructions button
            dbc.Row([
                dbc.Col([
                    html.Div(    
                        dbc.Button("Instructions", color="primary", outline=False,id='btn-mdl-instructions-polynomials-open'),
                        className="d-grid"
                    ),
                    modal_plolynomial_instructions
                        ], class_name='mb-2', sm=2
                    )],
                ),
            
            # ROW of controls and y=f(x) graph.
            dbc.Row([
                # First column containing just controls
                dbc.Col([
                    dbc.Stack([
                        # Dropdown menu
                        html.Div(dcc.Dropdown(id='dropdown_menu_1', options=dropdown_polynomial_options, 
                                            clearable=False, placeholder='CHOOSE A POLYNOMIAL'), className="d-grid"),
                        # General form of the polynomial in LaTeX
                        html.Div(dcc.Markdown("&nbsp;", mathjax=True, id='eq_1'), style={"textAlign": "center"}, className='mt-3'),
                        # Sliders contained in a card
                        html.Div(
                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row(my_slider(f"polynomial_slider_{i}", f"{i}")) for i in ['a', 'b', 'c', 'd']
                                ]),
                                color="primary", outline=True
                            ),
                        )
                    ], style=flex_column_style),
            ], style=flex_column_style, sm=4),

                # Second column containing just the graph y=f(x)
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-y', mathjax=True))
                    )
                ], sm=8, className="mt-sm-2-custom"),
            ]),
            
            # ROW containing y=f'(x) graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-d1y', mathjax=True)), )
                    ], sm=8, class_name='mt-2'),
                
                ]),
            
            # ROW containing y=f''(x) graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-d2y', mathjax=True)), )
                    ], sm=8, class_name='mt-2'),
                
                ]),

], className="mt-4")