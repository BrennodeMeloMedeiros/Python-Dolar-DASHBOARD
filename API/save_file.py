import json

def save_as_json(path, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file)
