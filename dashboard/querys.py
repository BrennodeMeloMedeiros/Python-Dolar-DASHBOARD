import duckdb

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