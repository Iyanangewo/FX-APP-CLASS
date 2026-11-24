import json
def read_file(file_name: str):
    file = open("students.json", "r")
    content = json.load(file)
    file.close()
    return content

def write_file(file_name: str, contents):
    file = open(file_name, "w")
    json.dump(contents, file, indent=4)
    file.close()    