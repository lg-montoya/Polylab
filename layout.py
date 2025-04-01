import dash_bootstrap_components as dbc
from dash import html
from forms import color_mode_switch
from dash import dcc
from dash_bootstrap_templates import ThemeSwitchAIO

from tabs import instructions, polynomials, sinusoidals, linear_programming


def page_layout(default_theme, other_theme):
    layout = html.Div(children=[
            dcc.Store(id='store-mypoly', storage_type='memory'),
            dbc.Container(fluid=False, children=[
                # html.Div(color_mode_switch, className="d-flex justify-content-end"),
                html.Div(ThemeSwitchAIO(aio_id="theme", themes=[default_theme, other_theme], 
                                        icons={"left":"fa fa-sun", "right":"fa fa-cloud-moon"}, 
                                        switch_props={"value":True}), className="d-flex justify-content-end"),
                dbc.Tabs(id='tab-group', class_name='nav-stack',  children=[
                    
                    dbc.Tab(id='tab-instruction', label='Introduction', children=[instructions.tab]),
                    dbc.Tab(id='tab-polynomials', label='Polynomials', children=[polynomials.tab]),
                    # dbc.Tab(id='tab-sinusoidals',  label='Sinusoidals', children=[sinusoidals.tab]),
                    # dbc.Tab(id='tab-linear-programming',  label='Linear Programming', children=[linear_programming.tab]),
                    
            ],)
        ], class_name="mt-2 dbc"),
    ])
    return layout