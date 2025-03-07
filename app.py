import dash
import dash_bootstrap_components as dbc
from layout import page_layout
# import callbacks, callbacks_theme_toggle 
import callbacks
import os

FLASK_DEBUG = os.environ.get('FLASK_DEBUG')


MATHJAX_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/MathJax.js?'

external_scripts = ['https://polyfill.io/v3/polyfill.min.js?features=es6',
                    {'type': 'text/javascript',
                     'id': 'MathJax-script',
                     'src': MATHJAX_CDN,
                     },
                    ]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [dbc.themes.SLATE, dbc_css, dbc.icons.FONT_AWESOME]
# external_stylesheets = [dbc.themes.DARKLY, dbc_css, dbc.icons.FONT_AWESOME]
# external_stylesheets = [dbc.themes.CYBORG, dbc_css, dbc.icons.FONT_AWESOME]
# external_stylesheets = [dbc.themes.VAPOR, dbc_css, dbc.icons.FONT_AWESOME]



app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1"}],
                prevent_initial_callbacks=True)


server=app.server
app.layout = page_layout()
app.scripts.config.serve_locally = True  # Needed for Dash DAQ components

# callbacks_theme_toggle.clientside_callback
# callbacks_theme_toggle.callback_wrapper(app)
callbacks.callback_wrapper(app)



if __name__ == '__main__':
    if FLASK_DEBUG == 'development':
        app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True)
    elif FLASK_DEBUG == 'production':
        app.run_server(debug=False)