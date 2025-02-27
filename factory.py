import plotly.graph_objs as go
import numpy as np
from sympy import symbols, latex, expand
import plotly.io as pio

class MyPolynomial:
    def __init__(self, coefficients):
        """
        Initialize the polynomial with coefficients.
        :param coefficients: List of coefficients [a_n, a_(n-1), ..., a_0]
                             where a_n * x^n + a_(n-1) * x^(n-1) + ... + a_0
        """
        self.coefficients = coefficients
        self.poly = np.polynomial.Polynomial(coefficients)  # Create a NumPy polynomial object

    def evaluate(self, x):
        """
        Evaluate the polynomial at a given value of x.
        :param x: Value or array of values to evaluate.
        :return: Result(s) as a NumPy array or scalar.
        """
        return self.poly(x)    
    
    def derivative(self, order=1):
        """
        Compute the derivative of the polynomial.
        :param order: Order of the derivative.
        :return: A new Polynomial object representing the derivative.
        """
        return self.poly.deriv(m=order)
    
    def plot(self):
        """
        Plot the polynomial in the interval [-10, 10] using Plotly Dash.
        """

        x_values = np.linspace(-10, 10, 400)
        y_values = self.evaluate(x_values)

        fig = go.Figure()

        # Plot the polynomial
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines'))
        
        return fig

    
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
    
    



def plot_axes():
    """
    Plot only the x-axis and y-axis in the interval [-10, 10] using Plotly Dash.
    """
    fig = go.Figure()

    # Plot the x=0 line (y-axis)
    fig.add_trace(go.Scatter(x=[0, 0], y=[-10, 10], mode='lines', line=dict(color='black'), showlegend=False))

    # Plot the f(x)=0 line (x-axis)
    fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', line=dict(color='black'), showlegend=False))

    # Update layout to set the range for x-axis and y-axis
    fig.update_layout(
        showlegend=False,
        xaxis=dict(range=[-10, 10], zeroline=False),
        yaxis=dict(range=[-10, 10], zeroline=False),
    )
    
    # fig.update_layout(showlegend=False)

    return fig
    
    