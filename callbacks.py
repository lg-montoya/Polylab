import numpy as np
from dash.dependencies import Input, Output, State, ALL
from dash import Patch
from defaults.cosmetics import  trace_colours
from defaults.dash_components import slider_max
from defaults.mathematics import derivative_notation, POLYNOMIALS, SINUSOIDALS
from factory import MyPolynomial


x_values = np.linspace(-slider_max, slider_max, 400)

def callback_wrapper(app):  

    # Update general form of equation based on dropdown
    @app.callback(
        Output("eq_1", "children"),
        Input("dropdown_menu_1", "value")
        )
    def display_general_polynomial_form(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]['general_form']
    
    # Update visibility and default slider values based on dropdown
    @app.callback(
        Output({"type": "polynomial_slider", "name": ALL}, "disabled"),
        Output({"type": "polynomial_slider", "name": ALL}, "value"),
        Input("dropdown_menu_1", "value"),
        prevent_initial_call=True
    )
    def update_slider_visibility(chosen_polynomial):
        available_sliders = [not i for i in POLYNOMIALS[chosen_polynomial]['available_sliders']]
        default_coefficient_values = POLYNOMIALS[chosen_polynomial]['default_coefficients']
        return available_sliders, default_coefficient_values
    
    # Update f(x) graph based on slider values.
    @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Input({"type": "polynomial_slider", "name": ALL}, "value"),
        )
    def update_graph_from_sliders(coefficients):
        
        patched_figure = Patch()
        
        y = MyPolynomial(coefficients)
        title = y.update_figure_title(*coefficients)
        d1y = y.derivative(order=1)
        d2y = y.derivative(order=2)
        
        y_values = y.evaluate(x_values)
        d1y_values = MyPolynomial(d1y.coef).evaluate(x_values)
        d2y_values = MyPolynomial(d2y.coef).evaluate(x_values)
        
        for i in range(3): 
            patched_figure['data'][i]['x'] = x_values
          
        patched_figure['data'][0]['y'] = y_values
        patched_figure['data'][1]['y'] = d1y_values    
        patched_figure['data'][2]['y'] = d2y_values
        
        patched_figure['data'][0]['name'] = fr"$y$"
        patched_figure['data'][1]['name'] = fr"${derivative_notation[1]}$"
        patched_figure['data'][2]['name'] = fr"${derivative_notation[2]}$"  
        
        patched_figure['layout']['title']['text'] = title.replace("0.0 + ", "")
      
        return patched_figure
    
   
    # Update derivative graphs based on slider values.
    def update_derivative_graph(order):
        @app.callback(
            Output(f"polynomial-graph-d{order}y", "figure", allow_duplicate=True),    
            Input({"type": "polynomial_slider", "name": ALL}, "value"),
            )
        def inner_function(coefficients):
            
            patched_figure = Patch()
            
            coeffs = MyPolynomial(coefficients).derivative(order=order).coef
            # Remove erronous precision in poly.deriv.
            coeffs = [round(i, 3) for i in coeffs]
            poly = MyPolynomial(coeffs)
            
            # Update the title
            terms = [f"{coeff}x^{i}" if i > 0 else f"{coeff}" for i, coeff in enumerate(coeffs)]
            derivative_str = " + ".join(terms).replace(" ","").replace("+0.0x^1","").replace("x^1","x").replace("+0.0x^2","")
            title = fr"${derivative_notation[order]}={derivative_str}$".replace("=0.0+", "=")
            
            patched_figure['data'][0]['x'] = x_values
            patched_figure['data'][0]['y'] = poly.evaluate(x_values)
            
            
            patched_figure['layout']['title']['text'] = title
            patched_figure["layout"]["showlegend"] = False
            
            # Always start on the default theme trace colour
            patched_figure['data'][0]['line']['color']=trace_colours['default_theme'][order]

            
            return patched_figure
        
    update_derivative_graph(1)
    update_derivative_graph(2)
    
    def modal_builder(name, link='lnk'):
        @app.callback(Output(f"mdl-{name}", "is_open"),
                    [Input(f"{link}-mdl-{name}-open", "n_clicks"),
                    Input(f"btn-mdl-{name}-close", "n_clicks")],
                    [State(f"mdl-{name}", "is_open")], )
        def function(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open
        
    modal_builder('instructions-polynomials', link='btn')
    # modal_builder('instructions-sinusoidals', link='btn')
    
    

    # # @app.callback(
    # #     Output('dynamic-sinusoidal', 'children'),
    # #     Input('dynamic-add-sinusoidal-btn', 'n_clicks'),
    # # )
    # # def add_sinusoidal(n_clicks):
    # #     patched_children=Patch()
        
    # #     dbc.Row(my_slider(id={'type': 'sinusoidal-dynamic-dropdown-a','index': n_clicks}, label="a"), className='mt-4'),
    # #     dbc.Row(my_slider(id={'type': 'sinusoidal-dynamic-dropdown-b','index': n_clicks}, label="b")),
    # #     dbc.Row(my_slider(id={'type': 'sinusoidal-dynamic-dropdown-c','index': n_clicks}, label="c")),
    # #     dbc.Row(my_slider(id={'type': 'sinusoidal-dynamic-dropdown-d','index': n_clicks}, label="d")),                       
        
    # #     return patched_children
