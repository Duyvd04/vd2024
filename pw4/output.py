def list_courses(stdscr, courses):
    stdscr.addstr(0, 0, "Courses:")
    for i, course in enumerate(courses, start=1):
        stdscr.addstr(i, 0, str(course.__dict__))

def list_students(stdscr, students):
    students.sort(key=lambda student: student.gpa, reverse=True)  # sort by GPA descending
    stdscr.addstr(0, 0, "Students:")
    for i, student in enumerate(students, start=1):
        stdscr.addstr(i, 0, str(student.__dict__))

def show_marks(stdscr, course_id, marks):
    stdscr.addstr(0, 0, "Marks:")
    for i, mark in enumerate(marks, start=1):
        if mark.course_id == course_id:
            stdscr.addstr(i, 0, f"Student ID: {mark.student_id}, Mark: {mark.mark}")
