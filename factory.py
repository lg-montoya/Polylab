import numpy as np
# import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash import dcc, html
from defaults.dash_components import slider_default
from defaults.cosmetics import STYLE_GRAPH_BORDER
from defaults.chart_elements import empty_figure
from dataclasses import dataclass
from copy import deepcopy


slider_min = slider_default["min"]
slider_max = slider_default["max"]
x_values = np.linspace(-slider_max, slider_max, 400)


class MyPolynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.poly = np.polynomial.Polynomial(
            coefficients
        )  # Create a NumPy polynomial object

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
                terms.append("+x")  # Only sign and variable
            elif b == -1:
                terms.append("-x")  # Only sign and variable
            else:
                terms.append(f"{'+' if b > 0 else ''}{b}x")

        if c != 0:
            if c == 1:
                terms.append("+x^2")  # Only sign and variable
            elif c == -1:
                terms.append("-x^2")  # Only sign and variable
            else:
                terms.append(f"{'+' if c > 0 else ''}{c}x^2")

        if d != 0:
            if d == 1:
                terms.append("+x^3")  # Only sign and variable
            elif d == -1:
                terms.append("-x^3")  # Only sign and variable
            else:
                terms.append(f"{'+' if d > 0 else ''}{d}x^3")

        # Rule 3: If only one term exists, include its sign only if negative
        if len(terms) == 1 and terms[0][0] != "-":
            terms[0] = terms[0].lstrip("+")

        # Combine terms into the polynomial string
        return rf"$y={''.join(terms).lstrip('+')}$"

    def __str__(self):
        """
        Return a human-readable string for the polynomial.
        """
        return str(self.poly)


def my_slider(id, label, disabled=True):
    step = int(slider_max / 5)
    
    # Enable hyperbolae sliders by default and set initial values
    if id.get("type") == "hyperbolae_slider":
        disabled = False
        initial_value = 0 if id.get("name") == "a" else 1 if id.get("name") == "b" else 0
    else:
        initial_value = 0
    
    slider = dbc.Row(
        [
            dbc.Col(
                html.Div(dcc.Markdown(f"$$\\quad {label}$$", mathjax=True)),
                width="auto",
                className="d-flex align-items-center",  # Align label vertically with the slider
            ),
            dbc.Col(
                html.Div(
                    dcc.Slider(
                        updatemode="drag",
                        disabled=disabled,
                        id=id,
                        min=slider_min,
                        max=slider_max,
                        value=initial_value,
                        marks={
                            i: str(i) for i in range(slider_min, slider_max + 1, step)
                        },
                    ),
                    className="w-100",
                ),
                width=True,
            ),
        ],
        className="g-2",
    )
    return slider


@dataclass
class GraphConfig:
    """Ensure each graph has it's own configuration instance rather than sharing a mutable default."""
    id: str
    class_name: str
    x_axis_title: str = None
    
    def create_figure(self):
        """Create a fresh figure instance with this configuration."""
        figure = deepcopy(empty_figure)
        if self.x_axis_title:
            figure.update_layout(xaxis_title=self.x_axis_title)
        return figure


def graph_generator(id: str, class_name: str, x_axis_title=None):
    config = GraphConfig(id=id, class_name=class_name, x_axis_title=x_axis_title)
    my_graph = dbc.Col(
        html.Div(
            dcc.Graph(
                figure=config.create_figure(),
                id=id,
                mathjax=True,
                config={"scrollZoom": False},
                style=STYLE_GRAPH_BORDER,
            )
        ),
        sm=8,
        className=class_name,
    )
    return my_graph
