import os, json


def create_file(name):
    custom_path = os.getcwd() + '/database/' + name
    return open(custom_path, "w")


def save_data(data, path):
    custom_path = open(os.getcwd() + '/database/' + path, "w")
    with custom_path as out: json.dump(data, out)
       

def get_file(path):
    open_path = open(os.getcwd() + path)
    return json.load(open_path)


def get_data(path, key):
    return map(lambda data: data[key], get_file(path))
