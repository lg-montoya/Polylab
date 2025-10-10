import dash_bootstrap_components as dbc
from dash import html, dcc
from factory import graph_generator, my_slider
from modals import MODAL_HYPERBOLAE_INSTRUCTIONS
from defaults.dash_components import slider_default
from defaults.cosmetics import graph_background_colours, STYLE_GRAPH_BORDER

axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)
flex_column_style = {
    "display": "flex",
    "flexDirection": "column",
    "justifyContent": "space-between",
}


tab = html.Div(
    [
        # ROW with just the instructions button
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
                                    id="btn-mdl-instructions-hyperbolae-open",
                                ),
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
                                # Spacer to push equation to middle
                                html.Div(style={"flex": "1"}),
                                # General form of the polynomial in LaTeX
                                html.Div(
                                    dcc.Markdown(
                                        rf"$$\Large y=a + \dfrac{{b}}{{x}}$$", 
                                        mathjax=True, 
                                        id="equation_hyperbolae",
                                    ),
                                    className="d-flex align-items-center justify-content-center",
                                ),
                                # Spacer to push sliders to bottom
                                html.Div(style={"flex": "1"}),
                                # Sliders
                                html.Div(
                                    [
                                        dbc.Row(
                                            my_slider(
                                                {
                                                    "type": "hyperbolae_slider",
                                                    "name": f"{i}",
                                                },
                                                f"{i}",
                                                disabled=False
                                            )
                                        )
                                        for i in ["a", "b",]
                                    ],
                                    style={
                                        **STYLE_GRAPH_BORDER,
                                        "background": graph_background_colours[
                                            "default_theme"
                                        ],
                                    },
                                    id="slider_hyperbolae_div",
                                ),
                            ],
                            style={"display": "flex", "flexDirection": "column", "height": "100%"},
                        ),
                    ],
                    style=flex_column_style,
                    sm=4,
                ),
                # Second column containing just the graph y=f(x)
                graph_generator(id="hyperbolae-graph", class_name="mt-sm-2-custom"),
            ]
        ),
        MODAL_HYPERBOLAE_INSTRUCTIONS,
    ],
    className="mt-3",
)

