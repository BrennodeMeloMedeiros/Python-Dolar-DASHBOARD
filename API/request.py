import requests
import logging
import config
def request_data() -> dict:
    try:
        response = requests.get(config.URL)
        response.raise_for_status()
        logging.info("Requisicao bem sucedida")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error de API : {e}")
        raise SystemExit(e)
    
if __name__ == "__main__":
    request_data()