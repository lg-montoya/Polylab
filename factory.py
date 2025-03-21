import plotly.graph_objs as go
import numpy as np
import plotly.io as pio
from dash import dcc
from defaults import slider_max


x_values = np.linspace(-slider_max, slider_max, 400)


class PolynomialGraph:
    def __init__(self, coefficients):
        self.graph = go.Figure()
        self.coefficients = coefficients
        self.polynomial_y = None
        self.polynomial_dy = None
        self.polynomial_d2y = None
   
        
    def set_polynomial_y(self):
        self.polynomial_y = np.polynomial.Polynomial(self.coefficients)
        return self
    
    def set_polynomial_d1y(self):
        self.polynomial_dy = self.polynomial_y.deriv(m=1)
        return self
    
    def set_polynomial_d2y(self):
        self.polynomial_d2y = self.polynomial_y.deriv(m=2)
        return self
    
    def update_polynomials(self, coefficients):
        self.polynomial_y.coef = coefficients
        self.set_polynomial_d1y()
        self.set_polynomial_d2y()
        return self
    
    def evaluate_polynomials(self):
        return self.polynomial_y(x_values), self.polynomial_dy(x_values), self.polynomial_d2y(x_values)



class MyPolynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.poly = np.polynomial.Polynomial(coefficients)  # Create a NumPy polynomial object

    def evaluate(self, x):
        return self.poly(x)    
    
    def derivative(self, order=1):
        return self.poly.deriv(m=order)


    
    def update_figure_title(self, a, b, c, d):
        # Rule 1: When all coefficients are zero, return f(x) = 0
        if a == 0 and b == 0 and c == 0 and d == 0:
            return r"$y=0$"

        # Initialize the list for polynomial terms
        terms = []

        # Rule 2 and 3: Add terms only if their coefficients are non-zero and follow sign rules
        if a != 0:
            terms.append(f"{a}")

        if b != 0:
            if b == 1:
                terms.append(f"+x")  # Only sign and variable
            elif b == -1:
                terms.append(f"-x")  # Only sign and variable
            else:
                terms.append(f"{'+' if b > 0 else ''}{b}x")

        if c != 0:
            if c == 1:
                terms.append(f"+x^2")  # Only sign and variable
            elif c == -1:
                terms.append(f"-x^2")  # Only sign and variable
            else:
                terms.append(f"{'+' if c > 0 else ''}{c}x^2")

        if d != 0:
            if d == 1:
                terms.append(f"+x^3")  # Only sign and variable
            elif d == -1:
                terms.append(f"-x^3")  # Only sign and variable
            else:
                terms.append(f"{'+' if d > 0 else ''}{d}x^3")

        # Rule 3: If only one term exists, include its sign only if negative
        if len(terms) == 1 and terms[0][0] != '-':
            terms[0] = terms[0].lstrip('+')

        # Combine terms into the polynomial string
        return fr"$y={''.join(terms).lstrip('+')}$"


    def __str__(self):
        """
        Return a human-readable string for the polynomial.
        """
        return str(self.poly)
    
def my_slider(min, max, id):
    step = int(max/5)
    slider = dcc.Slider(
                updatemode='drag',disabled=True,id=id, min=min, max=max, 
                marks={i: str(i) for i in range(min, max+1, step)}
            )
    return slider

