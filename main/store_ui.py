import dash_bootstrap_components as dbc
from dash import html, dcc
from backend import store_names_df, store_table_df

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
            hover=True,),
    ], style={"margin": "1rem"}, ),

])
