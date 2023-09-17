from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from data import path 

app = Dash(__name__)

app.layout = html.Div([
    # html.H4('Simple stock plot with adjustable axis'),
    html.Button("Button", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv(path) # replace with your own data source
    df = df[:100]

    # PIE CHART
    # fig = px.pie(df, values='length', names='type')
    
    # SCATTER PLOT
    fig = px.scatter(df, x="country", y="length", size="length", color="country", hover_data=["length"])

    #LINE PLOT
    # fig = px.line(df, x="length", y="type", title='Life expectancy in Canada')

    return fig

app.run_server(debug=True, use_reloader=True)
