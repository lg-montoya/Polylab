import dash
import dash_bootstrap_components as dbc
from layout import page_layout
from callbacks import clientside_callback, callback_wrapper


MATHJAX_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/MathJax.js?'

external_scripts = ['https://polyfill.io/v3/polyfill.min.js?features=es6',
                    {'type': 'text/javascript',
                     'id': 'MathJax-script',
                     'src': MATHJAX_CDN,
                     },
                    ]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css, dbc.icons.FONT_AWESOME]



app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1"}],
                prevent_initial_callbacks=True)


server=app.server
app.layout = page_layout()
app.scripts.config.serve_locally = True  # Needed for Dash DAQ components
clientside_callback
callback_wrapper(app)

# app.layout = html.Div([
#     # dcc.Markdown(f"### Polynomial: {poly.latex()}", dangerously_allow_html=True)
#     dcc.Graph(figure=poly.plot())
# ])

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True)


# import dash
# from dash import dcc, html, Input, Output, State
# import dash_bootstrap_components as dbc
# import numpy as np
# import plotly.graph_objects as go

# # List of Bootstrap themes
# BOOTSTRAP_THEMES = [
#     "bootstrap", "cerulean", "cosmo", "cyborg", "darkly", "flatly", "journal", "litera", "lumen", "lux",
#     "materia", "bootstrap", "morph", "pulse", "quartz", "sandstone", "simplex", "sketchy", "slate", "solar",
#     "spacelab", "superhero", "united", "vapor", "yeti", "zephyr"
# ]

# def generate_polynomial(a, b, c, d, x):
#     return a * x**3 + b * x**2 + c * x + d

# # Initialize the app
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# # Layout of the app
# app.layout = dbc.Container([
#     html.H1("Polynomial Explorer", className="text-center mt-4"),

#     # Dropdown for theme selection
#     dbc.Row([
#         dbc.Col([
#             html.Label("Select Theme"),
#             dcc.Dropdown(
#                 id="theme-dropdown",
#                 options=[{"label": theme.capitalize(), "value": theme} for theme in BOOTSTRAP_THEMES],
#                 value="bootstrap"
#             )
#         ])
#     ], className="mb-4"),

#     # Tabs
#     dbc.Tabs([
#         dbc.Tab(label="Polynomials", tab_id="tab-polynomials"),
#         dbc.Tab(label="Other", tab_id="tab-other")
#     ], id="tabs", active_tab="tab-polynomials"),

#     # Content for the active tab
#     html.Div(id="tab-content"),

#     # Dropdown for polynomial selection (always present in layout)
#     dcc.Dropdown(
#         id="polynomial-dropdown",
#         options=[
#             {"label": "Linear", "value": "linear"},
#             {"label": "Quadratic", "value": "quadratic"},
#             {"label": "Cubic", "value": "cubic"},
#             {"label": "Reciprocal", "value": "reciprocal"},
#             {"label": "Exponential", "value": "exponential"}
#         ],
#         value="choose",
#         placeholder="Choose a polynomial",
#         className="mb-3"
#     ),

#     # Sliders (always present in the layout)
#     html.Div([
#         html.Div([
#             html.Label(f"{letter}:"),
#             dcc.Slider(
#                 id=f"slider-{letter}",
#                 min=-5, max=5, step=1, value=1,
#                 marks={i: str(i) for i in range(-5, 6)}
#             ),
#             html.Div(id=f"slider-value-{letter}")
#         ], className="mb-3") for letter in ["a", "b", "c", "d"]
#     ], id="sliders-container", style={"display": "none"}),

#     # Graph (always present in the layout)
#     dcc.Graph(id="polynomial-graph", style={"display": "none"}),

#     # Button for popup (always in the layout)
#     dbc.Button("Show Info", id="info-button", color="primary", className="mb-2", style={"display": "none"}),

