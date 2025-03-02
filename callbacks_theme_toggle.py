from dash.dependencies import Input, Output
from dash import clientside_callback, Patch
import plotly.io as pio


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
        Output("tab-0-graph-y", "figure"),
        Input("switch", "value"),
    )
    def update_chart_theme(is_dark):
        template = pio.templates["sketchy_dark"] if is_dark else pio.templates["minty"]
        patched_figure = Patch()
        patched_figure["layout"]["template"] = template
        return patched_figure 
    
   