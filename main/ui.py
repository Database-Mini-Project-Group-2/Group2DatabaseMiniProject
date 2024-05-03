import dash_bootstrap_components as dbc
from dash import html, dcc
from backend import store_names_df, store_table_df

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
                             style={'height': 'auto', 'width': '50%', 'border': '0',
                                    'size': 'small', "background-color": "#0000"}),

                dcc.Graph(id="selling-products-pie-chart",
                          style={'height': 'auto', 'width': '24rem', "background-color": "#0000"}, ),
            ], width='auto', ),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Total Sales"),
                                dbc.Label("R10123.50", id="total-amount", style={'height': '2.5rem'}),
                            ])
                        ], className="border-0",
                            style={"background-color": "#f8f9fa09"})
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Shop Name"),
                                dbc.Label(".", id="shop-name-display", style={'height': '2.5rem'}),
                            ])
                        ], className="border-0",
                            style={"background-color": "#f8f9fa09"})
                    ]),
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Total Sales"),
                                dbc.Label("R10123.15", id="total-amount", style={'height': '2.5rem'}),
                            ])
                        ], className="border-0",
                            style={"background-color": "#f8f9fa09"})
                    ]),
                ], className="g-1", ),
                dbc.Row(dcc.Graph(id='histogram-chart',
                                  style={'height': '20rem', 'width': '42rem', }, )),

            ], className="g-1", )
        ]
    ),
    # dbc.Row(dcc.Graph(id='bars-chart', style={'height': '20rem', 'width': '42rem', }, )),
])

store_content = html.Div([
    dbc.Navbar(
        color="dark",
        dark=True,
        children=[
            dbc.NavbarBrand("Shop Information", className="ms-4"),
            dbc.Container(
                children=html.Div(
                    className="py-2, background-0",
                    children=dbc.Select(
                        store_names_df['name'],
                        store_names_df['name'][0],
                        id="store-dropdown-menu",
                    ),
                ),
            ),
        ]
    ),
    dbc.Col([
        html.H5("Sales Analysis"),
        dcc.Graph(id="line-graph-chart"),
        html.H5("Orders"),
        dcc.Dropdown(id='names',
                     options=['Pending', 'Shipped', 'Success'],
                     value='Pending',
                     clearable=False),
        dbc.Table.from_dataframe(
            store_table_df,
            striped=True,
            bordered=True,
            hover=True, ),
    ], style={"margin": "1rem"}, ),

])

products_content = html.Div([
    dbc.Navbar(
        color="dark",
        dark=True,
        children=[
            dbc.NavbarBrand("Products", className="ms-4"),
            dbc.Container(
                children=html.Div(
                    className="py-2, background-0",
                    children=dbc.Select(
                        store_names_df['name'],
                        store_names_df['name'][0],
                        id="store-dropdown-menu",
                    ),
                ),
            ),
        ]
    ),
    dbc.Col([
        html.Div(id="products-list"),
    ], style={"margin": "1rem"}, ),

])
