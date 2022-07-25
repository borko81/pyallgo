import json

a = {
    "name": "John",
    "age": 31,
    "Salary": 25000
}


def write_data_to_file():
    with open('sample.json', 'w') as f:
        json.dump(a, f, indent=4)


def load_json_data_from_file():
    with open('sample.json', 'r') as f:
        convert_data = json.load(f)
    return convert_data
