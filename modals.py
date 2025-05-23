import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import POLYNOMIAL_INSTRUCTIONS, SINUSOIDAL_INSTRUCTIONS, WARNING_GRIDLINES

# Polynomial Instructions modal
MODAL_POLYNOMIAL_INSTRUCTIONS = dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle("Instructions")),
        dbc.ModalBody(children=[
            dcc.Markdown(POLYNOMIAL_INSTRUCTIONS),
        ]),
        dbc.ModalFooter(
            dbc.Button("Close", id="btn-mdl-instructions-polynomials-close", class_name="ml-auto")
        )
        
],id="mdl-instructions-polynomials", scrollable=True, centered=True,)

# Sinusoidals Instructions modal
MODAL_SINUSOIDAL_INSTRUCTIONS = dbc.Modal([
        dbc.ModalHeader("Instructions"),
        dbc.ModalBody(children=[
            dcc.Markdown(SINUSOIDAL_INSTRUCTIONS),
        ]),
        dbc.ModalFooter(
            dbc.Button("Close", id="btn-mdl-instructions-sinusoidals-close", class_name="ml-auto")
        ),
    ],
    id="mdl-instructions-sinusoidals", scrollable=True,
)

# Gridlines Warning modal
MODAL_GRIDLINES = dbc.Modal(
    [
        dbc.ModalHeader("Range Warning"),
        dbc.ModalBody(children=[
            dcc.Markdown(WARNING_GRIDLINES),
        ]),
        dbc.ModalFooter(
            # dbc.Button("Close", id="btn-mdl-gridlines-close", class_name="ml-auto")
        ),
    ],
    id="mdl-gridlines", scrollable=True,
)
