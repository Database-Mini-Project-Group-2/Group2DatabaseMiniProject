import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from const import SHOP_LOGO


app = Dash(external_stylesheets=[dbc.themes.FLATLY])

# store_dropdown_options = [{'label': str(val), 'value': val} for val in store_names_df['name'].unique()]
# store_dropdown_menu = dcc.Dropdown(
#     children=store_dropdown_options,
#     id='store-dropdown-options',
# )

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=SHOP_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Marigold", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
            ),
            # store_dropdown_menu
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
                        html.H2("Total Sales", className="total-sales"),
                        html.H3("R10123.15", className="total-amount"),
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

