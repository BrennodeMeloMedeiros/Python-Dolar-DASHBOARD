import duckdb
import logging
import config

def src_to_raw(src_path: str, months: int, year:int) -> None:
    for i in range(1, months + 1):
        duckdb.sql(f'''
                COPY(
                WITH df as (
                    SELECT STRPTIME(data, '%d/%m/%Y') as data_conv, * from read_json("{src_path}") 
                )
                SELECT data, valor FROM df
                WHERE 
                    MONTH(data_conv) = {i}
                    AND
                    YEAR(data_conv) = {year}
                ) TO "{config.DOLAR_PATH}{i:02.0f}-{year}.json"
                ''')

    logging.info("RAW atualziado")