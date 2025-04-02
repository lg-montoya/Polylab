from dash import html
import dash_bootstrap_components as dbc


fluid_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-mobile me-2", html_for="fluid-toggle"),
        dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-laptop", html_for="fluid-toggle"),
    ]
)
# fluid_mode_switch =  html.Span(
#     [
#         dbc.Label(className="fa fa-mobile me-2", html_for="fluid-toggle"),
#         dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
#         dbc.Label(className="fa fa-laptop me-3", html_for="fluid-toggle"),
#     ]
# )