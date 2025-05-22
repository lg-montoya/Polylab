import dash_bootstrap_components as dbc
from dash import html, dcc
from defaults.dash_components import slider_default, dropdown_polynomial_options
# BELOW import is for figure_template loading
from defaults.cosmetics import graph_background_colours
from modals import MODAL_POLYNOMIAL_INSTRUCTIONS
from factory import my_slider, graph_generator
from defaults.cosmetics import STYLE_GRAPH_BORDER


axis = dict(range=[slider_default["min"], slider_default["max"]], zeroline=True)
flex_column_style = {'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'}

tab = html.Div([
            # ROW with just the instructions button
            dbc.Row([
                dbc.Col([
                    html.Div(    
                        dbc.Button("Instructions", color="primary", outline=False,id='btn-mdl-instructions-polynomials-open'),
                        className="d-grid"
                    )
                ],class_name='mb-2', sm=2)
            ]),
            
            # 1st ROW of controls and y=f(x) graph.
            dbc.Row([
                # First column containing just controls
                dbc.Col([
                    dbc.Stack([
                        
                        # Dropdown menu
                        html.Div(dcc.Dropdown(id='dropdown_menu_1', options=dropdown_polynomial_options, 
                                            clearable=False, placeholder='CHOOSE A POLYNOMIAL'), className="d-grid"),
                        
                        # General form of the polynomial in LaTeX
                        html.Div(
                            dcc.Markdown("&nbsp;", mathjax=True, id='eq_1'), 
                            style={"textAlign": "center"}, className='mt-3'
                        ),
                        
                        # Sliders
                        html.Div([
                            dbc.Row(my_slider({"type": "polynomial_slider", "name": f"{i}"}, f"{i}")) 
                            for i in ['a', 'b', 'c', 'd']
                            ],        
                            style={
                                **STYLE_GRAPH_BORDER,
                                "background": graph_background_colours["default_theme"],
                                },
                            id="slider_div"                        
                        )
                    ], style=flex_column_style),
            ], style=flex_column_style, sm=4),

                # Second column containing just the graph y=f(x)
                graph_generator(id='polynomial-graph-y', class_name="mt-sm-2-custom"),
        ]),
            
            # 2nd ROW containing y=f'(x) graph
            dbc.Row(      
                graph_generator(id='polynomial-graph-d1y', class_name="mt-2 ms-auto")
            ),
            
            # 3rd ROW containing y=f''(x) graph
            dbc.Row(
                graph_generator(id='polynomial-graph-d2y', class_name="mt-2 ms-auto")  
            ),
            
            MODAL_POLYNOMIAL_INSTRUCTIONS

], className="mt-4")