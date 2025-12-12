from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import webbrowser
import duckdb
import plotly.graph_objects as go


def start_app():
    app = Dash()

    months_dropmenu = [
            {'label': 'Tudo', 'value': 0},
            {'label': 'Janeiro', 'value': 1},
            {'label': 'Fevereiro', 'value': 2},
            {'label': 'Março', 'value': 3},
            {'label': 'Abril', 'value': 4},
            {'label': 'Maio', 'value': 5},
            {'label': 'Junho', 'value': 6},
            {'label': 'Julho', 'value': 7},
            {'label': 'Agosto', 'value': 8},
            {'label': 'Setembro', 'value': 9},
            {'label': 'Outubro', 'value': 10},
            {'label': 'Novembro', 'value': 11},
            {'label': 'Dezembro', 'value': 12},
        ]
    avg_value = duckdb.sql('''
                        SELECT ROUND(AVG(VALOR),2) 
                        FROM read_csv_auto("data/analytics/daily_metrics.csv")
                        ''').fetchall()[0][0]

    brute_daily_variation = duckdb.sql('''
                        SELECT ROUND(AVG(variacao_diaria_bruto),4) 
                        FROM read_csv_auto("data/analytics/daily_metrics.csv")
                        ''').fetchall()[0][0]
    if brute_daily_variation < 0:
        brute_daily_variation = f"-R${brute_daily_variation * -1}"
        
    perc_daily_variation = duckdb.sql('''
                        SELECT ROUND(AVG(variacao_diaria_perc),4) 
                        FROM read_csv_auto("data/analytics/daily_metrics.csv")
                        ''').fetchall()[0][0]

    brute_monthly_variation = duckdb.sql('''
                        SELECT ROUND(AVG(variacao_mensal_bruto),4) 
                        FROM read_csv_auto("data/analytics/monthly_metrics.csv")
                        ''').fetchall()[0][0]
    if brute_monthly_variation < 0:
        brute_monthly_variation = f"-R${brute_monthly_variation * -1}"

    perc_monthly_variation = duckdb.sql('''
                        SELECT ROUND(AVG(variacao_mensal_perc),4) 
                        FROM read_csv_auto("data/analytics/monthly_metrics.csv")
                        ''').fetchall()[0][0]

    app.layout = html.Div(
        className="body",
        children=[
            html.Div(
                className="row",
                children=[
                    html.Div(
                        className="month card",
                        children=["Selecione o mês desejado", dcc.Dropdown(options=months_dropmenu, value=0, clearable=False, id= "dropdown", placeholder="Escolha")]
                        ),
                        html.Div(
                        className="box",
                        children=[
                            "Valor médio ANUAL",
                            html.Div(className="label", children=[f"R${avg_value}"])
                                ]     
                        ),
                        html.Div(
                        className="box",
                        children=[
                            "Variação média mensal Bruta",
                            html.Div(className="label", children=[brute_monthly_variation])
                                ]     
                        )
                        ,html.Div(
                        className="box",
                        children=[
                            "Variação média mensal em %",
                            html.Div(className="label", children=[f"{perc_monthly_variation}%"])
                                ]     
                            )]
                    ),
            html.Div(
                className="full-box",
                children=[
                    html.Div(
                        className="box",
                        children=[
                            "Variação média diária bruta",
                            html.Div(className="label", children=[brute_daily_variation])
                                ]     
                            )
                    ,html.Div(
                        className="box",
                        children=[
                            "Variação média diária em %",
                            html.Div(className="label", children=[f"{perc_daily_variation}%"])
                                ]     
                            )
                    ,dcc.Graph(id="grafico")
                ]
                )
                ],
            )



    @app.callback(
        Output("grafico", "figure"),
        Input("dropdown","value")
    )
    def refresh_graph(month):
        print(f"MES ========= {month}")
        if month == 0:
            q = '''
            SELECT STRFTIME(MIN(DATA), '%B') as MES_NOME, ROUND(AVG(VALOR),2) 
            FROM read_csv_auto("data/analytics/daily_metrics.csv") GROUP BY MES ORDER BY MES
            '''

            rows = duckdb.sql(q).fetchall()

            x = [r[0] for r in rows]
            y = [r[1] for r in rows]

        else:
            q = f'''
            SELECT DAY(DATA), VALOR 
            FROM read_csv_auto("data/analytics/daily_metrics.csv") 
            WHERE  MES = {month} 
                
            ORDER BY DATA
            '''
            rows = duckdb.sql(q).fetchall()

            x = [r[0] for r in rows]
            y = [r[1] for r in rows]
        print(x)
        fig = go.Figure(
            data = go.Scatter(
                x = x,
                y = y,
                mode="lines"
            )
        )

        if month == 0:
            fig.update_layout(
                xaxis_title = "Mês",
                yaxis_title = "Valor Dolar"
            )
        else:
            fig.update_layout(
                xaxis_title = "Dia",
                yaxis_title = "Valor Dolar"
            )
        return fig
    webbrowser.open("http://127.0.0.1:8050")
    app.run(debug=True, use_reloader = False)
