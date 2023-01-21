from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv('winequelity.csv')
app = Dash(__name__)


def table_create(dataframe):
    max_rows = 10
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


app.layout = html.Div([
    html.H3(children='Wine'),
    table_create(df),
    html.Br(),
    html.Label('Model: '),
    dcc.Dropdown(['Regression', 'Classification'], 'Regression', id='method-dropdown'),
    html.Br(),
    html.Label('Variable: '),
    dcc.Dropdown(df.columns.to_list(), 'fixed acidity', id='var-dropdown'),
    dcc.Graph(id='graph')
])


@callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='method-dropdown', component_property='value'),
     Input(component_id='var-dropdown', component_property='value')]
)
def graph_create(model, var):
    if model == 'Regression':
        fig = px.area(df, y="pH", x=var)
    if model == 'Classification':
        fig = px.area(df, x="target", y=var)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
