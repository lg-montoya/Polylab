import numpy as np
import plotly.io as pio
from dash.dependencies import Input, Output, State
from dash_bootstrap_templates import ThemeSwitchAIO
from dash import Patch, callback_context, no_update
from defaults import POLYNOMIALS, derivative_notation
from factory import MyPolynomial

x_values = np.linspace(-10, 10, 400)


def callback_wrapper(app, default_chart_theme, other_chart_theme):    

    # Callback for updating availability of sliders.
    @app.callback(
        Output("slider_1_a", "disabled"),
        Output("slider_1_b", "disabled"),
        Output("slider_1_c", "disabled"),
        Output("slider_1_d", "disabled"),
        Input("dropdown_menu_1", "value"),
    )
    def update_slider_status(chosen_polynomial):
        return [not i for i in POLYNOMIALS[chosen_polynomial]['available_sliders']]
    

    # Callback for updating general formula of the chosen polynomial.
    @app.callback(
        Output("eq_1", "children"),
        Input("dropdown_menu_1", "value"),
    )
    def update_general_formula(chosen_polynomial):
        return POLYNOMIALS[chosen_polynomial]['general_form'] 
    
    
    # Callback for adding the default polynomial to the graph according to the chosen polynomial type.
    @app.callback(
        Output("tab-0-graph-y", "figure", allow_duplicate=True),
        Output("slider_1_a", "value"),
        Output("slider_1_b", "value"),
        Output("slider_1_c", "value"),
        Output("slider_1_d", "value"),
        Input("dropdown_menu_1", "value"),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        allow_duplicate=True
    )
    def set_default_graphs(selected_polynomial, theme_toggle):
        
        ctx = callback_context
        if type(ctx.triggered[0]['value']) == bool:
            patched_figure = Patch()
            template = pio.templates[default_chart_theme]  if theme_toggle else pio.templates[other_chart_theme]
            patched_figure["layout"]["template"] = template
            return patched_figure, no_update, no_update, no_update, no_update
        

  

        coefficients = POLYNOMIALS[selected_polynomial]['default_coefficients']
        my_polynomial = MyPolynomial(coefficients)
        y_values = my_polynomial.evaluate(x_values)
        
        patched_figure = Patch()
        patched_figure['data'][0]['y'] = y_values
        

        return patched_figure, *coefficients
    

    # Callback updating f(x) graph based on the slider values
    @app.callback(
        Output("tab-0-graph-y", "figure", allow_duplicate=True),
        Input("slider_1_a", "value"),
        Input("slider_1_b", "value"),
        Input("slider_1_c", "value"),
        Input("slider_1_d", "value"),
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        allow_duplicate=True
    )
    def update_graph_from_sliders(a, b, c, d, theme_toggle):
        
        ctx = callback_context
        if type(ctx.triggered[0]['value']) == bool:
            patched_figure = Patch()
            template = pio.templates[default_chart_theme]  if theme_toggle else pio.templates[other_chart_theme]
            patched_figure["layout"]["template"] = template
            return patched_figure
        
        
        coefficients = [a, b, c, d]
        y = MyPolynomial(coefficients)
        title = y.update_figure_title(*coefficients)
        d1y = y.derivative(order=1)
        d2y = y.derivative(order=2)
        
        y_values = y.evaluate(x_values)
        d1y_values = MyPolynomial(d1y.coef).evaluate(x_values)
        d2y_values = MyPolynomial(d2y.coef).evaluate(x_values)
        
        
        patched_figure = Patch()
        
        patched_figure['data'][0]['x'] = x_values
        patched_figure['data'][1]['x'] = x_values    
        patched_figure['data'][2]['x'] = x_values    
        
        patched_figure['data'][0]['y'] = y_values
        patched_figure['data'][1]['y'] = d1y_values    
        patched_figure['data'][2]['y'] = d2y_values
        
        patched_figure['data'][0]['name'] = fr"$y$"
        patched_figure['data'][1]['name'] = fr"${derivative_notation[1]}$"
        patched_figure['data'][2]['name'] = fr"${derivative_notation[2]}$"  
        
        patched_figure['layout']['title']['text'] = title.replace("0.0 + ", "")
        patched_figure['layout']['title']['x'] = 0.5
        patched_figure['layout']['title']['xanchor'] = "center"
        patched_figure['layout']['title']['yanchor'] = "top"
        patched_figure['layout']['title_font_size'] = 20
      
        return patched_figure
    
    
    def update_derivative_graph(order, color):
        @app.callback(
            Output(f"tab-0-graph-d{order}y", "figure", allow_duplicate=True),
            Input("slider_1_a", "value"),
            Input("slider_1_b", "value"),
            Input("slider_1_c", "value"),
            Input("slider_1_d", "value"),
            Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
            allow_duplicate=True
        )
        def update_graph_from_sliders(a, b, c, d, theme_toggle):
            
            ctx = callback_context
            if type(ctx.triggered[0]['value']) == bool:
                patched_figure = Patch()
                template = pio.templates[default_chart_theme]  if theme_toggle else pio.templates[other_chart_theme]
                patched_figure["layout"]["template"] = template
                return patched_figure
            
            coefficients = [a, b, c, d]
            coeffs = MyPolynomial(coefficients).derivative(order=order).coef
            poly = MyPolynomial(coeffs)
            
            # Update the title
            terms = [f"{coeff}x^{i}" if i > 0 else f"{coeff}" for i, coeff in enumerate(coeffs)]
            derivative_str = " + ".join(terms).replace(" ","").replace("+0.0x^1","").replace("x^1","x").replace("+0.0x^2","")
            title = fr"${derivative_notation[order]}={derivative_str}$".replace("=0.0+", "=")
            
            patched_figure = Patch()
            
            patched_figure['data'][0]['x'] = x_values
            patched_figure['data'][0]['y'] = poly.evaluate(x_values)
            patched_figure['data'][0]['name'] = f"Derivative Order {order}"
            patched_figure['data'][0]['line']['color'] = color
            
            patched_figure['layout']['title']['text'] = title
            patched_figure['layout']['title']['x'] = 0.5
            patched_figure['layout']['title']['xanchor'] = "center"
            patched_figure['layout']['title']['yanchor'] = "top"
            patched_figure['layout']['title_font_size'] = 20
            
            return patched_figure
        

    update_derivative_graph(1,"blue")
    update_derivative_graph(2,"red")
    
    def modal_builder(name, link='lnk'):
        @app.callback(Output(f"mdl-{name}", "is_open"),
                    [Input(f"{link}-mdl-{name}-o", "n_clicks"),
                    Input(f"btn-mdl-{name}-q", "n_clicks")],
                    [State(f"mdl-{name}", "is_open")], )
        def function(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open
        
    modal_builder('instructions', link='btn')
    
 



    