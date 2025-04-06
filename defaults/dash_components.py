from .mathematics import POLYNOMIALS


slider_max=10
slider_default={"min":-slider_max, "max":slider_max,}
dropdown_polynomial_options = [{'label': key, 'value': key} for key in POLYNOMIALS.keys()]
