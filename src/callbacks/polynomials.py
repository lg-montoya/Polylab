"""
Module containing (Non-cosmetic) Callbacks for the polynomial graphing app.
"""

import numpy as np
from dash.dependencies import Input, Output, State, ALL
from dash import Patch
from src.constants.styles import TRACE_COLOURS
from src.constants.ui_defaults import slider_default["max"]
from src.constants.mathematics import derivative_notation, POLYNOMIALS
from src.utils.mathematical import PolynomialCalculator
from .factory import modal_callback


x_values = np.linspace(-slider_default["max"], slider_default["max"], 400)


# Wrapper function to register callbacks
def callback_wrapper(app):
    # Update general form of equation based on polynomial-dropdown selection
    @app.callback(Output("equation_polynomials", "children"), Input("dropdown_polynomials", "value"))
    def display_general_polynomial_form(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]["general_form"]

    # Update visibility and default slider values based on polynomial-dropdown selection.
    @app.callback(
        Output({"type": "polynomial_slider", "name": ALL}, "disabled"),
        Output({"type": "polynomial_slider", "name": ALL}, "value"),
        Input("dropdown_polynomials", "value"),
        prevent_initial_call=True,
    )
    def update_slider_visibility(chosen_polynomial):
        available_sliders = [
            not i for i in POLYNOMIALS[chosen_polynomial]["available_sliders"]
        ]
        default_coefficient_values = POLYNOMIALS[chosen_polynomial][
            "default_coefficients"
        ]
        return available_sliders, default_coefficient_values

    # Update f(x) graph based on slider values.
    @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Input({"type": "polynomial_slider", "name": ALL}, "value"),
        State("polynomial-graph-y", "figure"),
        prevent_initial_call=True,
    )
    def update_graph_from_sliders(coefficients, current_figure):
        patched_figure = Patch()

        y = PolynomialCalculator(coefficients)
        title = y.update_figure_title(*coefficients)
        d1y = y.derivative(order=1)
        d2y = y.derivative(order=2)

        y_values = y.evaluate(x_values)
        d1y_values = PolynomialCalculator(d1y.coef).evaluate(x_values)
        d2y_values = PolynomialCalculator(d2y.coef).evaluate(x_values)

        # Preserve current visibility state
        current_visibility = {}
        if current_figure and "data" in current_figure:
            for i, trace in enumerate(current_figure["data"]):
                if i < 3:  # Only for our 3 traces
                    current_visibility[i] = trace.get("visible", True)

        for i in range(3):
            patched_figure["data"][i]["x"] = x_values

        patched_figure["data"][0]["y"] = y_values
        patched_figure["data"][1]["y"] = d1y_values
        patched_figure["data"][2]["y"] = d2y_values

        patched_figure["data"][0]["name"] = rf"$y$"
        patched_figure["data"][1]["name"] = rf"${derivative_notation[1]}$"
        patched_figure["data"][2]["name"] = rf"${derivative_notation[2]}$"
        
        # Only set initial visibility if no current state exists
        if not current_visibility:
            # Initial state: main function visible, derivatives hidden
            patched_figure["data"][1]["visible"] = "legendonly"
            patched_figure["data"][2]["visible"] = "legendonly"
        else:
            # Preserve existing visibility state
            for i in range(3):
                if i in current_visibility:
                    patched_figure["data"][i]["visible"] = current_visibility[i]

        patched_figure["layout"]["title"]["text"] = title.replace("0.0 + ", "")

        return patched_figure


    # Update f'(x) and f''(x) graphs based on slider values.
    def update_derivative_graph(derivative_order):
        @app.callback(
            Output(
                f"polynomial-graph-d{derivative_order}y", "figure", allow_duplicate=True
            ),
            Input({"type": "polynomial_slider", "name": ALL}, "value"),
        )
        def inner_function(coefficients):
            patched_figure = Patch()

            coeffs = PolynomialCalculator(coefficients).derivative(order=derivative_order).coef
            # Remove erronous precision in poly.deriv.
            coeffs = [round(i, 3) for i in coeffs]
            poly = PolynomialCalculator(coeffs)

            # Update the title
            terms = [
                f"{coeff}x^{i}" if i > 0 else f"{coeff}"
                for i, coeff in enumerate(coeffs)
            ]
            derivative_str = (
                " + ".join(terms)
                .replace(" ", "")
                .replace("+0.0x^1", "")
                .replace("x^1", "x")
                .replace("+0.0x^2", "")
            )
            title = (
                rf"${derivative_notation[derivative_order]}={derivative_str}$".replace(
                    "=0.0+", "="
                )
            )

            patched_figure["data"][0]["x"] = x_values
            patched_figure["data"][0]["y"] = poly.evaluate(x_values)

            patched_figure["layout"]["title"]["text"] = title
            patched_figure["layout"]["showlegend"] = False

            # Always start on the default theme trace colour
            patched_figure["data"][0]["line"]["color"] = TRACE_COLOURS["default_theme"][
                derivative_order
            ]

            return patched_figure

    update_derivative_graph(1)
    update_derivative_graph(2)



    modal_callback(app, "instructions-polynomials", link="btn")