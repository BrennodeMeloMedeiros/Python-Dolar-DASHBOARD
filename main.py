import datetime
import logging
from API.request import request_data
from API.validate import today_file_exists
from API.save_file import save_as_json
from extract.extract_raw import src_to_raw
from extract.raw_to_bronze import raw_to_bronze
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

def main():
    logging.info("INICIO de execucao")
    
    day = str(datetime.datetime.now())[:10]
    today_src_file = f"src/data_{day}.json"
    if not today_file_exists(today_src_file):
        raw_data = request_data()
        save_as_json(today_src_file, raw_data)
    else:
        logging.info("Requisicao API dispensada")

    src_to_raw(today_src_file, months = 12, year = 2025)
    raw_to_bronze()


    logging.info("FIM de execucao")
if __name__ == "__main__":
    main()