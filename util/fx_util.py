import json

def read_file(file_name: str):
    with open(file_name, "r") as file:
        content = json.load(file)
        return content

def write_file(file_name: str, content):
    with open(file_name, "w") as file:
        json.dump(content, file, indent=4)
