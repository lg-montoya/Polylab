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


# chart_default_theme = "vizro_dark"
chart_default_theme = "quartz_dark"
# chart_default_theme = "vapor_dark"
# chart_default_theme = "vapor"
# chart_other_theme = "vapor"
chart_other_theme = "quartz"

slider_max=20
slider_default={"min":-slider_max, "max":slider_max,}

# OBTAIN VALUES BELOW FROM A CELL IN THE JUPYTER NOTEBOOK.
"""
    Default colouring of traces for following templates:
    vapor ['#6829ad', '#e14b56', '#19f37f', '#f7c200', '#51a0f6']
    vizro_dark ['#00b4ff', '#ff9222', '#3949ab', '#ff5267', '#08bdba', '#fdc935', '#689f38', '#976fd1', '#f781bf', '#52733e'] 
    quartz [['#e72e84', '#f77f14', '#52e8b5', '#ffef47', '#21a4d3']]
"""



trace_colours = {
    'default_theme':{0:'#00b4ff', 1:'#ff9222', 2:'#3949ab'},
    # 'default_theme':{0:'#6829ad', 1:'#e14b56', 2:'#19f37f'},
    'other_theme':{0:'#e72e84', 1:'#f77f14', 2:'#52e8b5'}
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