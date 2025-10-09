"""
Module containing (Non-cosmetic) Callbacks for the hyperbolae graphing app.
"""

from dash.dependencies import Input, Output, ALL
from dash import callback


def callback_wrapper(app):
    # Update hyperbolae equation based on slider values
    @app.callback(
        Output("equation_hyperbolae", "children"),
        Input({"type": "hyperboalae_slider", "name": ALL}, "value"),
        prevent_initial_call=True,
    )
    def update_hyperbolae_equation(coefficients):
        if not coefficients or len(coefficients) < 2 or any(c is None for c in coefficients):
            return rf"$$\Large y=a + \dfrac{{b}}{{x}}$$"
        
        a, b = coefficients[0], coefficients[1]
        
        # Handle special cases for cleaner equation display
        if a == 0 and b == 0:
            return rf"$$\Large y=0$$"
        
        # Build equation parts
        parts = []
        
        # Handle 'a' term
        if a != 0:
            parts.append(str(a))
        
        # Handle 'b/x' term
        if b != 0:
            if b == 1:
                if parts:  # If there's already an 'a' term
                    parts.append(rf"+\dfrac{{1}}{{x}}")
                else:
                    parts.append(rf"\dfrac{{1}}{{x}}")
            elif b == -1:
                parts.append(rf"-\dfrac{{1}}{{x}}")
            else:
                if parts:  # There are existing terms
                    sign = "+" if b > 0 else "-"
                    abs_b = abs(b)
                    parts.append(rf"{sign}\dfrac{{{abs_b}}}{{x}}")
                else:  # First term
                    parts.append(rf"\dfrac{{{b}}}{{x}}")
        
        # Join parts and clean up
        equation = "".join(parts)
        if not equation:
            equation = "0"
        
        return rf"$$\Large y={equation}$$"

