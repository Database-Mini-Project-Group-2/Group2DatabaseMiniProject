import dash_bootstrap_components as dbc
from dash import html, dcc

from backend import store_names_df

home_content = html.Div([
    dbc.Navbar(
        dbc.Container([
            # Dropdown menu
            html.Div(
                dbc.Select(
                    store_names_df['name'],
                    store_names_df['name'][0],
                    id="store-dropdown-menu",
                ),
                className="py-2",
            ),
        ]),
        color="dark",
        dark=True,
    ),
    dbc.Row(
        [
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H4("Selling Products", className="selling-products"),
                        dcc.Dropdown(id='names',
                                     options=['smoker', 'day', 'time', 'sex'],
                                     value='day',
                                     clearable=False,
                                     ),

                        dcc.Graph(id="selling-products-pie-chart",
                                  style={'height': '22rem', 'width': '22rem'}, ),
                    ]), className="border-0"),
                ], className="border-0")

            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H4("Total Sales", className="total-sales"),
                        html.H5("R10123.15", className="total-amount"),
                    ]), className="border-0"),
                ], className="border-0")
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H4("Shop Name", className="total-sales2"),
                        html.H5("Name", id="shop-name-display"),
                    ]), className="border-0"),
                ], className="border-0")
            ]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(dbc.CardBody([
                        html.H4("Total Sales", className="total-sales"),
                        html.H5("R10123.15", className="total-amount"),
                    ]), className="border-0"),
                ], className="border-0")
            ]),
        ],
        className="g-2",
        style={"margin": "1rem"}
    ),
    dbc.Row(
        dbc.Col([
            # html.Div("An automatically sized column")
        ], width="auto")
    ),
])


