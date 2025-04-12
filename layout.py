import dash_bootstrap_components as dbc
from dash import html, dcc
from forms import fluid_mode_switch, gridlines_radio
from dash_bootstrap_templates import ThemeSwitchAIO
from tabs import introduction, polynomials, sinusoidals, linear_programming
from modals import modal_gridlines
from defaults.cosmetics import graph_background_colours

def app_layout(default_theme, other_theme):
    
    theme_switch = html.Span(ThemeSwitchAIO(
        aio_id = "theme", 
        themes = [default_theme, other_theme], 
        icons = {"left":"fa fa-sun", "right":"fa fa-cloud-moon"}, 
        switch_props = {"value":True},
        ),
        style={"marginTop": "3px"}
    )
    
    layout = html.Div([
        dcc.Store(id='gridlines', storage_type='memory'),
        dbc.Container(
            children=[    
                # ROW containing app controls    
                dbc.Row(
                    dbc.Col( 
                        html.Div(
                            children=[gridlines_radio, fluid_mode_switch, theme_switch],
                            className="d-flex flex-row align-items-center gap-2 mb-2",
                            style={        
                                "border": "1px solid var(--bs-primary)",
                                "borderRadius": "6px", 
                                "overflow": "hidden",
                                "background": graph_background_colours["default_theme"],
                                "padding": "0rem 0.5rem"
                            },
                            id="app-controls-div"
                        ),
                        className="d-flex justify-content-center justify-content-sm-end"       
                        )
                ),           
                # ROW containing the tabs
                dbc.Tabs([                  
                    dbc.Tab(introduction.tab, tab_id='tab-introduction', label='Introduction'),
                    dbc.Tab(polynomials.tab, tab_id='tab-polynomials', label='Polynomials'),
                    # dbc.Tab(tab_id='tab-sinusoidals', label='Sinusoidals', children=[sinusoidals.tab]),
                ], id='tab-group', class_name='nav-stack', active_tab='tab-polynomials'),
                
                modal_gridlines
                
            ], id='main-container', fluid=False, class_name="mt-3 dbc"
        )
    ])
    
    return layout


