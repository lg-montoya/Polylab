from dash.dependencies import Input, Output, State
from dash import Patch
import plotly.io as pio
from defaults import POLYNOMIALS, derivative_notation
from factory import MyPolynomial, plot_axes


def callback_wrapper(app):    

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
        allow_duplicate=True  # Allow duplicate callback
    )
    def update_graph(selected_polynomial):
        # Return an empty figure if no polynomial is selected
        if selected_polynomial is None:
            return Patch()  

        coefficients = POLYNOMIALS[selected_polynomial]['default_coefficients']
        my_polynomial = MyPolynomial(coefficients)
        fig = plot_axes()  # Start with the axes

        # Add the polynomial trace
        poly_trace = my_polynomial.plot().data[0]
        fig.add_trace(poly_trace)

        return fig, *coefficients
    

    # Callback updating f(x) graph based on the slider values
    @app.callback(
        Output("tab-0-graph-y", "figure", allow_duplicate=True),
        Input("slider_1_a", "value"),
        Input("slider_1_b", "value"),
        Input("slider_1_c", "value"),
        Input("slider_1_d", "value"),
    )
    def update_graph_from_sliders(a, b, c, d):
        coefficients = [a, b, c, d]
        my_polynomial = MyPolynomial(coefficients)
        first_derivative = my_polynomial.derivative(order=1)
        second_derivative = my_polynomial.derivative(order=2)
        
        fig = plot_axes()  # Start with the axes

        # Add the polynomial trace
        poly_trace = my_polynomial.plot().data[0]
        poly_trace.update(name=fr"$y$")
        fig.add_trace(poly_trace)
        
        # # Add the first-order derivative trace
        first_derivative_trace = MyPolynomial(first_derivative.coef).plot().data[0]
        first_derivative_trace.update(name=fr"${derivative_notation[1]}$", line=dict(color='blue'))
        fig.add_trace(first_derivative_trace)
        
        # Add the second-order derivative trace
        second_derivative_trace = MyPolynomial(second_derivative.coef).plot().data[0]
        second_derivative_trace.update(name=fr"${derivative_notation[2]}$", line=dict(color='red'))
        fig.add_trace(second_derivative_trace)
        
        # Update the title
        title = my_polynomial.update_figure_title(*coefficients)
        fig.update_layout(
            title={
                "text": title.replace("0.0 + ", ""),
                "x": 0.5,  # Center the title
                "xanchor": "center",
                "yanchor": "top"
            },
            title_font_size=20
            )
        fig.update_layout(showlegend=True),        
        return fig
    
    
    def update_derivative_graph(order, color):
        @app.callback(
            Output(f"tab-0-graph-d{order}y", "figure", allow_duplicate=True),
            Input("slider_1_a", "value"),
            Input("slider_1_b", "value"),
            Input("slider_1_c", "value"),
            Input("slider_1_d", "value"),
        )
        def update_graph_from_sliders(a, b, c, d):
            coefficients = [a, b, c, d]
            coeffs = MyPolynomial(coefficients).derivative(order=order).coef
            poly = MyPolynomial(coeffs)
            fig = plot_axes()  # Start with the axes

            # Add the polynomial trace
            poly_trace = poly.plot().data[0]
            
            poly_trace.update(name=f"Derivative Order {order}", line=dict(color=color))
            
            fig.add_trace(poly_trace)
            
            # Update the title
            terms = [f"{coeff}x^{i}" if i > 0 else f"{coeff}" for i, coeff in enumerate(coeffs)]
            derivative_str = " + ".join(terms).replace(" ","").replace("+0.0x^1","").replace("x^1","x").replace("+0.0x^2","")
            title = fr"${derivative_notation[order]}={derivative_str}$".replace("=0.0+", "=")
            
            fig.update_layout(
                title={
                    "text": title,
                    "x": 0.5,  # Center the title
                    "xanchor": "center",
                    "yanchor": "top"
                },
                title_font_size=20
            )
            
            return fig

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
    
 



    