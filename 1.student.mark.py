# 1.student.mark.py

students = []
courses = []
marks = []

def input_number_of_students():
    num = int(input("Enter number of students: "))
    return num

def input_student_info():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DoB: ")
    students.append({"id": id, "name": name, "dob": dob})

def input_number_of_courses():
    num = int(input("Enter number of courses: "))
    return num

def input_course_info():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append({"id": id, "name": name})

def input_marks():
    course_id = input("Select a course ID: ")
    for student in students:
        mark = float(input(f"Enter mark for student {student['name']}: "))
        marks.append({"student_id": student["id"], "course_id": course_id, "mark": mark})

def list_courses():
    for course in courses:
        print(course)

def list_students():
    for student in students:
        print(student)

def show_marks():
    course_id = input("Enter course ID to view marks: ")
    for mark in marks:
        if mark["course_id"] == course_id:
            print(f"Student ID: {mark['student_id']}, Mark: {mark['mark']}")

# Driver code
num_students = input_number_of_students()
for _ in range(num_students):
    input_student_info()

num_courses = input_number_of_courses()
for _ in range(num_courses):
    input_course_info()

input_marks()

list_courses()
list_students()
show_marks()
