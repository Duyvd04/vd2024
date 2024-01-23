class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB: ")
        self.students.append(Student(id, name, dob))

    def input_course_info(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self.courses.append(Course(id, name))

    def input_marks(self, course_id):
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.name}: "))
            self.marks.append(Mark(student.id, course_id, mark))

    def list_courses(self):
        for course in self.courses:
            print(course.__dict__)

    def list_students(self):
        for student in self.students:
            print(student.__dict__)

    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        for mark in self.marks:
            if mark.course_id == course_id:
                print(f"Student ID: {mark.student_id}, Mark: {mark.mark}")

school = School()

num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    school.input_student_info()

num_courses = int(input("Enter number of courses: "))
for _ in range(num_courses):
    school.input_course_info()

for course in school.courses:
    print(f"Entering marks for course {course.name}")
    school.input_marks(course.id)

school.list_courses()
school.list_students()
school.show_marks()
