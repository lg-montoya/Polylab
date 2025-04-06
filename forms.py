from dash import html
import dash_bootstrap_components as dbc


gridlines_switch = html.Span([
        dbc.Label(className="fa-solid fa-square me-2", html_for="gridlines-toggle"),
        dbc.Switch(id="gridlines-toggle", value=False, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-table-cells me-1", html_for="gridlines-toggle"),
])

fluid_mode_switch = html.Span([
        dbc.Label(className="fa fa-mobile me-2", html_for="fluid-toggle"),
        dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-laptop", html_for="fluid-toggle"),
])

# THIS IS THE ARRANGEMENT FOR THE HORIZONTAL ALIGNMENT OF THE TOGGLES
# fluid_mode_switch =  html.Span(
#     [
#         dbc.Label(className="fa fa-mobile me-2", html_for="fluid-toggle"),
#         dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
#         dbc.Label(className="fa fa-laptop me-3", html_for="fluid-toggle"),
#     ]
# )