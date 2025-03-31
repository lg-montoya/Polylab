import dash_bootstrap_components as dbc
from dash import html
from forms import color_mode_switch
from tabs import tab_1, tab_2, tab_0, tab_3
from dash import dcc
from dash_bootstrap_templates import ThemeSwitchAIO


def page_layout(default_theme, other_theme):
    layout = html.Div(children=[
            dcc.Store(id='store-mypoly', storage_type='memory'),
            dbc.Container(fluid=False, children=[
                # html.Div(color_mode_switch, className="d-flex justify-content-end"),
                html.Div(ThemeSwitchAIO(aio_id="theme", themes=[default_theme, other_theme], 
                                        icons={"left":"fa fa-sun", "right":"fa fa-cloud-moon"}, 
                                        switch_props={"value":True}), className="d-flex justify-content-end"),
                dbc.Tabs(id='tab-group', class_name='nav-stack',  children=[
                    
                    dbc.Tab(id='tab-0', label='Introduction', children=[tab_0]),
                    dbc.Tab(id='tab-1', label='Polynomials', children=[tab_1]),
                    dbc.Tab(id='tab-2',  label='Sinusoidals', children=[tab_2]),
                    # dbc.Tab(id='tab-3',  label='Regions', children=[tab_3]),
                    # dbc.Tab(id='tab-4',  label='Integration', children=[tab_3]),
                    
                        
            ],)
        ], class_name="mt-2 dbc"),
    ])
    return layout