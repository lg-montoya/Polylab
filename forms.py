from dash import html
import dash_bootstrap_components as dbc


fluid_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-mobile me-2", html_for="fluid-toggle"),
        dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-laptop me-3", html_for="fluid-toggle"),
        # dbc.Label(className="fa fa-laptop", html_for="fluid-toggle"),
    ]
)

# fullscreen_toggle = html.Span(
#     [
#         dbc.Label(className="fa fa-mobile me-2", html_for="fullscreen-toggle"),
#         dbc.Switch(id="fullscreen-toggle", value=False, className="d-inline-block"),
#         dbc.Label(className="fa fa-laptop me-2", html_for="fullscreen-toggle"),
#     ]
# )

# fullscreen_toggle = html.Span(
#     [
#         dbc.Label("Fullscreen", html_for="fullscreen-toggle", className="me-2"),
#         dbc.Switch(id="fullscreen-toggle", value=False, className="d-inline-block"),
#     ]
# )