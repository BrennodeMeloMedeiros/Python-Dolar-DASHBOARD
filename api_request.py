import json
import requests
import datetime
import os

def request_data():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json;dataInicial=01/01/2025;dataFinal=31/12/2025&dataInicial=10/12/2015&dataFinal=10/12/2025"
    response = requests.get(url)
    
    c_time = str(datetime.datetime.now())[:19]
    c_time = c_time.replace(":", ".")
    
    if response.status_code == 200: 
        status = "Concluído"
        path = f"data/raw/raw_{c_time}.json"
        data = response.json()
        with open(path, "w") as f:
            json.dump(data, f)
    else:
        status = "Erro"
        print("######################")
        print("Houve um erro no retorno da API")
        print("######################")
        pass

    register_log(status, c_time)

def register_log(status: str, time: str):
    
    with open("log.json", "a") as log:
        line = [
                {"nome": os.getlogin()}, 
                {"hora": time}, 
                {"status": status}
                ]
        json.dump(line, log)
if __name__ == "__main__":
    request_data()