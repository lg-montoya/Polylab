import dash_bootstrap_components as dbc
from dash import html


tab = html.Div(
    dbc.Row([
        dbc.Col(
            [html.H4(f'But first sinusoidals.'),]
        )
    ], class_name="mt-4")
)