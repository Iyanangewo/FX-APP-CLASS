from util.file_util import read_file, write_file

def add_student():
    students = read_file("students.json")

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    write_file("students.json", students)
    print(f"Student {name} added successfully!")

def display_students():
        students = read_file("students.json")
        for student in students:
            print(student)

add_student()
display_students()