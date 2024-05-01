import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

from backend import store_names_df

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url('bike_logo.png'), height="48px")),
                        dbc.Col(dbc.NavbarBrand("Marigold", className="ms-1")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            # Dropdown menu
            html.Div(
                dbc.Select(
                    store_names_df['name'],
                    store_names_df['name'][0],
                    id="store-dropdown-menu",
                ),
                className="py-2",
            ),
        ]
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div([
    navbar,
    dbc.Row(
        [
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H2("Total Sales", className="total-sales"),
                        html.H3("R10123.15", className="total-amount"),
                    ])),
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H2("Selling Products", className="selling-products"),
                        dcc.Dropdown(id='names',
                                     options=['smoker', 'day', 'time', 'sex'],
                                     value='day',
                                     clearable=False,
                                     ),

                        dcc.Graph(id="selling-products-pie-chart",
                                  style={'height': '18rem', 'width': '18rem'}, ),
                    ])),
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H2("Shop Name", className="total-sales2"),
                        html.H4("Name", id="shop-name-display"),
                    ])),
                ])
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H2("Total Sales", className="total-sales"),
                        html.H3("R10123.15", className="total-amount"),
                    ])),
                ])
            ]),
        ],
        className="g-2",
        style={"margin": "2rem"}
    ),
    dbc.Row(
        dbc.Col([
            html.Div("An automatically sized column")
        ], width="auto")
    ),
])
