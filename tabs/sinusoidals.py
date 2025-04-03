import dash_bootstrap_components as dbc
from dash import html
from modals import modal_sinusoidal_instructions
from defaults.mathematics import SINUSOIDALS


tab = html.Div([
            # ROW with just the instructions and "+" button
            dbc.Row([
                dbc.Col([                    
                    html.Div([
                    dbc.Button("Instructions", color="info", outline=False,id='btn-mdl-instructions-sinusoidals-open'),
                    dbc.Button("+", color="secondary", id='dynamic-add-sinusoidal-btn', className='me-md-2')
                    ],
                    className="d-grid gap-2 d-md-flex justify-content-md-start",    
                    ),
                    modal_sinusoidal_instructions,
                ], class_name='mb-3')
            ]),
            
            dbc.Row(id='dynamic-sinusoidal',children=[])
                       
], className="mt-4")