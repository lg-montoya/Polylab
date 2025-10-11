"""
    Module for creating generic repetitive callbacks in a Dash application.
    Possibly look at patter matching in Python 3.10+ for further simplification.
"""


from dash import Input, Output, State


def modal_close_callback(app, name, link="lnk"):
    @app.callback(
        Output(f"mdl-{name}", "is_open"),
        [
            Input(f"{link}-mdl-{name}-open", "n_clicks"),
            Input(f"btn-mdl-{name}-close", "n_clicks"),
        ],
        [State(f"mdl-{name}", "is_open")],
    )
    def function(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open