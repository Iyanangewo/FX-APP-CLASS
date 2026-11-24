from util.file_util import read_file

def get_grade_config() -> dict:
    return read_file("grade_config_v1.json")

def convert_grade(num: float):
    if num == None or num > 100 or num < 0:
        return "Invalid Input"
    else:
        config = get_grade_config()
        for key in config.keys():
            if num >= config.get(key).get("min") and num <= config.get(key).get("max"):
                return key  

s_input = input("grading conversion \nRaw grade:")
print(f"converted grade: {convert_grade(float(s_input))}")
