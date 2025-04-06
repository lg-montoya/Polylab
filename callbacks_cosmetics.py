from dash import Patch
from dash.dependencies import Input, Output
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.io as pio
from defaults.cosmetics import trace_colours


def callback_wrapper(app, default_chart_theme, other_chart_theme):  

        @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d1y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d2y", "figure", allow_duplicate=True),
        Input("gridlines-radio", "value")  # Listen to the radio items' value
        )
        def update_gridlines(selected_value):
            # Create patches for the figures
            patched_figures = [Patch() for _ in range(3)]

            # Case selection based on the radio items' value
            match selected_value:
                case "blank":
                    for figure in patched_figures:
                        figure["layout"]["xaxis"]["showgrid"] = False
                        figure["layout"]["yaxis"]["showgrid"] = False
                case "few_gridlines":
                    for figure in patched_figures:
                        figure["layout"]["xaxis"]["dtick"] = 0
                        figure["layout"]["yaxis"]["dtick"] = 0
                        figure["layout"]["xaxis"]["showgrid"] = True
                        figure["layout"]["yaxis"]["showgrid"] = True
                case "more_gridlines":
                    for figure in patched_figures:
                        figure["layout"]["xaxis"]["dtick"] = 1
                        figure["layout"]["yaxis"]["dtick"] = 1
                        figure["layout"]["xaxis"]["showgrid"] = True
                        figure["layout"]["yaxis"]["showgrid"] = True

            return patched_figures


        # Update fluid-mode based on toggle
        @app.callback(
            Output("main-container", "fluid"),
            Input("fluid-toggle", "value")
        )
        def toggle_fluid_mode(is_fluid):
            return not is_fluid


        # Update trace colors based on toggle
        @app.callback(
            Output("polynomial-graph-y", "figure", allow_duplicate=True),
            Output(f"polynomial-graph-d1y", "figure", allow_duplicate=True),
            Output(f"polynomial-graph-d2y", "figure", allow_duplicate=True),
            Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        )
        def update_graph_from_sliders(is_dark):
            patch_figure = Patch()
            patched_figures = [Patch() for _ in range(2)]

            patch_figure["layout"]["template"] = (pio.templates[default_chart_theme] 
                                                if is_dark else pio.templates[other_chart_theme])    
            
            i=1
            if is_dark:
                for figure in patched_figures:
                    # figure["layout"]["xaxis"]["showgrid"]= False
                    # figure["layout"]["yaxis"]["showgrid"]= False
                    figure["layout"]["template"] = pio.templates[default_chart_theme]
                    figure['data'][0]['line']['color']=trace_colours['default_theme'][i]
                    i+=1
            else:
                for figure in patched_figures:
                    # figure["layout"]["xaxis"]["showgrid"]= True
                    # figure["layout"]["yaxis"]["showgrid"]= True
                    figure["layout"]["template"] = pio.templates[other_chart_theme]
                    figure['data'][0]['line']['color']=trace_colours['other_theme'][i]
                    i+=1 
                
            return patch_figure, *patched_figures
        
        