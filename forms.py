from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

# Gridlines radio-group
gridlines_radio = html.Div(  
        dcc.RadioItems(id='gridlines-radio', options=[
                {'label': html.Span([html.I(className="fa-solid fa-square ms-1 me-2")]), 'value': 'blank'},
                {'label': html.Span([html.I(className="fa fa-table-cells-large ms-1 me-2"), ""]), 'value': 'few_gridlines'},
                {'label': html.Span([html.I(className="fa fa-table-cells ms-1 me-1"), ""]), 'value': 'more_gridlines'}
                ],value='blank', inline=True, 
        ),
        style={
        "padding": "5px",  # Add padding around the radio items
        "borderRadius": "5px",  # Rounded corners
        "display": "inline-block"  # Ensures the container behaves like an inline element
    }
)

# Fluid toggle group
fluid_mode_switch = html.Span([
        dbc.Label(className="fa fa-mobile me-1", html_for="fluid-toggle"),
        dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-laptop", html_for="fluid-toggle"),
],style={"marginTop": "3px"})



# Theme toggle group
theme_mode_switch = html.Div([
        # dbc.Label(DashIconify(icon="emojione:unicorn-face", flip='horizontal', width=16, className='me-1', style={"marginBottom": "2px"}), html_for="theme-toggle"),
        dbc.Label(DashIconify(icon="fluent-emoji-flat:unicorn", flip='horizontal', width=17, className='me-1', style={"marginBottom": "2px"}), html_for="theme-toggle"),
        dbc.Switch(id="theme-toggle", value=True, className="d-inline-block", persistence=False),
        # dbc.Label(DashIconify(icon="mdi:ninja", width=18), html_for="theme-toggle"),
        dbc.Label(DashIconify(icon="fa6-solid:user-ninja", width=15, style={"marginBottom": "3px"}), html_for="theme-toggle"),
        # dbc.Label(DashIconify(icon="game-icons:ninja-heroic-stance", width=24, style={"marginBottom": "5px"}), html_for="theme-toggle"),
        # dbc.Label(DashIconify(icon="game-icons:ninja-head", width=18), html_for="theme-toggle"),
],style={"marginTop": "8px"})
