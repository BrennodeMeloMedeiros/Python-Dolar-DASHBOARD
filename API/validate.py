import os

def today_file_exists(dir: str) -> bool:
    if os.path.isfile(dir):
        return True
    else:
        return False 