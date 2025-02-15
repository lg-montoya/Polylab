POLYNOMIALS = {
    'constant':{
        'default_coefficients':[1,0,0,0], 'general_form':r"$f(x)=a$",
        'available_sliders':[True, False, False, False]
        },
    'linear':{
        'default_coefficients':[0,1,0,0], 'general_form':r"$f(x)=a + bx$",
        'available_sliders':[True, True, False, False]
        },
    'quadratic':{
        'default_coefficients':[0,0,1,0], 'general_form':r"$f(x)=a+bx+cx^2$",
        'available_sliders':[True, True, True, False]
        },
    'cubic':{
        'default_coefficients':[0,0,0,1], 'general_form':r"$f(x)=a+bx+cx^2+dx^3$",
        'available_sliders':[True, True, True, True]
        },
    }

# GENERAL_FORM = fr"$f(x)={{{P}}}x+b$"

GENERAL_FORM = r"$f(x)=ax+b$"
