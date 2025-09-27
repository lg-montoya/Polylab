import plotly.graph_objs as go
import numpy as np
from sympy import symbols, latex, expand
import plotly.io as pio
from defaults.dash_components import slider_default

slider_min = slider_default["min"]
slider_max = slider_default["max"]

x_values = np.linspace(-slider_max, slider_max, 400)


class MyPolynomial(go.Figure, np.polynomial.Polynomial):
    def __init__():
        super().__init__()

    pass


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
        return (
            self.polynomial_y(x_values),
            self.polynomial_dy(x_values),
            self.polynomial_d2y(x_values),
        )
