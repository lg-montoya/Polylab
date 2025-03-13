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


chart_default_theme = "vizro_dark"
# chart_other_theme = "vapor"
chart_other_theme = "quartz"

slider_max = 20
slider_default = {"min":-slider_max, 
                   "max":slider_max,
                   }

"""
    Default colouring of traces for following templates:
    

   vizro_dark ['#00b4ff', '#ff9222', '#3949ab', '#ff5267', '#08bdba', '#fdc935', '#689f38', '#976fd1', '#f781bf', '#52733e'] 
   quartz ['#00b4ff', '#ff9222', '#3949ab', '#ff5267', '#08bdba', '#fdc935', '#689f38', '#976fd1', '#f781bf', '#52733e'] 
"""



trace_colours = {'default_theme':{1:'#00b4ff', 2:'#ff9222', 3:'#3949ab',},
                 'other_theme':{1:[], 2:[], 3:[]},
}


