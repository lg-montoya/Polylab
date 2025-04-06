import dash_bootstrap_components as dbc
from dash import html, dcc
from forms import fluid_mode_switch, gridlines_switch, gridlines_radio
from dash_bootstrap_templates import ThemeSwitchAIO
from tabs import introduction, polynomials, sinusoidals, linear_programming


def app_layout(default_theme, other_theme):
    
    theme_switch = ThemeSwitchAIO(
        aio_id = "theme", 
        themes = [default_theme, other_theme], 
        icons = {"left":"fa fa-sun", "right":"fa fa-cloud-moon"}, 
        switch_props = {"value":True}
        )
    
    layout = html.Div([
        dbc.Container(
            children=[
                # html.Div([gridlines_switch, fluid_mode_switch, theme_switch], className="d-flex justify-content-end align-items-center gap-4"),
                            
                html.Div([
                    dbc.Card([
                        dbc.Container([
                            gridlines_radio,
                            # gridlines_switch, 
                            fluid_mode_switch, 
                            theme_switch
                        ], className="d-flex flex-row flex-nowrap align-items-center gap-3 mt-1")
                    ]), 
                ], className="d-flex justify-content-end mb-2"),
                
                dbc.Tabs([                  
                    dbc.Tab(polynomials.tab, id='tab-polynomials', label='Polynomials'),
                    dbc.Tab(introduction.tab, id='tab-introduction', label='Introduction'),
                    # dbc.Tab(id='tab-sinusoidals', label='Sinusoidals', children=[sinusoidals.tab]),
                ], id='tab-group', class_name='nav-stack')
                
            ], id='main-container', fluid=False, class_name="mt-3 dbc"
        )
    ])
    
    return layout


