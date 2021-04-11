import json


def read_file(filename):
    json_data = open(filename, encoding="utf-8")
    data = json.load(json_data)
    return data
