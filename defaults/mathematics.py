# Below are three different ways to represent derivatives in chart titles.
# derivative_notation={1:"f'(x)", 2:"f''(x)"}
# derivative_notation={1:fr"\frac{{dy}}{{dx}}", 2:fr"\frac{{d^2y}}{{dx^2}}"}
import numpy as np

derivative_notation = {1: rf"dy/dx", 2: rf"d^2y/dx^2"}

POLYNOMIALS = {
    "constant": {
        "default_coefficients": [1, 0, 0, 0],
        "general_form": rf"$$\Large y=a$$",
        "available_sliders": [True, False, False, False],
    },
    "linear": {
        "default_coefficients": [0, 1, 0, 0],
        "general_form": rf"$$\Large y=a + bx$$",
        "available_sliders": [True, True, False, False],
    },
    "quadratic": {
        "default_coefficients": [0, 0, 1, 0],
        "general_form": rf"$$\Large y=a+bx+cx^2$$",
        "available_sliders": [True, True, True, False],
    },
    "cubic": {
        "default_coefficients": [0, 0, 0, 1],
        "general_form": rf"$$\Large y=a+bx+cx^2+dx^3$$",
        "available_sliders": [True, True, True, True],
    },
}


SINUSOIDALS = {
    "Sine": {
        "default_coefficients": [0, 1, 1],
        "general_form": rf"$$\Large y=a + bsin(cx)$$",
        "available_sliders": [True, True, True],
        "function": np.sin,
        "function_name": "sin",
    },
    "Cosine": {
        "default_coefficients": [0, 1, 1],
        "general_form": rf"$$\Large y=a + bcos(cx)$$",
        "available_sliders": [True, True, True],
        "function": np.cos,
        "function_name": "cos",
    },
    "Tangent": {
        "default_coefficients": [0, 1, 1],
        "general_form": rf"$$\Large y=a + btan(cx)$$",
        "available_sliders": [True, True, True],
        "function": np.tan,
        "function_name": "tan",
    },
}
