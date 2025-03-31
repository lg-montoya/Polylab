import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import HISTORY

tab = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Markdown(HISTORY, mathjax=True),
            html.A(id='tabla-topologia'),
        ])
    ])
], className="mt-4")