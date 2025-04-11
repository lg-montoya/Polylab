from dash import Patch
from dash.dependencies import Input, Output, State
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.io as pio
from defaults.cosmetics import trace_colours, graph_background_colours


def callback_wrapper(app, default_chart_theme, other_chart_theme):  

        @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d1y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d2y", "figure", allow_duplicate=True),
        Output("gridlines", "data"),
        Input("gridlines-radio", "value"),
        State("polynomial-graph-y", "figure"),
        State("polynomial-graph-d1y", "figure"),
        State("polynomial-graph-d2y", "figure"),
        prevent_initial_call=True
        )
        def update_gridlines(selected_value, fig_y, fig_d1y, fig_d2y):
            # Create patches for the figures
            patched_figures = [Patch() for _ in range(3)]
            current_figs = [fig_y, fig_d1y, fig_d2y]
            
            small_range=[]
            for fig in current_figs:
                x_range = fig.get("layout", {}).get("xaxis", {}).get("range", None)
                y_range = fig.get("layout", {}).get("yaxis", {}).get("range", None)
                small_range.append(max(x_range[1], y_range[1]) < 25)

            has_large_range=False
            
            # Case selection based on the radio items' value
            match selected_value:
                case "blank":
                    for figure in patched_figures:
                        figure["layout"]["xaxis"]["dtick"] = 0
                        figure["layout"]["yaxis"]["dtick"] = 0
                        figure["layout"]["xaxis"]["showgrid"] = False
                        figure["layout"]["yaxis"]["showgrid"] = False
                case "few_gridlines":
                    for figure in patched_figures:
                        figure["layout"]["xaxis"]["dtick"] = 0
                        figure["layout"]["yaxis"]["dtick"] = 0
                        figure["layout"]["xaxis"]["showgrid"] = True
                        figure["layout"]["yaxis"]["showgrid"] = True
                case "more_gridlines":
                    for figure, is_small_range in zip(patched_figures, small_range):
                        dtick = 1 if is_small_range else 0
                        figure["layout"]["xaxis"]["dtick"] = dtick
                        figure["layout"]["yaxis"]["dtick"] = dtick
                        figure["layout"]["xaxis"]["showgrid"] = True 
                        figure["layout"]["yaxis"]["showgrid"] = True
                    
                    has_large_range = not all(small_range)
            
            return *patched_figures, has_large_range
        
        # ...existing code...

        @app.callback(
            Output("mdl-gridlines", "is_open"),
            Input("gridlines", "data"),
            prevent_initial_call=True
        )
        def show_gridlines_modal(has_large_range):
            """Launch modal when gridlines store indicates large range"""
            return True if has_large_range else False

        # ...existing code...


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
                    figure["layout"]["template"] = pio.templates[default_chart_theme]
                    figure['data'][0]['line']['color']=trace_colours['default_theme'][i]
                    i+=1
            else:
                for figure in patched_figures:
                    figure["layout"]["template"] = pio.templates[other_chart_theme]
                    figure['data'][0]['line']['color']=trace_colours['other_theme'][i]
                    i+=1 
                
            return patch_figure, *patched_figures
        
        @app.callback(
            Output("slider_div", "style"),
            Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        )
        def update_slider_div_background(is_dark):
            # Select the appropriate background color
            bg_color = graph_background_colours["default_theme"] if is_dark else graph_background_colours["other_theme"]

            # Return updated style
            return {
                "border": "1px solid var(--bs-primary)",
                "borderRadius": "6px",
                "overflow": "hidden",
                "padding": "12px",
                "background": bg_color,  # Dynamically set background color
            }
        
        