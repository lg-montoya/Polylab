import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import MOTIVATION

tab = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown(MOTIVATION, mathjax=True),
                        # html.Span(MOTIVATION),
                        html.A(
                            "*",  # Hyperlink text
                            id="hyperlink-popover",  # ID for the popover target
                            style={
                                "cursor": "pointer",
                                "textDecoration": "none",
                                "color": "blue",
                            },
                        ),
                        dbc.Popover(
                            dbc.PopoverBody(
                                "This is the additional information displayed in the pop-up.",
                                style={"padding": "0px"},
                            ),
                            target="hyperlink-popover",
                            body=True,
                            trigger="hover",
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="mt-4",
)
