from dash import html, Input, Output
import dash_bootstrap_components as dbc



color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-sun", html_for="switch"),
        dbc.Switch(id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-moon", html_for="switch"),
    ]
)

# html.Div(
#                 dbc.Collapse(
#                     [dcc.Markdown(mathjax=True, id='eq_1', className="mt-2 mb-2"),
#                     # [dcc.Markdown(mathjax=True, id='eq_1', className="slider-label"),
                     
#                     html.Div(dbc.Row([
#                                 # dbc.Col(html.Label("a"), width=1),
#                                 dbc.Col(dcc.Markdown("$$a$$",mathjax=True), width=1),
#                                 dbc.Col(
#                                     dcc.Slider(
#                                         id="slider_1_a",
#                                         min=-5, max=5, value=1,
#                                         marks={i: str(i) for i in range(-5, 6)}
#                                         ),width=12
#                                         ),
#                                     ]),       
#                             ),
                    
#                     html.Div(dbc.Row([
#                                 # dbc.Col(html.Label("a"), width=1),
#                                 dbc.Col(dcc.Markdown("$$b$$",mathjax=True), width=1),
#                                 dbc.Col(
#                                     dcc.Slider(
#                                         id="slider_2_a",
#                                         min=-5, max=5, value=1,
#                                         marks={i: str(i) for i in range(-5, 6)}
#                                         ),width=12
#                                         ),
#                                     ]),       
#                             ),
                    
#                     html.Div(dbc.Row([
#                                 # dbc.Col(html.Label("a"), width=1),
#                                 dbc.Col(dcc.Markdown("$$c$$",mathjax=True), width=1),
#                                 dbc.Col(
#                                     dcc.Slider(
#                                         id="slider_3_a",
#                                         min=-5, max=5, value=1,
#                                         marks={i: str(i) for i in range(-5, 6)}
#                                         ),width=12
#                                         ),
#                                     ]),       
#                             ),
                    
#                     html.Div(dbc.Row([
#                                 # dbc.Col(html.Label("a"), width=1),
#                                 dbc.Col(dcc.Markdown("$$d$$",mathjax=True), width=1),
#                                 dbc.Col(
#                                     dcc.Slider(
#                                         id="slider_4_a",
#                                         min=-5, max=5, value=1,
#                                         marks={i: str(i) for i in range(-5, 6)}
#                                         ),width=12
#                                         ),
#                                     ]),       
#                             ),
                            