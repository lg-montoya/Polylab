from dash.dependencies import Input, Output, State
from dash import clientside_callback, Patch
import plotly.io as pio
from defaults import POLYNOMIALS


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
    

    @app.callback(
        Output("collapse_1", "is_open"),
        Input("dropdown_menu_1", "value"),
        [State("collapse_1", "is_open")]
    )
    def reveal_coefficients(selected_value, is_open):
        if selected_value is not None:
            return True
        return False
    
    
    @app.callback(
        Output("eq_1", "children"),
        Input("dropdown_menu_1", "value"),
    )
    def update_general_formula(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]['general_form'] 