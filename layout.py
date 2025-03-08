import dash_bootstrap_components as dbc
from dash import html
from forms import color_mode_switch
from tabs import tab_0
from dash import dcc
from dash_bootstrap_templates import ThemeSwitchAIO


def page_layout(default_theme, other_theme):
    layout = html.Div(children=[
            dcc.Store(id='store-mypoly', storage_type='memory'),
            dbc.Container(fluid=True, children=[
                # html.Div(color_mode_switch, className="d-flex justify-content-end"),
                html.Div(ThemeSwitchAIO(aio_id="theme", themes=[default_theme, other_theme]), className="d-flex justify-content-end"),
                # html.Div(theme_switch, className="d-flex justify-content-end"),
                # html.Div(className="d-flex justify-content-end"),
                dbc.Tabs(id='tab-group', class_name='nav-stack',  children=[
                dbc.Tab(id='tab-0', label='Polynomials',
                        # children=[tab_0], active_label_style={"color": "#FB79B3"}),
                        children=[tab_0]),
                dbc.Tab(id='tab-1',  label='Other', disabled=False,
                        # active_label_style={"color": "#FB79B3"})
                        )
                        
            ],)
        ], class_name="mt-2 dbc"),
    ])
    return layout