import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import POLYNOMIAL_INSTRUCTIONS, SINUSOIDAL_INSTRUCTIONS

# Layout for modal on "Instructions" button.
modal_plolynomial_instructions = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Instructions")),
        dbc.ModalBody(children=[
            dcc.Markdown(POLYNOMIAL_INSTRUCTIONS),
        ]),
        dbc.ModalFooter(
            dbc.Button("Close", id="btn-mdl-instructions-polynomials-close", class_name="ml-auto")
        ),
    ],
    id="mdl-instructions-polynomials", scrollable=True, centered=True,
)

modal_sinusoidal_instructions = dbc.Modal(
    [
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
