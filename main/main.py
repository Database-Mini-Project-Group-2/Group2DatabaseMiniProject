import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Output, Input, callback
from home_ui import home_content
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.config.suppress_callback_exceptions = True

sidebar = html.Div(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=app.get_asset_url('bike_logo.png'), height="92px", width='auto')),
                    dbc.Col(html.H2("Marigold", className="ms-1")),
                ],
                align="start",
                className="g-0",
            ),
            href="/",
            style={"textDecoration": "none"},
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Shop Dashboard", href="/shop_ui", active="exact"),
                dbc.NavLink("Products per Shop", href="/products", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
    },
)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    html.Div(id="page-content", style={"margin-left": "16rem", })
])


@callback(Output("page-content", "children"),
          Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return home_content
    elif pathname == "/shop_ui":
        return html.P("This is the dashboard per shop.")
    elif pathname == "/products":
        return html.P("This is page will shop all the products with it pictures.")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@callback(
    Output("selling-products-pie-chart", "figure"),
    Input("names", "value"), )
def generate_selling_products_chart(names):
    df = px.data.tips()  # replace with your own data source
    fig = px.pie(df, values='total_bill', names=names, hole=.3)
    return fig


@callback(
    Output("shop-name-display", "children"),
    Input("store-dropdown-menu", "value"),
)
def on_form_change(store_value):
    return f"Display information for this store: {store_value}."


if __name__ == '__main__':
    app.run_server(debug=True)
