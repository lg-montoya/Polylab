from .mathematics import POLYNOMIALS, SINUSOIDALS


SLIDER_MAX = 10  # (absolute) Maximum value for sliders
slider_default = {
    "min": -SLIDER_MAX,
    "max": SLIDER_MAX,
}
dropdown_polynomial_options = [
    {"label": key, "value": key} for key in POLYNOMIALS.keys()
]

dropdown_sinusoidals_options = [
    {"label": key, "value": key} for key in SINUSOIDALS.keys()
]