import plotly.io as pio
from dash_bootstrap_templates import load_figure_template

POLYNOMIALS = {
    'constant':{
        'default_coefficients':[1,0,0,0], 'general_form':r"$y=a$",
        'available_sliders':[True, False, False, False]
        },
    'linear':{
        'default_coefficients':[0,1,0,0], 'general_form':r"$y=a + bx$",
        'available_sliders':[True, True, False, False]
        },
    'quadratic':{
        'default_coefficients':[0,0,1,0], 'general_form':r"$y=a+bx+cx^2$",
        'available_sliders':[True, True, True, False]
        },
    'cubic':{
        'default_coefficients':[0,0,0,1], 'general_form':r"$y=a+bx+cx^2+dx^3$",
        'available_sliders':[True, True, True, True]
        },
    }

GENERAL_FORM = r"$y=ax+b$"

# derivative_notation={1:"f'(x)", 2:"f''(x)"}
derivative_notation={1:fr"\frac{{dy}}{{dx}}", 2:fr"\frac{{d^2y}}{{dx^2}}"}
# derivative_notation={1:fr"dy/dx", 2:fr"d^2y/dx^2"}

# Choose from 
["quartz_dark", "vizro_dark", "vapor_dark", "vapor", "quartz"]
chart_default_theme = "quartz_dark"
chart_other_theme = "quartz"

slider_max=20
slider_default={"min":-slider_max, "max":slider_max,}


load_figure_template([chart_default_theme, chart_other_theme])
chart_other_theme_colours = list(pio.templates[chart_other_theme]["layout"]["colorway"])
chart_default_theme_colours = list(pio.templates[chart_default_theme]["layout"]["colorway"])

trace_colours = {
    'default_theme':{i:j for i,j in enumerate(chart_default_theme_colours)},
    'other_theme': {i:j for i,j in enumerate(chart_other_theme_colours)}
}

SINUSOIDALS = {
    'Sine':{
        'default_coefficients':[0,1,0,0], 'general_form':r"$y=a + bsinc(x+d)$",
        'available_sliders':[True, True, False, False]
        },
    'Cosine':{
        'default_coefficients':[0,0,1,0], 'general_form':r"$y=a + bcosc(x+d)$",
        'available_sliders':[True, True, True, False]
        },
    'Tangent':{
        'default_coefficients':[0,0,0,1], 'general_form':r"$y=a + btanc(x+d)$",
        'available_sliders':[True, True, True, True]
        },
    }