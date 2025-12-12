import duckdb



def generate_daily_metrics() -> None:

    duckdb.sql(f'''
                COPY(SELECT 
                    DATA,
                    VALOR,
                    MONTH(DATA) AS MES,
                    ROUND(VALOR - LAG(VALOR) OVER (ORDER BY data),2) AS variacao_diaria_bruto, 
                    ROUND((variacao_diaria_bruto / LAG(VALOR) OVER (ORDER BY DATA)),2) AS variacao_diaria_perc
                FROM read_csv_auto("data/bronze/dolar/dolar_2025.csv", 
                                    header=true, 
                                    columns={{'DATA':'DATE',
                                            'VALOR':'DECIMAL(6,4)'
                                            }})
                ) TO "data/analytics/daily_metrics.csv"
               
               ''')

def generate_monthly_metrics() -> None:

    duckdb.sql(f'''
                COPY(
                WITH temp AS (
                SELECT
                    DATE_TRUNC('month',DATA) AS DATA,
                    AVG(VALOR) as media_mensal,
                    
                FROM read_csv_auto("data/bronze/dolar/dolar_2025.csv", 
                                    header=true, 
                                    columns={{'DATA':'DATE',
                                            'VALOR':'DECIMAL(6,4)'
                                            }})
                GROUP BY DATA 
               )
               
               
               SELECT DATA,
                    MONTH(DATA) AS MES,
                    ROUND(media_mensal,2) as media_mensal,
                    ROUND(media_mensal - LAG(media_mensal) OVER (ORDER BY DATA), 2) AS variacao_mensal_bruto, 
                    ROUND((variacao_mensal_bruto / LAG(media_mensal) OVER (ORDER BY DATA)) ,2) as variacao_mensal_perc 
                FROM temp 
                   ORDER BY DATA
                ) TO "data/analytics/monthly_metrics.csv"
               
               ''')

generate_daily_metrics()