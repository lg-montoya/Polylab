# Below are three different ways to represent derivatives in chart titles.
# derivative_notation={1:"f'(x)", 2:"f''(x)"}
# derivative_notation={1:fr"\frac{{dy}}{{dx}}", 2:fr"\frac{{d^2y}}{{dx^2}}"}
derivative_notation={1:fr"dy/dx", 2:fr"d^2y/dx^2"}

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