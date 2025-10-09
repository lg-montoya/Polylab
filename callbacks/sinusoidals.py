"""
Module containing (Non-cosmetic) Callbacks for the polynomial graphing app.
"""

import numpy as np
from dash.dependencies import Input, Output, State, ALL
from dash import Patch
from defaults.cosmetics import trace_colours
from defaults.mathematics import SINUSOIDALS

SLIDER_MAX = 10  # Assuming a constant for slider max value, adjust as needed


def format_sinusoidal_title(a, b, c, function_type):
    """
    Generate LaTeX-formatted title following MyPolynomial.update_figure_title() patterns.
    """
    func_name = SINUSOIDALS[function_type]["function_name"]
    parts = []
    
    # Handle constant term 'a' following polynomial formatting rules
    if a != 0:
        parts.append(str(int(a)) if a == int(a) else f"{a:.1f}")
    
    # Handle coefficient 'b' and function term
    if b != 0:
        # Format coefficient b following smart coefficient formatting
        if b == 1:
            coeff_str = ""
        elif b == -1:
            coeff_str = "-"
        else:
            coeff_str = str(int(b)) if b == int(b) else f"{b:.1f}"
        
        # Format argument 'c*x'
        if c == 1:
            arg_str = "x"
        elif c == -1:
            arg_str = "-x"
        else:
            c_str = str(int(c)) if c == int(c) else f"{c:.1f}"
            arg_str = f"{c_str}x"
        
        # Build function term with LaTeX
        func_term = f"{coeff_str}\\{func_name}({arg_str})"
        
        # Add appropriate sign if there are existing terms
        if parts and b > 0:
            func_term = "+" + func_term
        
        parts.append(func_term)
    
    # Join parts and handle edge cases
    if not parts:
        equation = "0"
    else:
        equation = "".join(parts)
        # Clean up formatting following polynomial title rules
        equation = equation.replace("+-", "-").lstrip("+")
    
    return f"$y = {equation}$"



# Wrapper function to register callbacks
def callback_wrapper(app):
    # Update general form of equation based on polynomial-dropdown selection
    @app.callback(Output("equation_sinusoidals", "children"), Input("dropdown_sinusoidals", "value"))
    def display_general_polynomial_form(chosen_sinusoidals):
        return SINUSOIDALS[chosen_sinusoidals]["general_form"]

    # Update visibility and default slider values based on polynomial-dropdown selection.
    @app.callback(
        Output({"type": "sinusoidals_slider", "name": ALL}, "disabled"),
        Output({"type": "sinusoidals_slider", "name": ALL}, "value"),
        Input("dropdown_sinusoidals", "value"),
        prevent_initial_call=True,
    )
    def update_slider_visibility(chosen_polynomial):
        available_sliders = [
            not i for i in SINUSOIDALS[chosen_polynomial]["available_sliders"]
        ]
        default_coefficient_values = SINUSOIDALS[chosen_polynomial][
            "default_coefficients"
        ]
        return available_sliders, default_coefficient_values
    
    
    # Update sinusoidals graph based on slider values and dropdown selection
    @app.callback(
        Output("sinusoidals-graph", "figure", allow_duplicate=True),
        Input({"type": "sinusoidals_slider", "name": ALL}, "value"),
        Input("dropdown_sinusoidals", "value"),
        prevent_initial_call=True,
    )
    def update_graph_from_sliders(coefficients, function_type):
        patched_figure = Patch()
        
        # Set default values if coefficients are missing
        if not coefficients or len(coefficients) < 3:
            a, b, c = SINUSOIDALS[function_type]["default_coefficients"]
        else:
            a, b, c = coefficients
        
        # Get the mathematical function from the SINUSOIDALS dictionary
        math_function = SINUSOIDALS[function_type]["function"]
        
        # Create x values for plotting
        x_values = np.linspace(-SLIDER_MAX, SLIDER_MAX, 1000)
        
        # Calculate y = a + b*FUNC(c*x)
        try:
            # Handle potential domain issues (e.g., tan at π/2)
            with np.errstate(invalid='ignore', divide='ignore'):
                y_values = a + b * math_function(c * x_values)
            
            # Clip extreme values for better visualization
            y_values = np.clip(y_values, -SLIDER_MAX*2, SLIDER_MAX*2)
            
        except Exception:
            # Fallback to zeros if calculation fails
            y_values = np.zeros_like(x_values)
            
        title = format_sinusoidal_title(a, b, c, function_type)
        
        # Update the trace data
        patched_figure["data"][0]["x"] = x_values
        patched_figure["data"][0]["y"] = y_values
        # patched_figure["data"][0]["name"] = f"y = {a} + {b}{function_type.lower()}({c}x)"
        patched_figure["layout"]["title"]["text"] = title
        
        return patched_figure
