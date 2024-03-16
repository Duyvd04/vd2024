import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.gpa = None

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Mark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

class School:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self):
        id = self.stdscr.getstr(10, 10, 60).decode(encoding="utf-8")
        name = self.stdscr.getstr(11, 10, 60).decode(encoding="utf-8")
        dob = self.stdscr.getstr(12, 10, 60).decode(encoding="utf-8")
        self.students.append(Student(id, name, dob))

    def input_course_info(self):
        id = self.stdscr.getstr(10, 10, 60).decode(encoding="utf-8")
        name = self.stdscr.getstr(11, 10, 60).decode(encoding="utf-8")
        credit = int(self.stdscr.getstr(12, 10, 60).decode(encoding="utf-8"))
        self.courses.append(Course(id, name, credit))

    def input_marks(self, course_id):
        for student in self.students:
            mark = float(self.stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
            mark = math.floor(mark * 10) / 10.0  # round down to 1 decimal place
            self.marks.append(Mark(student.id, course_id, mark))

    def calculate_gpa(self, student_id):
        marks = np.array([mark.mark for mark in self.marks if mark.student_id == student_id])
        credits = np.array([course.credit for course in self.courses for mark in self.marks if mark.course_id == course.id and mark.student_id == student_id])
        gpa = np.sum(marks * credits) / np.sum(credits)
        return gpa

    def update_students_gpa(self):
        for student in self.students:
            student.gpa = self.calculate_gpa(student.id)

    def list_courses(self):
        self.stdscr.addstr(0, 0, "Courses:")
        for i, course in enumerate(self.courses, start=1):
            self.stdscr.addstr(i, 0, str(course.__dict__))

    def list_students(self):
        self.update_students_gpa()
        self.students.sort(key=lambda student: student.gpa, reverse=True)  # sort by GPA descending
        self.stdscr.addstr(0, 0, "Students:")
        for i, student in enumerate(self.students, start=1):
            self.stdscr.addstr(i, 0, str(student.__dict__))

    def show_marks(self):
        course_id = self.stdscr.getstr(10, 10, 60).decode(encoding="utf-8")
        self.stdscr.addstr(0, 0, "Marks:")
        for i, mark in enumerate(self.marks, start=1):
            if mark.course_id == course_id:
                self.stdscr.addstr(i, 0, f"Student ID: {mark.student_id}, Mark: {mark.mark}")

def main(stdscr):
    # Initialize the school with the stdscr object
    school = School(stdscr)

    num_students = int(stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
    for _ in range(num_students):
        school.input_student_info()

    num_courses = int(stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
    for _ in range(num_courses):
        school.input_course_info()

    for course in school.courses:
        stdscr.addstr(0, 0, f"Entering marks for course {course.name}")
        school.input_marks(course.id)

    school.list_courses()
    school.list_students()
    school.show_marks()
    stdscr.refresh()
curses.wrapper(main)
