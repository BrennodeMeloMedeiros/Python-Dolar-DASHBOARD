import datetime
import logging

from API.request import request_data
from API.validate import today_data_exists
from API.save_file import save_as_json
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

def main():
    logging.info("INICIO de execucao")
    day = str(datetime.datetime.now())[:10]
    api_json_path = f"src/data_{day}.json"
    
    if not today_data_exists(api_json_path):
        raw_data = request_data()
        save_as_json(api_json_path, raw_data)
    else:
        logging.info("Requisicao API dispensada")


    print("Continuou")
    logging.info("FIM de execucao")
if __name__ == "__main__":
    main()