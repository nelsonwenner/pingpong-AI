import os, json


def create_file(path, name_file):
    custom_path = "{}{}{}".format(os.getcwd(), path, name_file)
    return open(custom_path, "w")


def save_data(path, data, name_file, flag=False):
    custom_path = open("{}{}{}".format(os.getcwd(), path, name_file), "w")
    with custom_path as out:
        if flag: return json.dump(data.tolist(), out)
        return json.dump(data, out)

def get_file(path):
    open_path = open("{}{}".format(os.getcwd(), path))
    return json.load(open_path)


def get_data(path, index=0, flag=True):
    if flag: return list(map(lambda data: data[index], get_file(path)))
    return get_file(path)