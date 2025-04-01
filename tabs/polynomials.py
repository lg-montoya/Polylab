import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from defaults import POLYNOMIALS
from dash_bootstrap_templates import load_figure_template
from modals import modal_plolynomial_instructions
import plotly.graph_objects as go
from defaults import chart_default_theme, chart_other_theme, slider_default
from factory import my_slider

load_figure_template([chart_default_theme, chart_other_theme])
axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)

empty_figure = go.Figure()
empty_figure.update_layout(xaxis=axis, yaxis=axis,)


tab = html.Div([
            # ROW with just the instructions button
            dbc.Row([
                dbc.Col([
                    dbc.Button("Instructions", color="info", outline=False,id='btn-mdl-instructions-polynomials-open'),
                    modal_plolynomial_instructions
                        ], class_name='mb-3'
                    )],
                ),
            # ROW containing ALL the controls. This is subdivided itself into 2 columns. The first column has THREE rows.
            dbc.Row([
                dbc.Col([
                    # Row for the dropdown menu
                    dbc.Row(html.Div(dcc.Dropdown(id='dropdown_menu_1', options=[{'label': key, 'value': key} for key in POLYNOMIALS.keys()], 
                                    clearable=False, placeholder='CHOOSE A POLYNOMIAL'))),
                    # Row for the general form of the polynomial in LaTeX
                    dbc.Row(html.Div(dcc.Markdown("&nbsp;", mathjax=True, id='eq_1'), style={"textAlign": "center"}, className='mt-2')),
                    # Row for the sliders is contained in a card
                    dbc.Row(
                        html.Div(    
                        dbc.Card([                               
                           dbc.Row(my_slider("slider_1_a", "a"), className='mt-4'),
                           dbc.Row(my_slider("slider_1_b", "b")),
                           dbc.Row(my_slider("slider_1_c", "c")),
                           dbc.Row(my_slider("slider_1_d", "d")),                       
                        ], style={'width': '100%', 'height': '100%'})
                        )    
                    )], width=4, style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}),

                
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-y', mathjax=True)))
                    ], width=8, align='end'),
    
    
            ]),
            # ROW containing the second graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-d1y', mathjax=True)), )
                    ], width=8, class_name='mt-4'),
                
                ]),
            
            # ROW containing the third graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='polynomial-graph-d2y', mathjax=True)), )
                    ], width=8, class_name='mt-4'),
                
                ]),
             
], className="mt-4")