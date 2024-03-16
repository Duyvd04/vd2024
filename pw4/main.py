import sys
sys.path.append("..")
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
from input import input_student_info, input_course_info, input_marks
from output import list_courses, list_students, show_marks



def main(stdscr):
    students = []
    courses = []
    marks = []

    num_students = int(stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
    for _ in range(num_students):
        input_student_info(stdscr, students)

    num_courses = int(stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
    for _ in range(num_courses):
        input_course_info(stdscr, courses)

    for course in courses:
        stdscr.addstr(0, 0, f"Entering marks for course {course.name}")
        input_marks(stdscr, students, course.id, marks)

    list_courses(stdscr, courses)
    list_students(stdscr, students)
    show_marks(stdscr, course_id, marks)
    stdscr.refresh()

curses.wrapper(main)
