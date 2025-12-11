import json
import requests
import datetime
import os
import csv

def request_data(file_path: str):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json;dataInicial=01/01/2025;dataFinal=31/12/2025&dataInicial=10/12/2015&dataFinal=10/12/2025"
    response = requests.get(url)
    if response.status_code == 200: 
        status = "Concluido"
        data = response.json()
        with open(file_path, "w") as f:
            json.dump(data, f)
    else:
        status = "Erro de retorno API"
        pass


        
if __name__ == "__main__":
    request_data()