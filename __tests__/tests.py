import os, json

def save_data(data):
    custom_path = open(os.getcwd() + "/arq.txt", "w")
    with custom_path as out: json.dump(data, out)

def get_data(path):
    open_path = open(os.getcwd() + path)
    data = json.load(open_path)
    return data

class Vector:
    def __init__(self, x, y, side):
        self.vector = {'x': x, 'y': y}
        self.side = side

def main():
    
    #list = [[1, 2], [3, 4], [5, 6]]
    new_list = [{"x": 1, "y": 2, "side": 1}, {"x": 3, "y": 4, "side": 0}, {"x": 5, "y": 6, "hide": 1}]

    #new_list = [Vector(1, 0, 1), Vector(0, 0, 1), Vector(0, 0, 0)]

    #save_data(new_list)

    #print(map(lambda x: x['x'], list)) 

    get_list = get_data("/arq.txt")

    print(map(lambda data: data['x'], get_list)) 


if __name__ == "__main__":
    main()