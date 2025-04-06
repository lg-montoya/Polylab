from dash import html, dcc
import dash_bootstrap_components as dbc

gridlines_radio = html.Div(  
        dcc.RadioItems(id='gridlines-radio', options=[
                {'label': html.Span([html.I(className="fa-solid fa-square ms-1 me-2")]), 'value': 'blank'},
                {'label': html.Span([html.I(className="fa fa-table-cells-large ms-1 me-2"), ""]), 'value': 'few_gridlines'},
                {'label': html.Span([html.I(className="fa fa-table-cells ms-1 me-1"), ""]), 'value': 'more_gridlines'}
                ],value='few_gridlines', inline=True, 
        ),
        style={
        "padding": "5px",  # Add padding around the radio items
        "borderRadius": "5px",  # Rounded corners
        "display": "inline-block"  # Ensures the container behaves like an inline element
    }, className='ml-1 mt-0 mb-1'
)

fluid_mode_switch = html.Span([
        dbc.Label(className="fa fa-mobile me-1", html_for="fluid-toggle"),
        dbc.Switch(id="fluid-toggle", value=True, className="d-inline-block", persistence=False),
        dbc.Label(className="fa fa-laptop", html_for="fluid-toggle"),
])

