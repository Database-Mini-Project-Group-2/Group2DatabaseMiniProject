from dash import Output, Input, callback
import plotly.express as px
from ui import app


@callback(
    Output("selling-products-pie-chart", "figure"),
    Input("names", "value"), )
def generate_selling_products_chart(names):
    df = px.data.tips()  # replace with your own data source
    # fig = px.pie(df, values=['total_bill', 'tip', 'size'], names=names, hole=.3)
    fig = px.pie(df, values='size', names=names, hole=.3)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
