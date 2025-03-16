import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from defaults import POLYNOMIALS
from dash_bootstrap_templates import load_figure_template
from modals import modal_instructions
import plotly.graph_objects as go
from defaults import chart_default_theme, chart_other_theme, slider_default, trace_colours
from hardcoded import HISTORY
from factory import my_slider

load_figure_template([chart_default_theme, chart_other_theme])
# load_figure_template([chart_default_theme])

empty_figure = go.Figure()
empty_figure.update_layout(
    xaxis=dict(range=[slider_default["min"], slider_default["max"]], zeroline=True),
    yaxis=dict(range=[slider_default["min"], slider_default["max"]], zeroline=True),
)


tab_0 = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown(HISTORY, mathjax=True),
            html.A(id='tabla-topologia'),
            # html.H5("Información Geografica"),
            html.Div([
                # dbc.Button("Aceptar", outline=False, color="success", class_name="me-1", id='btn-aceptar'),
                # dbc.Button("Rechazar", outline=False, color="danger", class_name="me-1", id='btn-rechazar'),
                ])]
        )])
    ], className="mt-4")


tab_1 = html.Div([
            # ROW with just the instructions button
            dbc.Row([
                dbc.Col([
                    dbc.Button("Instructions", color="info", outline=False,id='btn-mdl-instructions-o'),
                    modal_instructions
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
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad a$$",mathjax=True)), width=1, className='mt-4'),
                                dbc.Col(html.Div(my_slider(slider_default["min"],slider_default["max"],"slider_1_a")), width=11, className='mt-4 mb-3 '),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad b$$",mathjax=True)), width=1),
                                dbc.Col(html.Div(my_slider(slider_default["min"],slider_default["max"],"slider_1_b")), width=11, className='mb-3'),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad c$$",mathjax=True)), width=1),
                                dbc.Col(html.Div(my_slider(slider_default["min"],slider_default["max"],"slider_1_c")), width=11, className='mb-3'),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div(dcc.Markdown("$$\quad d$$",mathjax=True)), width=1),
                                dbc.Col(html.Div(my_slider(slider_default["min"],slider_default["max"],"slider_1_d")), width=11, className='mb-3'),
                            ]),                        
                        ], style={'width': '100%', 'height': '100%'})
                        )    
                    )], width=4, style={'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}),

                
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='tab-0-graph-y', mathjax=True)))
                    ], width=8, align='end'),
    
    
            ]),
            # ROW containing the second graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='tab-0-graph-d1y', mathjax=True)), )
                    ], width=8, class_name='mt-4'),
                
                ]),
            
            # ROW containing the third graph
            dbc.Row([
                dbc.Col(),
                dbc.Col([
                    html.Div(
                        dbc.Card(dcc.Graph(figure=empty_figure, id='tab-0-graph-d2y', mathjax=True)), )
                    ], width=8, class_name='mt-4'),
                
                ]),
             
        ], className="mt-4")

tab_2 = html.Div(
    dbc.Row([
        dbc.Col(
            [html.H4(f'Coming soon ...'),]
        )
    ], class_name="mt-4")
)

tab_3 = html.Div(
    dbc.Row([
        dbc.Col(
            [html.H4(f'But first sinusoidals.'),]
        )
    ], class_name="mt-4")
)