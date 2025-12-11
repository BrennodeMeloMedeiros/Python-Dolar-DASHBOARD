import datetime
import logging

from API.request import request_data
from API.validate import today_data_exists
from API.save_file import save_as_json
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 

def main():
    c_date = str(datetime.datetime.now())[:10]
    api_data_path = f"src/data_{c_date}.json"
    
    if not today_data_exists(api_data_path):
        raw_data = request_data()
        save_as_json(api_data_path, raw_data)
    else:
        logging.INFO("Requisição API dispensada")
    

    print("Continuou")
    
if __name__ == "__main__":
    main()