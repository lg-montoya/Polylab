from dash.dependencies import Input, Output, State
from dash import clientside_callback, Patch
import plotly.io as pio
from defaults import POLYNOMIALS
from factory import Polynomial, plot_axes    


clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-bs-theme', switchOn ? 'dark' : 'light');  
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)

            
def callback_wrapper(app):
    
    @app.callback(
        Output("tab-0-graph", "figure"),
        Input("switch", "value"),
    )
    def update_chart_theme(is_dark):
        template = pio.templates["sketchy_dark"] if is_dark else pio.templates["minty"]
        patched_figure = Patch()
        patched_figure["layout"]["template"] = template
        return patched_figure 
    
    # Callback for updating availability of sliders.
    @app.callback(
        Output("slider_1_a", "disabled"),
        Output("slider_1_b", "disabled"),
        Output("slider_1_c", "disabled"),
        Output("slider_1_d", "disabled"),
        Input("dropdown_menu_1", "value"),
    )
    def update_slider_status(chosen_polynomial):
        return [not i for i in POLYNOMIALS[chosen_polynomial]['available_sliders']]
    
    # Callback for updating general formula of the chosen polynomial.
    @app.callback(
        Output("eq_1", "children"),
        Input("dropdown_menu_1", "value"),
    )
    def update_general_formula(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]['general_form'] 
    
    # Callback for adding the default polynomial to the graph according to the chosen polynomial type.
    @app.callback(
        Output("tab-0-graph", "figure", allow_duplicate=True),
        Output("slider_1_a", "value"),
        Output("slider_1_b", "value"),
        Output("slider_1_c", "value"),
        Output("slider_1_d", "value"),
        Input("dropdown_menu_1", "value"),
        allow_duplicate=True  # Allow duplicate callback
    )
    def update_graph(selected_polynomial):
        if selected_polynomial is None:
            return Patch()  # Return an empty figure if no polynomial is selected

        coefficients = POLYNOMIALS[selected_polynomial]['default_coefficients']
        poly = Polynomial(coefficients)
        fig = plot_axes()  # Start with the axes

        # Add the polynomial trace
        poly_trace = poly.plot().data[0]
        fig.add_trace(poly_trace)

        return fig, *coefficients
    
        
    # Callback to add a new trace of the polynomial to the existing graph based on the slider values
    @app.callback(
        Output("tab-0-graph", "figure", allow_duplicate=True),
        Input("slider_1_a", "value"),
        Input("slider_1_b", "value"),
        Input("slider_1_c", "value"),
        Input("slider_1_d", "value"),
    )
    def update_graph_from_sliders(a, b, c, d):
        coefficients = [a, b, c, d]
        poly = Polynomial(coefficients)
        fig = plot_axes()  # Start with the axes

        # Add the polynomial trace
        poly_trace = poly.plot().data[0]
        fig.add_trace(poly_trace)
        return fig
 
    
    
    