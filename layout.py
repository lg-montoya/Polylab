import dash_bootstrap_components as dbc
from dash import html
from forms import fluid_mode_switch
from dash_bootstrap_templates import ThemeSwitchAIO
from tabs import introduction, polynomials, sinusoidals, linear_programming


def app_layout(default_theme, other_theme):
    
    theme_switch = ThemeSwitchAIO(
        aio_id = "theme", 
        themes = [default_theme, other_theme], 
        icons = {"left":"fa fa-sun me-1", "right":"fa fa-cloud-moon"}, 
        switch_props = {"value":True}
        )
    
    layout = html.Div([
        dbc.Container(
            children=[
                # html.Div([fluid_mode_switch, theme_switch], className="d-flex justify-content-end"),
                
                html.Div(fluid_mode_switch, className="d-flex justify-content-end"), 
                html.Div(theme_switch, className="d-flex justify-content-end"), 
 
                dbc.Tabs([                  
                    dbc.Tab(introduction.tab, id='tab-introduction', label='Introduction'),
                    dbc.Tab(polynomials.tab, id='tab-polynomials', label='Polynomials'),
                    # dbc.Tab(id='tab-sinusoidals', label='Sinusoidals', children=[sinusoidals.tab]),
                ], id='tab-group', class_name='nav-stack')
                
            ], id='main-container', fluid=False, class_name="mt-3 dbc"
        )
    ])
    
    return layout