#     # Modal for information popup
#     dbc.Modal([
#         dbc.ModalHeader("Info"),
#         dbc.ModalBody("This is a short random sentence!"),
#         dbc.ModalFooter(
#             dbc.Button("Close", id="close-button", className="ms-auto", n_clicks=0)
#         )
#     ], id="info-popup", is_open=False),

#     # Polynomial info (always present in layout)
#     html.Div(id="polynomial-info", style={"display": "none"})
# ], fluid=True)

# # Layout for the Polynomials tab
# def polynomials_tab():
#     return dbc.Row([
#         # Column 1: Dropdown and info
#         dbc.Col([
#             html.Div([
#                 dcc.Dropdown(
#                     id="polynomial-dropdown-visible",
#                     options=[
#                         {"label": "Linear", "value": "linear"},
#                         {"label": "Quadratic", "value": "quadratic"},
#                         {"label": "Cubic", "value": "cubic"},
#                         {"label": "Reciprocal", "value": "reciprocal"},
#                         {"label": "Exponential", "value": "exponential"}
#                     ],
#                     value="choose",
#                     placeholder="Choose a polynomial",
#                     className="mb-3"
#                 ),
#                 html.Div(id="polynomial-info-visible", className="mt-2 mb-3")
#             ])
#         ], width=3),
#     ])

# # Callback to render tab content
# @app.callback(
#     [Output("tab-content", "children"),
#      Output("sliders-container", "style"),
#      Output("polynomial-graph", "style"),
#      Output("info-button", "style"),
#      Output("polynomial-info", "style")],
#     Input("tabs", "active_tab")
# )
# def render_tab_content(active_tab):
#     if active_tab == "tab-polynomials":
#         return polynomials_tab(), {"display": "block"}, {"display": "block"}, {"display": "block"}, {"display": "block"}
#     elif active_tab == "tab-other":
#         return html.Div("This is the Other tab."), {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}
#     return None, {"display": "none"}, {"display": "none"}, {"display": "none"}, {"display": "none"}

# # Callback to update polynomial info
# @app.callback(
#     Output("polynomial-info", "children"),
#     Output("slider-a", "value"),
#     Output("slider-b", "value"),
#     Output("slider-c", "value"),
#     Output("slider-d", "value"),
#     Input("polynomial-dropdown", "value")
# )
# def update_polynomial_info(selected_polynomial):
#     if selected_polynomial == "choose":
#         return "", 1, 1, 1, 1
#     else:
#         equations = {
#             "linear": "f(x) = ax + b",
#             "quadratic": "f(x) = ax^2 + bx + c",
#             "cubic": "f(x) = ax^3 + bx^2 + cx + d",
#             "reciprocal": "f(x) = a / x",
#             "exponential": "f(x) = a * e^(bx)"
#         }
#         return f"Selected Polynomial: {equations.get(selected_polynomial, '')}", 1, 1, 1, 1

# # Callback to toggle popup
# @app.callback(
#     Output("info-popup", "is_open"),
#     [Input("info-button", "n_clicks"), Input("close-button", "n_clicks")],
#     [State("info-popup", "is_open")]
# )
# def toggle_popup(info_clicks, close_clicks, is_open):
#     if info_clicks or close_clicks:
#         return not is_open
#     return is_open

# # Callback to update slider values and graph
# @app.callback(
#     [Output(f"slider-value-{letter}", "children") for letter in "abcd"] +
#     [Output("polynomial-graph", "figure")],
#     [Input(f"slider-{letter}", "value") for letter in "abcd"]
# )
# def update_graph(a, b, c, d):
#     x = np.linspace(-10, 10, 500)
#     y = generate_polynomial(a, b, c, d, x)

#     # Create the figure
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Polynomial"))
#     fig.update_layout(
#         title=f"f(x) = {a}x^3 + {b}x^2 + {c}x + {d}",
#         xaxis_title="x",
#         yaxis_title="f(x)",
#         template="plotly_white"
#     )

#     return [f"Value: {v}" for v in [a, b, c, d]] + [fig]

# if __name__ == "__main__":
#     app.run_server(debug=True)
