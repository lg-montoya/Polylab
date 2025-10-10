import dash_bootstrap_components as dbc
from dash import html, dcc
from factory import graph_generator, my_slider
from modals import MODAL_SINUSOIDALS_INSTRUCTIONS
from defaults.dash_components import slider_default, dropdown_sinusoidals_options
from defaults.cosmetics import graph_background_colours, STYLE_GRAPH_BORDER
import numpy as np
from dash import Patch

axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)
flex_column_style = {
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "space-between",
}


tab = html.Div(
    [
        # ROW with just the instructions and "+" button
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.Button(
                                    "Instructions",
                                    color="info",
                                    outline=False,
                                    id="btn-mdl-instructions-sinusoidals-open",
                                ),
                                # dbc.Button(
                                #     "+",
                                #     color="secondary",
                                #     id="dynamic-add-sinusoidals-btn",
                                #     className="me-md-2",
                                # ),
                            ],
                            className="d-grid gap-2 d-md-flex justify-content-md-start",
                        ),
                    ],
                    class_name="mb-2",
                    sm=2,
                )
            ]
        ),
        
        
        dbc.Row(
            [
                # First column containing just controls
                dbc.Col(
                    [
                        dbc.Stack(
                            [
                                # Dropdown menu
                                html.Div(
                                    dcc.Dropdown(
                                        id="dropdown_sinusoidals",
                                        options=dropdown_sinusoidals_options,
                                        clearable=False,
                                        placeholder="CHOOSE A SINUSOIDAL",
                                    ),
                                    className="d-grid",
                                ),
                                # General form of the sinusoidal in LaTeX
                                html.Div(
                                    dcc.Markdown("&nbsp;", mathjax=True, id="equation_sinusoidals"),
                                    style={"textAlign": "center"},
                                    className="mt-3",
                                ),
                                # Sliders
                                html.Div(
                                    [
                                        dbc.Row(
                                            my_slider(
                                                {
                                                    "type": "sinusoidals_slider",
                                                    "name": f"{i}",
                                                },
                                                f"{i}",
                                            )
                                        )
                                        for i in ["a", "b", "c"]
                                    ],
                                    style={
                                        **STYLE_GRAPH_BORDER,
                                        "background": graph_background_colours[
                                            "default_theme"
                                        ],
                                    },
                                    id="slider_sinusoidals_div",
                                ),
                            ],
                            style=flex_column_style,
                        ),
                    ],
                    style=flex_column_style,
                    sm=4,
                ),
                # Second column containing just the graph y=f(x)
                graph_generator(id="sinusoidals-graph", class_name="mt-sm-2-custom"),
            ]
        ),
        
        MODAL_SINUSOIDALS_INSTRUCTIONS,
    ],
    className="mt-4",
)