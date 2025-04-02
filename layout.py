import dash_bootstrap_components as dbc
from dash import html
from forms import fluid_mode_switch
from dash_bootstrap_templates import ThemeSwitchAIO
from tabs import introduction, polynomials, sinusoidals, linear_programming


def page_layout(default_theme, other_theme):
    layout = html.Div([
            dbc.Container(id='main-container', fluid=False, children=[
                html.Div(fluid_mode_switch, className="d-flex justify-content-end"),
                html.Div(
                    ThemeSwitchAIO(aio_id="theme", themes=[default_theme, other_theme], 
                                        icons={"left":"fa fa-sun me-1", "right":"fa fa-cloud-moon"}, 
                                        switch_props={"value":True}), className="d-flex justify-content-end"),
                
                dbc.Tabs([                  
                    dbc.Tab(id='tab-introduction', label='Introduction', children=[introduction.tab]),
                    dbc.Tab(id='tab-polynomials', label='Polynomials', children=[polynomials.tab]),
                    # dbc.Tab(id='tab-sinusoidals', label='Sinusoidals', children=[sinusoidals.tab]),
                ], id='tab-group', class_name='nav-stack')
        ], class_name="mt-3 dbc"),
    ])
    return layout