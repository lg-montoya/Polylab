"""
Module containing (Non-cosmetic) Callbacks for the polynomial graphing app.
"""

import numpy as np
from dash.dependencies import Input, Output, ALL
from dash import Patch
from defaults.mathematics import SINUSOIDALS
from .factory import modal_close_callback

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


def handle_tangent_discontinuities(x_values, y_values, c):
    """
    Handle tangent function discontinuities by inserting None values at asymptotes.
    Following Polylab's mathematical accuracy patterns.
    """
    if c == 0:
        return x_values, y_values
    
    # Find asymptotes: tan(cx) is undefined when cx = π/2 + nπ
    # So x = (π/2 + nπ) / c
    asymptote_period = np.pi / abs(c)
    asymptote_offset = (np.pi / 2) / abs(c)
    
    # Find asymptotes within our domain
    n_min = int(np.floor((x_values.min() * abs(c) - np.pi/2) / np.pi))
    n_max = int(np.ceil((x_values.max() * abs(c) - np.pi/2) / np.pi))
    
    asymptotes = [(asymptote_offset + n * asymptote_period) * np.sign(c) 
                  for n in range(n_min, n_max + 1)
                  if x_values.min() <= (asymptote_offset + n * asymptote_period) * np.sign(c) <= x_values.max()]
    
    if not asymptotes:
        return x_values, y_values
    
    # Split domain at asymptotes and insert None values
    x_split = []
    y_split = []
    
    prev_idx = 0
    for asymptote in sorted(asymptotes):
        # Find the index closest to asymptote
        split_idx = np.searchsorted(x_values, asymptote)
        
        if split_idx > prev_idx:
            # Add segment before asymptote
            x_split.extend(x_values[prev_idx:split_idx])
            y_split.extend(y_values[prev_idx:split_idx])
            
            # Add discontinuity break
            if split_idx < len(x_values):
                x_split.append(None)
                y_split.append(None)
        
        prev_idx = split_idx
    
    # Add remaining segment
    if prev_idx < len(x_values):
        x_split.extend(x_values[prev_idx:])
        y_split.extend(y_values[prev_idx:])
    
    return np.array(x_split, dtype=object), np.array(y_split, dtype=object)



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
            # Handle potential domain issues following Polylab mathematical accuracy
            with np.errstate(invalid='ignore', divide='ignore'):
                y_values = a + b * math_function(c * x_values)
            
            # Handle tangent discontinuities specifically
            if function_type == "Tangent":
                x_values, y_values = handle_tangent_discontinuities(x_values, y_values, c)
            
        except Exception:
            # Fallback to zeros if calculation fails
            y_values = np.zeros_like(x_values)
        
        # Generate LaTeX-formatted title following polynomial patterns
        title = format_sinusoidal_title(a, b, c, function_type)

        # Update the trace data and title using Patch() pattern
        patched_figure["data"][0]["x"] = x_values
        patched_figure["data"][0]["y"] = y_values
        patched_figure["layout"]["title"]["text"] = title
                
        return patched_figure
    
    @app.callback(
            Output("sinusoidals-graph", "figure", allow_duplicate=True),
            Input("sinusoidals-unit-toggle", "value"),
            prevent_initial_call=True,  
        )
    def update_sinusoidals_xaxis_units(units):
        """Update x-axis labels between radians and degrees."""
        fig_patch = Patch()
        
        # Define the x-axis range in radians
        x_min, x_max = -6 * np.pi, 6 * np.pi
        
        if units:  # True means degrees
            # Create tick values in radians but show degree labels
            tick_radians = np.linspace(x_min, x_max, 25, endpoint=True)  # 9 evenly spaced ticks
            tick_degrees = [int(np.round(np.degrees(rad))) for rad in tick_radians]
            
            fig_patch["layout"]["xaxis"]["tickvals"] = tick_radians
            fig_patch["layout"]["xaxis"]["ticktext"] = [f"{deg}°" for deg in tick_degrees]
            fig_patch["layout"]["xaxis"]["title"]["text"] = "degrees"
        else:  # False means radians
            # Reset to default radian display
            fig_patch["layout"]["xaxis"]["tickvals"] = None
            fig_patch["layout"]["xaxis"]["ticktext"] = None
            fig_patch["layout"]["xaxis"]["title"]["text"] = "radians"
        
        return fig_patch
    
    modal_close_callback(app, "instructions-sinusoidals", link="btn")
    # modal_close_callback(app, "gridlines", link="btn")