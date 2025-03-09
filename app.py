import dash
import dash_bootstrap_components as dbc
from layout import page_layout 
import callbacks
import os

FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

# page themes
page_default_theme= dbc.themes.QUARTZ
page_other_theme = dbc.themes.CYBORG



from defaults import chart_default_theme, chart_other_theme


MATHJAX_CDN = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/MathJax.js?'

FONT_AWESOME = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css'

external_scripts = ['https://polyfill.io/v3/polyfill.min.js?features=es6',
                    {'type': 'text/javascript',
                     'id': 'MathJax-script',
                     'src': MATHJAX_CDN,
                     },
                    ]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
external_stylesheets = [page_default_theme, dbc_css, dbc.icons.FONT_AWESOME]

# external_stylesheets = [page_default_theme, dbc_css, FONT_AWESOME]




app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                meta_tags=[{"name": "viewport",
                            "content": "width=device-width, initial-scale=1"}],
                prevent_initial_callbacks=True)


server=app.server
app.layout = page_layout(page_default_theme, page_other_theme)
app.scripts.config.serve_locally = True  # Needed for Dash DAQ components

# callbacks_theme_toggle.clientside_callback
# callbacks_theme_toggle.callback_wrapper(app)
callbacks.callback_wrapper(app, chart_default_theme, chart_other_theme)



if __name__ == '__main__':
    if FLASK_DEBUG == 'development':
        app.run_server(debug=True, threaded=True, dev_tools_hot_reload=True)
    elif FLASK_DEBUG == 'production':
        app.run_server(debug=False)