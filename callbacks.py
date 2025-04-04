import numpy as np
import plotly.io as pio
from dash.dependencies import Input, Output, State, ALL
from dash_bootstrap_templates import ThemeSwitchAIO
from dash import Patch
from defaults.cosmetics import  trace_colours
from defaults.dash_components import slider_max
from defaults.mathematics import derivative_notation, POLYNOMIALS, SINUSOIDALS
from factory import MyPolynomial


x_values = np.linspace(-slider_max, slider_max, 400)

def callback_wrapper(app, default_chart_theme, other_chart_theme):  

    @app.callback(
        Output("eq_1", "children"),
        Input("dropdown_menu_1", "value")
        )
    def display_general_polynomial_form(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]['general_form']
    
    
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
        
    
    # Update trace theme.
    @app.callback(
        Output("polynomial-graph-y", "figure", allow_duplicate=True),
        Output(f"polynomial-graph-d1y", "figure", allow_duplicate=True),
        Output(f"polynomial-graph-d2y", "figure", allow_duplicate=True),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    )
    def update_graph_from_sliders(is_dark):
        patch_figure = Patch()
        patched_figures = [Patch() for _ in range(2)]

        patch_figure["layout"]["template"] = (pio.templates[default_chart_theme] 
                                              if is_dark else pio.templates[other_chart_theme])    
         
        i=1
        if is_dark:
            for figure in patched_figures:
                figure["layout"]["template"] = pio.templates[default_chart_theme]
                figure['data'][0]['line']['color']=trace_colours['default_theme'][i]
                i+=1
        else:
            for figure in patched_figures:
                figure["layout"]["template"] = pio.templates[other_chart_theme]
                figure['data'][0]['line']['color']=trace_colours['other_theme'][i]
                i+=1 
            
        return patch_figure, *patched_figures
    
    
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
    
    @app.callback(
        Output("main-container", "fluid"),
        Input("fluid-toggle", "value")
    )
    def toggle_fluid_mode(is_fluid):
        return not is_fluid

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





