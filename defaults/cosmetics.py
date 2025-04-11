import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.io as pio

page_default_theme= dbc.themes.CYBORG
page_other_theme = dbc.themes.QUARTZ

# Choose from 
["quartz_dark", "vizro_dark", "vapor_dark", "vapor", "quartz"]
chart_default_theme = "quartz_dark"
chart_other_theme = "quartz"

load_figure_template([chart_default_theme, chart_other_theme])
chart_other_theme_colours = list(pio.templates[chart_other_theme]["layout"]["colorway"])
chart_default_theme_colours = list(pio.templates[chart_default_theme]["layout"]["colorway"])

trace_colours = {
    'default_theme':{index:color_code for index, color_code in enumerate(chart_default_theme_colours)},
    'other_theme': {index:color_code for index, color_code in enumerate(chart_other_theme_colours)}
}

# Extract background colors from the themes
graph_background_colours = {
    "default_theme": pio.templates[chart_default_theme]["layout"]["paper_bgcolor"],
    "other_theme": pio.templates[chart_other_theme]["layout"]["paper_bgcolor"]
}