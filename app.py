import dash
import os
import dash_bootstrap_components as dbc
from layout import app_layout 
import callbacks
from defaults.cosmetics import (
    chart_default_theme, chart_other_theme, 
    page_default_theme, page_other_theme
    )

# Determine if production or development environment
FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

# Configure external stylesheets and scripts
MATHJAX_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/MathJax.js?'
external_scripts = ['https://polyfill.io/v3/polyfill.min.js?features=es6',
                    {'type': 'text/javascript',
                     'id': 'MathJax-script',
                     'src': MATHJAX_CDN,
                     },
                    ]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [page_default_theme, dbc_css, dbc.icons.FONT_AWESOME]

# Initialize the app
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1"}],
                title="Maths Lab",
                prevent_initial_callbacks=True)
server=app.server
app.scripts.config.serve_locally = True  # Needed for Dash DAQ components

# Load the layout and callbacks
app.layout = app_layout(page_default_theme, page_other_theme)
callbacks.callback_wrapper(app, chart_default_theme, chart_other_theme)

# Set the server to run in production or development mode
if __name__ == '__main__':
    if FLASK_DEBUG == 'development':
        # app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True, port=8080)
        app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True)
    elif FLASK_DEBUG == 'production':
        app.run_server(debug=False)