#----------------------------



    # # Callback updating f(x) graph based on slider values.
    # @app.callback(
    #     Output("polynomial-graph-y", "figure", allow_duplicate=True),
    #     Input("polynomial_slider_a", "value"),
    #     Input("polynomial_slider_b", "value"),
    #     Input("polynomial_slider_c", "value"),
    #     Input("polynomial_slider_d", "value"),
    #     Input(ThemeSwitchAIO.ids.switch("theme"), "value"))
    # def update_graph_from_sliders(a, b, c, d, is_dark):
        
    #     ctx = callback_context
    #     patched_figure = Patch()
        
    #     if type(ctx.triggered[0]['value']) == bool:
    #         template = pio.templates[default_chart_theme]  if is_dark else pio.templates[other_chart_theme]
    #         patched_figure["layout"]["template"] = template
    #         return patched_figure
        
    #     coefficients = [a, b, c, d]
    #     y = MyPolynomial(coefficients)
    #     title = y.update_figure_title(*coefficients)
    #     d1y = y.derivative(order=1)
    #     d2y = y.derivative(order=2)
        
    #     y_values = y.evaluate(x_values)
    #     d1y_values = MyPolynomial(d1y.coef).evaluate(x_values)
    #     d2y_values = MyPolynomial(d2y.coef).evaluate(x_values)
        
    #     patched_figure['data'][0]['x'] = x_values
    #     patched_figure['data'][1]['x'] = x_values    
    #     patched_figure['data'][2]['x'] = x_values    
        
    #     patched_figure['data'][0]['y'] = y_values
    #     patched_figure['data'][1]['y'] = d1y_values    
    #     patched_figure['data'][2]['y'] = d2y_values
        
    #     patched_figure['data'][0]['name'] = fr"$y$"
    #     patched_figure['data'][1]['name'] = fr"${derivative_notation[1]}$"
    #     patched_figure['data'][2]['name'] = fr"${derivative_notation[2]}$"  
        
    #     patched_figure['layout']['title']['text'] = title.replace("0.0 + ", "")
      
    #     return patched_figure
    
        # # Callback setting sliders' visibility.
    # @app.callback(
    #     Output("polynomial_slider_a", "disabled"),
    #     Output("polynomial_slider_b", "disabled"),
    #     Output("polynomial_slider_c", "disabled"),
    #     Output("polynomial_slider_d", "disabled"),
    #     Input("dropdown_menu_1", "value"))
    # def set_slider_visibility(chosen_polynomial):
    #     available_sliders = [not i for i in POLYNOMIALS[chosen_polynomial]['available_sliders']]
    #     # return general_form, *available_sliders
    #     return available_sliders
    
    
     # Callback initialising slider values.
    # @app.callback(
    #     Output("polynomial_slider_a", "value"),
    #     Output("polynomial_slider_b", "value"),
    #     Output("polynomial_slider_c", "value"),
    #     Output("polynomial_slider_d", "value"),
    #     Input("dropdown_menu_1", "value"))
    # def set_default_graphs(chosen_polynomial):
    #     return POLYNOMIALS[chosen_polynomial]['default_coefficients']
    
        # # Callback updating f(x) graph based on slider values.
    # @app.callback(
    #     Output("polynomial-graph-y", "figure", allow_duplicate=True),
    #     Input("polynomial_slider_a", "value"),
    #     Input("polynomial_slider_b", "value"),
    #     Input("polynomial_slider_c", "value"),
    #     Input("polynomial_slider_d", "value"),
    #     Input(ThemeSwitchAIO.ids.switch("theme"), "value"))
    # def update_graph_from_sliders(a, b, c, d, is_dark):
        
    #     ctx = callback_context
    #     patched_figure = Patch()
        
    #     if type(ctx.triggered[0]['value']) == bool:
    #         template = pio.templates[default_chart_theme]  if is_dark else pio.templates[other_chart_theme]
    #         patched_figure["layout"]["template"] = template
    #         return patched_figure
        
    #     coefficients = [a, b, c, d]
    #     y = MyPolynomial(coefficients)
    #     title = y.update_figure_title(*coefficients)
    #     d1y = y.derivative(order=1)
    #     d2y = y.derivative(order=2)
        
    #     y_values = y.evaluate(x_values)
    #     d1y_values = MyPolynomial(d1y.coef).evaluate(x_values)
    #     d2y_values = MyPolynomial(d2y.coef).evaluate(x_values)
        
    #     patched_figure['data'][0]['x'] = x_values
    #     patched_figure['data'][1]['x'] = x_values    
    #     patched_figure['data'][2]['x'] = x_values    
        
    #     patched_figure['data'][0]['y'] = y_values
    #     patched_figure['data'][1]['y'] = d1y_values    
    #     patched_figure['data'][2]['y'] = d2y_values
        
    #     patched_figure['data'][0]['name'] = fr"$y$"
    #     patched_figure['data'][1]['name'] = fr"${derivative_notation[1]}$"
    #     patched_figure['data'][2]['name'] = fr"${derivative_notation[2]}$"  
        
    #     patched_figure['layout']['title']['text'] = title.replace("0.0 + ", "")
      
    #     return patched_figure
    
    
        # def update_derivative_graph(order):
    #     @app.callback(
    #         Output(f"polynomial-graph-d{order}y", "figure", allow_duplicate=True),
    #         Input("polynomial_slider_a", "value"),
    #         Input("polynomial_slider_b", "value"),
    #         Input("polynomial_slider_c", "value"),
    #         Input("polynomial_slider_d", "value"),
    #         Input(ThemeSwitchAIO.ids.switch("theme"), "value"))
    #     def inner_function(a, b, c, d, is_dark):
    #         ctx = callback_context
    #         patched_figure = Patch()
            
    #         if type(ctx.triggered[0]['value']) == bool:
    #             if is_dark:
    #                 template = pio.templates[default_chart_theme]
    #                 patched_figure['data'][0]['line']['color'] = trace_colours['default_theme'][order]
    #             else:
    #                 template = pio.templates[other_chart_theme]
    #                 patched_figure['data'][0]['line']['color'] = trace_colours['other_theme'][order]
                    
    #             patched_figure["layout"]["template"] = template
    #             return patched_figure
            
            
    #         coefficients = [a, b, c, d]
    #         coeffs = MyPolynomial(coefficients).derivative(order=order).coef
    #         poly = MyPolynomial(coeffs)
            
    #         # Update the title
    #         terms = [f"{coeff}x^{i}" if i > 0 else f"{coeff}" for i, coeff in enumerate(coeffs)]
    #         derivative_str = " + ".join(terms).replace(" ","").replace("+0.0x^1","").replace("x^1","x").replace("+0.0x^2","")
    #         title = fr"${derivative_notation[order]}={derivative_str}$".replace("=0.0+", "=")
            
            
    #         patched_figure['data'][0]['x'] = x_values
    #         patched_figure['data'][0]['y'] = poly.evaluate(x_values)
            
    #         if is_dark:
    #             patched_figure['data'][0]['line']['color']=trace_colours['default_theme'][order]
    #         else:
    #             patched_figure['data'][0]['line']['color']=trace_colours['other_theme'][order]
            
    #         patched_figure['layout']['title']['text'] = title
    #         patched_figure["layout"]["showlegend"] = False

            
    #         return patched_figure