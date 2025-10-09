import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import (
    POLYNOMIAL_INSTRUCTIONS, 
    HYPERBOLAE_INSTRUCTIONS,
    WARNING_GRIDLINES,
)

# Polynomial Instructions modal
MODAL_POLYNOMIAL_INSTRUCTIONS = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Instructions")),
        dbc.ModalBody(
            children=[
                dcc.Markdown(POLYNOMIAL_INSTRUCTIONS),
            ]
        ),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="btn-mdl-instructions-polynomials-close",
                class_name="ml-auto",
            )
        ),
    ],
    id="mdl-instructions-polynomials",
    scrollable=True,
    centered=True,
)

# Hyperbolae Instructions modal
MODAL_HYPERBOLAE_INSTRUCTIONS = dbc.Modal(
    [
        dbc.ModalHeader("Instructions"),
        dbc.ModalBody(
            children=[
                dcc.Markdown(HYPERBOLAE_INSTRUCTIONS),
            ]
        ),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="btn-mdl-instructions-hyperbolae-close",
                class_name="ml-auto",
            )
        ),
    ],
    id="mdl-instructions-hyperbolae",
    scrollable=True,
)

# Gridlines Warning modal
MODAL_GRIDLINES = dbc.Modal(
    [
        dbc.ModalHeader("Range Warning"),
        dbc.ModalBody(
            children=[
                dcc.Markdown(WARNING_GRIDLINES),
            ]
        ),
        dbc.ModalFooter(
            # dbc.Button("Close", id="btn-mdl-gridlines-close", class_name="ml-auto")
        ),
    ],
    id="mdl-gridlines",
    scrollable=True,
)
