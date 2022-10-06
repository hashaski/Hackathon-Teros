from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
url = 'https://raw.githubusercontent.com/hashaski/Hackathon-Teros/test/resultado.csv'
url_teste = 'https://raw.githubusercontent.com/hashaski/Hackathon-Teros/main/dados_teste_x_hackaton.csv'
df = pd.read_csv(url, encoding = "ISO-8859-1")
dft = pd.read_csv(url_teste, encoding = "ISO-8859-1")

fig = px.bar(df, x="ID_cliente", y="Fechou", color="Fechou", barmode="group")
clientes = list(df['ID_cliente'])
app.layout = html.Div (children=[
    html.H1(children='IA Masters'),
    html.H2(children='Probabilidade de Venda'),

    html.Div(children='''
        Essa Probabilidade é de acordo com a IA desenvolvida pelo nosso grupo
    '''),
    dcc.Dropdown(clientes, value='escolha o cliente', id='id-clientes'),
    dcc.Graph(
        id='Regressão Logística',
        figure=fig
    )
])
def generate_table(dft, max_rows=1):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dft.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dft.iloc[i][col]) for col in dft.columns
            ]) for i in range(min(len(dft), max_rows))
        ])
    ])


app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)