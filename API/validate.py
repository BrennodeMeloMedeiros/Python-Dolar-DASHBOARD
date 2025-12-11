import os

def today_data_exists(DIR: str) -> bool:
    if os.path.isfile(DIR):
        return True
    else:
        return False 