import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from hardcoded import (
    POLYNOMIAL_INSTRUCTIONS, 
    HYPERBOLAE_INSTRUCTIONS,
    SINUSOIDALS_INSTRUCTIONS,
    WARNING_GRIDLINES,
)

def create_instructions_modal(modal_id: str, content: str, close_button_id: str, centered: bool = True) -> dbc.Modal:
    """
    Factory function to create instruction modals with consistent styling.
    
    Args:
        modal_id: Unique ID for the modal
        content: Markdown content to display
        close_button_id: ID for the close button
        centered: Whether to center the modal vertically
    
    Returns:
        dbc.Modal: Configured modal component
    """
    return dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("Instructions")),
            dbc.ModalBody(
                children=[
                    dcc.Markdown(content),
                ]
            ),
            dbc.ModalFooter(
                dbc.Button(
                    "Close",
                    id=close_button_id,
                    class_name="ml-auto",
                )
            ),
        ],
        id=modal_id,
        scrollable=True,
        centered=centered,
    )

# Polynomial Instructions modal
MODAL_POLYNOMIAL_INSTRUCTIONS = create_instructions_modal(
    modal_id="mdl-instructions-polynomials",
    content=POLYNOMIAL_INSTRUCTIONS,
    close_button_id="btn-mdl-instructions-polynomials-close"
)

# Hyperbolae Instructions modal
MODAL_HYPERBOLAE_INSTRUCTIONS = create_instructions_modal(
    modal_id="mdl-instructions-hyperbolae",
    content=HYPERBOLAE_INSTRUCTIONS,
    close_button_id="btn-mdl-instructions-hyperbolae-close",
    centered=False  # Matches original hyperbolae modal
)
# Sinusoidals Instructions modal
MODAL_SINUSOIDALS_INSTRUCTIONS = create_instructions_modal(
    modal_id="mdl-instructions-sinusoidals",
    content=SINUSOIDALS_INSTRUCTIONS,
    close_button_id="btn-mdl-instructions-sinusoidals-close",
    centered=False  # Matches original hyperbolae modal
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