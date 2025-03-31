import dash_bootstrap_components as dbc
from dash import html


tab = html.Div(
    dbc.Row([
        dbc.Col(
            [html.H4(f'Coming soon ...'),]
        )
    ], class_name="mt-4")
)