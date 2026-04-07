import os, json

def read(file_name: str):
    path = os.path.abspath(__file__ + '/../../static/' + file_name)
    with open(path) as file:
        return json.load(file)
    