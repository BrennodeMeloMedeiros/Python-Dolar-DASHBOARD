import requests
import logging

def request_data() -> dict:
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json;dataInicial=01/01/2025;dataFinal=31/12/2025&dataInicial=01/01/2025&dataFinal=31/12/2025"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Requisicao bem sucedida")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error de API : {e}")
        raise SystemExit(e)
    
if __name__ == "__main__":
    request_data()