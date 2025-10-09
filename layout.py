import dash_bootstrap_components as dbc
from dash import html, dcc
from forms import fluid_mode_switch, gridlines_radio, theme_mode_switch
from dash_bootstrap_templates import ThemeSwitchAIO
from tabs import hyperbolae, introduction, polynomials, linear_programming
from modals import MODAL_GRIDLINES
from defaults.cosmetics import graph_background_colours, APP_THEMES


DEFAULT_THEME = "default_theme"


def app_layout(app_themes):
    theme_switch = html.Span(
        ThemeSwitchAIO(
            aio_id="theme",
            themes=list(app_themes.values()),
            icons={"left": "fa fa-sun", "right": "fa fa-cloud-moon"},
            switch_props={"value": True},
        ),
        className="theme-switch-container",
        style={"marginTop": "3px"},
    )

    layout = html.Div(
        [
            # App-wide variable for grid-lines granularity setting
            dcc.Store(id="gridlines", storage_type="memory"),
            # App-wide variable for current App theme setting
            dcc.Store(id="theme-store", data=DEFAULT_THEME, storage_type="local"),
            # Link to dynamically update the stylesheet
            html.Link(
                id="theme-link", rel="stylesheet", href=APP_THEMES[DEFAULT_THEME]
            ),
            # dbc wrapper for the app.
            dbc.Container(
                children=[
                    # ROW containing app controls
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                children=[
                                    gridlines_radio,
                                    fluid_mode_switch,
                                    theme_mode_switch,
                                ],
                                # children=[gridlines_radio, fluid_mode_switch, theme_switch],
                                className="d-flex flex-row align-items-center gap-2 mb-2",
                                style={
                                    "border": "1px solid var(--bs-primary)",
                                    "borderRadius": "6px",
                                    "overflow": "hidden",
                                    "background": graph_background_colours[
                                        "default_theme"
                                    ],
                                    "padding": "0.5rem",
                                    "margin": "0rem",
                                },
                                id="app-controls-div",
                            ),
                            className="d-flex justify-content-center justify-content-sm-end",
                            style={"padding": "0rem 0.5rem"},
                        )
                    ),
                    # ROW containing the tabs
                    dbc.Tabs(
                        [
                            dbc.Tab(
                                introduction.tab,
                                tab_id="tab-introduction",
                                label="Introduction",
                            ),
                            dbc.Tab(
                                polynomials.tab,
                                tab_id="tab-polynomials",
                                label="Polynomials",
                            ),
                            dbc.Tab(
                                hyperbolae.tab,
                                tab_id='tab-hyperbolae', 
                                label='Hyperbolae', ),
                        ],
                        id="tab-group",
                        class_name="nav-stack",
                        active_tab="tab-polynomials",
                    ),
                    MODAL_GRIDLINES,
                ],
                id="main-container",
                fluid=False,
                class_name="mt-3 dbc",
            ),
        ]
    )

    return layout
