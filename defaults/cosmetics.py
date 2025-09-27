import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.io as pio


# Themes for the app
default_theme_cdn = dbc.themes.CYBORG
other_theme_cdn = dbc.themes.QUARTZ
APP_THEMES = {"default_theme": default_theme_cdn, "other_theme": other_theme_cdn}

# Choose plotly template themes from either:
# ["quartz_dark", "vizro_dark", "vapor_dark", "vapor", "quartz"]
# These are the themes that apply specifically to the charts.
chart_default_theme = "quartz_dark"
chart_other_theme = "quartz"
load_figure_template([chart_default_theme, chart_other_theme])
FIGURE_TEMPLATE = {
    "default": pio.templates[chart_default_theme],
    "other": pio.templates[chart_other_theme],
}

# Extract trace colors from the themes
trace_default_theme_colours = list(FIGURE_TEMPLATE["default"]["layout"]["colorway"])
trace_other_theme_colours = list(FIGURE_TEMPLATE["other"]["layout"]["colorway"])
trace_colours = {
    "default_theme": {
        index: color_code
        for index, color_code in enumerate(trace_default_theme_colours)
    },
    "other_theme": {
        index: color_code for index, color_code in enumerate(trace_other_theme_colours)
    },
}

# Extract background colors from the themes
graph_background_colours = {
    "default_theme": FIGURE_TEMPLATE["default"]["layout"]["paper_bgcolor"],
    "other_theme": FIGURE_TEMPLATE["other"]["layout"]["paper_bgcolor"],
}

# Blue rounded border style for graphs
STYLE_GRAPH_BORDER = {
    "border": "1px solid var(--bs-primary)",
    "borderRadius": "6px",
    "overflow": "hidden",
}
