import dash_bootstrap_components as dbc
from dash import html
from factory import plot_axes
from dash import dcc
from defaults import POLYNOMIALS,GENERAL_FORM
from dash_bootstrap_templates import load_figure_template

load_figure_template(["sketchy_dark", "minty"])


tab_0 = html.Div([
            # ROW with just the instructions button
            dbc.Row(
                dbc.Col(
                    dbc.Button("Instructions", color="info", outline=False,id='xx'), class_name='mb-3')
                ),
            # ROW containing ALL the controls. This is subdivided itself into 2 columns. The first column has THREE rows.
            dbc.Row([
                dbc.Col([
                    # Row for the dropdown menu
                    dbc.Row(html.Div(dcc.Dropdown(id='dropdown_menu_1', options=[{'label': key, 'value': key} for key in POLYNOMIALS.keys()], 
                                    clearable=False, placeholder='CHOOSE A POLYNOMIAL'))),
                    # Row for the general form of the polynomial in LaTeX
                    dbc.Row(html.Div(dcc.Markdown("&nbsp;", mathjax=True, id='eq_1'), style={"textAlign": "center"})),
                    # Row for the sliders is contained in a card
                    dbc.Row(
                        html.Div(    
                        dbc.Card([    
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad a$$",mathjax=True)), width=1, className='mt-4'),
                                dbc.Col(html.Div(dcc.Slider(updatemode='drag',disabled=True,id="slider_1_a",min=-5, max=5, marks={i: str(i) for i in range(-5, 6)})), width=11, className='mt-4 mb-3 '),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad b$$",mathjax=True)), width=1,),
                                dbc.Col(html.Div(dcc.Slider(updatemode='drag',disabled=True,id="slider_1_b",min=-5, max=5, marks={i: str(i) for i in range(-5, 6)})), width=11, className='mb-3'),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad c$$",mathjax=True)), width=1,),
                                dbc.Col(html.Div(dcc.Slider(updatemode='drag',disabled=True,id="slider_1_c",min=-5, max=5, marks={i: str(i) for i in range(-5, 6)})), width=11, className='mb-3'),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad d$$",mathjax=True)), width=1,),
                                dbc.Col(html.Div(dcc.Slider(updatemode='drag',disabled=True,id="slider_1_d",min=-5, max=5, marks={i: str(i) for i in range(-5, 6)})), width=11, className='mb-3'),
                            ]),                        
                        ], style={'width': '100%', 'height': '100%'})
                        )    
                    )], width=4, style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}),

                
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=plot_axes(), id='tab-0-graph', mathjax=True)), )
                    ], width=8),
    
    
            ]), 
        ], className="mt-4")