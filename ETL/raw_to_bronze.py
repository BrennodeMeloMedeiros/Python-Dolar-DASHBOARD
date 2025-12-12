import duckdb
import config

def raw_to_bronze() -> None:
    duckdb.sql(f'''
        COPY(    
        WITH temp AS (
            SELECT DISTINCT * FROM read_json("data/raw/dolar/*.json")                    
            WHERE
                data is not null
                AND 
                data <> ''
                AND
                valor is not null
                AND
                valor <> ''
        )
        SELECT CAST(strptime(data, '%d/%m/%Y') AS DATE) as DATA, CAST(valor as DECIMAL(6,4)) as VALOR FROM temp
            ORDER BY DATA
        ) TO "{config.BRONZE_DOLAR_PATH}dolar_2025.csv"
    ''')

