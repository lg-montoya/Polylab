"""
Module containing callbacks related to the cosmetics of the app,
such as theme switching, gridlines, and fluid mode.
"""

from dash import Patch, clientside_callback, set_props, ctx
from dash.dependencies import Input, Output, State
from dash_bootstrap_templates import ThemeSwitchAIO
import plotly.io as pio
from defaults.cosmetics import trace_colours, graph_background_colours, APP_THEMES


# Allow instant theme switching in the browser without a round-trip to the server.
theme_js_dict = ",\n        ".join([f'"{k}": "{v}"' for k, v in APP_THEMES.items()])
clientside_callback_code = f"""
function(theme) {{
    const urls = {{
        {theme_js_dict}
    }};

    const linkTag = document.getElementById("theme-link");
    if (linkTag && urls[theme]) {{
        linkTag.href = urls[theme];
    }}
    return window.dash_clientside.no_update;
}}
"""
graph_background_colours


# Wrapper function to register callbacks
def callback_wrapper(app, chart_default_theme, chart_other_theme) -> None:
    # Allow instant theme switching in the browser without a round-trip to the server.
    clientside_callback(
        clientside_callback_code,
        Output("theme-link", "href"),
        Input("theme-store", "data"),
    )

    # Callback to update the gridlines of the graphs based on
    # the gridlines radio button selection.
    @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d1y", "figure", allow_duplicate=True),
        Output("polynomial-graph-d2y", "figure", allow_duplicate=True),
        Output("gridlines", "data"),
        Input("gridlines-radio", "value"),
        State("polynomial-graph-y", "figure"),
        State("polynomial-graph-d1y", "figure"),
        State("polynomial-graph-d2y", "figure"),
        prevent_initial_call=True,
    )
    def update_gridlines(gridline_amount, fig_y, fig_d1y, fig_d2y):
        # Create patches for the figures
        patched_figures = [Patch() for _ in range(3)]
        current_figs = [fig_y, fig_d1y, fig_d2y]

        small_range = []
        for fig in current_figs:
            x_range = fig.get("layout", {}).get("xaxis", {}).get("range", None)
            y_range = fig.get("layout", {}).get("yaxis", {}).get("range", None)
            small_range.append(max(x_range[1], y_range[1]) < 25)

        has_large_range = False

        # Determine amount of gridlines based on the selected option
        match gridline_amount:
            case "none":
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

    # Open modal warning when too many gridlines will be rendered
    @app.callback(
        Output("mdl-gridlines", "is_open"),
        Input("gridlines", "data"),
        prevent_initial_call=True,
    )
    def show_gridlines_modal(has_large_range):
        """Launch modal when gridlines store indicates large range"""
        return True if has_large_range else False

    # Update fluid-mode (affects app width) based on toggle
    @app.callback(Output("main-container", "fluid"), Input("fluid-toggle", "value"))
    def toggle_fluid_mode(is_fluid):
        return not is_fluid

    #     app.callback(
    # Output("daq-knob", "data-bs-theme"),
    # Input("theme-toggle", "value"),
    # )

    # Update trace (graph lines) colours based on toggle
    @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Output(f"polynomial-graph-d1y", "figure", allow_duplicate=True),
        Output(f"polynomial-graph-d2y", "figure", allow_duplicate=True),
        Input("theme-toggle", "value"),
    )
    def update_graph_from_sliders(is_dark):
        patch_function_figure = Patch()
        patched_derivative_figures = [Patch() for _ in range(2)]

        patch_function_figure["layout"]["template"] = (
            pio.templates[chart_default_theme]
            if is_dark
            else pio.templates[chart_other_theme]
        )

        i = 1
        if is_dark:
            for figure in patched_derivative_figures:
                figure["layout"]["template"] = pio.templates[chart_default_theme]
                figure["data"][0]["line"]["color"] = trace_colours["default_theme"][i]
                i += 1
        else:
            for figure in patched_derivative_figures:
                figure["layout"]["template"] = pio.templates[chart_other_theme]
                figure["data"][0]["line"]["color"] = trace_colours["other_theme"][i]
                i += 1

        return patch_function_figure, *patched_derivative_figures

    # Change background of sliders based on theme
    @app.callback(Output("slider_polynomials_div", "style"), Input("theme-toggle", "value"))
    def update_slider_background(is_dark):
        # Select the appropriate background color
        bg_color = (
            graph_background_colours["default_theme"]
            if is_dark
            else graph_background_colours["other_theme"]
        )

        updated_style = {
            "border": "1px solid var(--bs-primary)",
            "borderRadius": "6px",
            "overflow": "hidden",
            "background": bg_color,  # Dynamically set background color
        }
        return updated_style

    # Change background of cosmetics-controls-components based on theme
    @app.callback(
        Output("app-controls-div", "style"),
        Input("theme-toggle", "value"),
    )
    def update_contlros_background(is_dark):
        # Select the appropriate background color depending on the theme
        if is_dark:
            bg_color = graph_background_colours["default_theme"]
        else:
            bg_color = graph_background_colours["other_theme"]

        updated_style = {
            "border": "1px solid var(--bs-primary)",
            "borderRadius": "6px",
            "overflow": "hidden",
            "background": bg_color,  # Dynamically set background color
            "padding": "0.5rem",
            "margin": "0rem",
        }
        return updated_style

    # NO clue why this was needed, but it is used to sync the theme toggle with the theme store.
    @app.callback(
        Output("theme-toggle", "value"),
        Output("theme-store", "data"),
        Input("theme-toggle", "value"),
        Input("theme-store", "data"),
    )
    def sync_theme_toggle_and_store(toggle_value, store_data):
        trigger = ctx.triggered_id

        if trigger == "theme-toggle":
            # User toggled theme manually
            new_store = "default_theme" if toggle_value else "other_theme"
            return toggle_value, new_store
        elif trigger == "theme-store":
            # Theme store was updated elsewhere (e.g. from localStorage)
            new_toggle = True if store_data == "default_theme" else False
            return new_toggle, store_data
