import dash_bootstrap_components as dbc
from dash import html, dcc

home_content = html.Div([
    dbc.Navbar(
        color="dark",
        dark=True,
        children=dbc.NavbarBrand("Dashboard", className="ms-4"),
    ),
    dbc.Row(
        className="g-2",
        style={"margin": "1rem"},
        children=[
            dbc.Col([
                html.H5("Selling Products"),
                dcc.Dropdown(id='names',
                             options=['smoker', 'day', 'time', 'sex'],
                             value='day',

                             clearable=False,
                             style={'height': 'auto', 'width': '50%', 'border': '0', 'size': 'small'}),

                dcc.Graph(id="selling-products-pie-chart",
                          style={'height': 'auto', 'width': '24rem'}, ),
            ], width='auto', ),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader(dbc.CardBody([
                                html.H5("Total Sales"),
                                dbc.Label("R10123.50", id="total-amount", style={'height': '2.5rem'}),
                            ]), className="border-0"),
                        ], className="border-0")
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader(dbc.CardBody([
                                html.H5("Shop Name"),
                                dbc.Label(".", id="shop-name-display", style={'height': '2.5rem'}),
                            ]), className="border-0"),
                        ], className="border-0")
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardHeader(dbc.CardBody([
                                html.H5("Total Sales"),
                                dbc.Label("R10123.15", id="total-amount", style={'height': '2.5rem'}),
                            ]), className="border-0"),
                        ], className="border-0")
                    ]),
                ], className="g-1", ),
                dbc.Row(dcc.Graph(id='histogram-chart', style={'height': '20rem', 'width': '42rem'}, ))
            ], className="g-1", )
        ]
    ),
])
