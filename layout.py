import dash_bootstrap_components as dbc
from dash import html
# from forms import color_mode_switch
from tabs import tab_0


def page_layout():
    layout = html.Div(children=[

            dbc.Container(fluid=True, children=[
                # html.Div(color_mode_switch, className="d-flex justify-content-end"),
                # html.Div(className="d-flex justify-content-end"),
                dbc.Tabs(id='tab-group', class_name='nav-stack',  children=[
                dbc.Tab(id='tab-0', label='Polynomials',
                        children=[tab_0], active_label_style={"color": "#FB79B3"}),
                # dbc.Tab(id='tab-1',  label='Other', disabled=False,
                        # children=[tab_1], active_label_style={"color": "#FB79B3"})
            ],)
        ], class_name="mt-2 dbc"),
    ])
    return layout