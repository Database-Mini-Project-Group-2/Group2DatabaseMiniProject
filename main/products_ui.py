import dash_bootstrap_components as dbc
from dash import html, dcc
from backend import store_names_df, store_table_df

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
