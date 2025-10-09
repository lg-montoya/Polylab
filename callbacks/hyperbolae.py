"""
Module containing (Non-cosmetic) Callbacks for the hyperbolae graphing app.
"""

from dash.dependencies import Input, Output, ALL
from dash import Patch


def callback_wrapper(app):
    # Update hyperbolae equation based on slider values
    @app.callback(
        Output("equation_hyperbolae", "children"),
        Input({"type": "hyperbolae_slider", "name": ALL}, "value"),
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
    
    import numpy as np
    from defaults.dash_components import SLIDER_MAX
    
    # Create x values, avoiding x = 0 to prevent division by zero
    x_negative = np.linspace(-SLIDER_MAX, -0.001, 200)
    x_positive = np.linspace(0.001, SLIDER_MAX, 200)
    
    @app.callback(
        Output("hyperbolae-graph", "figure", allow_duplicate=True),
        Input({"type": "hyperbolae_slider", "name": ALL}, "value"),
        prevent_initial_call=True,
    )
    def update_graph_from_sliders(coefficients):
        patched_figure = Patch()
    
        if not coefficients or len(coefficients) < 2:
            return patched_figure
        
        a, b, = coefficients
        
        # Vectorized calculation: y = a + b/x
        y_negative = a + b / x_negative
        y_positive = a + b / x_positive
        
        # Insert None values to break the line at the discontinuity
        x_combined = np.concatenate([x_negative, [None], x_positive])
        y_combined = np.concatenate([y_negative, [None], y_positive])
        
        # Update the trace data
        patched_figure["data"][0]["x"] = x_combined
        patched_figure["data"][0]["y"] = y_combined
        
        return patched_figure


