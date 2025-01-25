import plotly.graph_objs as go
import numpy as np
from sympy import symbols, latex, expand
import plotly.io as pio

class Polynomial:
    def __init__(self, coefficients=[1,1,1,1]):
        """
        Initialize the polynomial with coefficients.
        :param coefficients: List of coefficients [a_n, a_(n-1), ..., a_0]
                             where a_n * x^n + a_(n-1) * x^(n-1) + ... + a_0
        """
        self.coefficients = coefficients
        self.poly = np.poly1d(coefficients)  # Create a NumPy polynomial object

    def evaluate(self, x):
        """
        Evaluate the polynomial at a given value of x.
        :param x: Value or array of values to evaluate.
        :return: Result(s) as a NumPy array or scalar.
        """
        return self.poly(x)

    def latex(self):
        """
        Generate the LaTeX representation of the polynomial.
        :return: LaTeX string for the polynomial.
        """
        x = symbols('x')
        polynomial_exp = sum(coeff * x**i for i, coeff in enumerate(reversed(self.coefficients)))
        return f"$${latex(expand(polynomial_exp))}$$"

    def __str__(self):
        """
        Return a human-readable string for the polynomial.
        """
        return str(self.poly)
    
    def plot(self):
        """
        Plot the polynomial in the interval [-10, 10] using Plotly Dash.
        """

        x_values = np.linspace(-10, 10, 400)
        y_values = self.evaluate(x_values)

        fig = go.Figure()

        # Plot the polynomial
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines'))

        # Plot the x=0 line
        # fig.add_trace(go.Scatter(x=[0, 0], y=[min(y_values), max(y_values)], mode='lines'))
        # fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines'))
        
        fig.update_layout(showlegend=False)
        
        return fig
    
    def plot_axes(self):
        """
        Plot only the x-axis and y-axis in the interval [-10, 10] using Plotly Dash.
        """
        fig = go.Figure()

        # Plot the x=0 line (y-axis)
        fig.add_trace(go.Scatter(x=[0, 0], y=[-10, 10], mode='lines', line=dict(color='black')))

        # Plot the f(x)=0 line (x-axis)
        fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', line=dict(color='black')))

        # Update layout to set the range for x-axis and y-axis
        fig.update_layout(
            showlegend=False,
            xaxis=dict(range=[-10, 10], zeroline=False),
            yaxis=dict(range=[-10, 10], zeroline=False),
        )

            
        return fig
    
    