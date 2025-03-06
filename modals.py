import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import POLYNOMIAL_INSTRUCTIONS

# Layout for modal on "Instructions" button.
modal_instructions = dbc.Modal(
    [
        dbc.ModalHeader("Instructions"),
        dbc.ModalBody(children=[
            dcc.Markdown(POLYNOMIAL_INSTRUCTIONS),
        ]),
        dbc.ModalFooter(
            dbc.Button("Close", id="btn-mdl-instructions-q", class_name="ml-auto")
        ),
    ],
    id="mdl-instructions", scrollable=True,
)
