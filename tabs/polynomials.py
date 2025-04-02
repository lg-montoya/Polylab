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
    # title={'x':0.05}
    title=
    {'font': {'color': 'rgba(255, 255, 255, 0.8784313725)', 'size': 15},
              'pad': {'b': 24, 'l': 24, 'r': 24, 't': 50},
              'x': 0,
              'xanchor': 'left',
              'xref': 'container',
            #   'y': 0.95,
              'y': 1,
            #   'text': 'y=f(x)',
              'yanchor': 'bottom',
            #   'yref': 'container'},
              'yref': 'paper'},
    )

flex_column_style = {'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}

tab = html.Div([
            # ROW with just the instructions button
            dbc.Row([
                dbc.Col([
                    html.Div(    
                        dbc.Button("Instructions", color="info", outline=False,id='btn-mdl-instructions-polynomials-open'),
                        className="d-grid"
                    ),
                    modal_plolynomial_instructions
                        ], class_name='mb-3', sm=4
                    )],
                ),
            
            # ROW of controls and y=f(x) graph.
            dbc.Row([
                # First column containing just controls
                dbc.Col([
                    dbc.Stack([
                        # Dropdown menu
                        html.Div(dcc.Dropdown(id='dropdown_menu_1', options=dropdown_polynomial_options, 
                                            clearable=False, placeholder='CHOOSE A POLYNOMIAL'), className="d-grid gap-2"),
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