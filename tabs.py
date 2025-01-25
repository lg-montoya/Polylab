import dash_bootstrap_components as dbc
from dash import html
from factory import Polynomial
from dash import dcc
from defaults import POLYNOMIALS,GENERAL_FORM
from dash_bootstrap_templates import load_figure_template

load_figure_template(["sketchy_dark", "minty"])

poly = Polynomial([1, 1, 1])




tab_0 = html.Div([
            # ROW with just the instructions button
            dbc.Row(
                dbc.Col(
                    dbc.Button("Instructions", color="info", outline=False,id='xx'), class_name='mb-3')
                ),

            dbc.Row([
                dbc.Col([
                    html.Div(dcc.Dropdown(id='dropdown_menu_1', options=[{'label': key, 'value': key} for key in POLYNOMIALS.keys()], 
                                          clearable=False, placeholder='CHOOSE A POLYNOMIAL', className="mb-4 mt-2")),
                    html.Div(dcc.Markdown(mathjax=True, id='eq_1'), style={"textAlign": "center"}),
                    
                    
                    dbc.Card([ 
                        dbc.Row([
                            dbc.Label(html.Div(dcc.Markdown("$$\quad a$$",mathjax=True)), width='1'),
                            dbc.Col(dcc.Slider(id="slider_1_a",min=-5, max=5, value=1,marks={i: str(i) for i in range(-5, 6)}, className="mt-4 mb-4",), width=11),
                        ]),
                        dbc.Row([
                            dbc.Label(html.Div(dcc.Markdown("$$\quad b$$",mathjax=True)), width=1),
                            dbc.Col(dcc.Slider(id="slider_1_b",min=-5, max=5, value=1,marks={i: str(i) for i in range(-5, 6)}, className="mb-4"), width=11),
                        ]),
                        dbc.Row([
                            dbc.Label(html.Div(dcc.Markdown("$$\quad c$$",mathjax=True)), width=1),
                            dbc.Col(dcc.Slider(id="slider_1_c",min=-5, max=5, value=1,marks={i: str(i) for i in range(-5, 6)}, className="mb-4"), width=11),
                        ]),
                        dbc.Row([
                            dbc.Label(html.Div(dcc.Markdown("$$\quad d$$",mathjax=True)), width=1),
                            dbc.Col(dcc.Slider(id="slider_1_d",min=-5, max=5, value=1,marks={i: str(i) for i in range(-5, 6)}), width=11),
                        ])
                    ]),
                ], width=4),

                
                dbc.Col([
                    html.Div(
                        dbc.Card(dbc.CardBody(dcc.Graph(figure=poly.plot(), id='tab-0-graph')), ))
                    ], width=8, class_name="mt-2"),
    
    
            ]), 
        ], className="mt-4")