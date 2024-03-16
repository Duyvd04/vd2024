def input_student_info(stdscr, students):
    id = stdscr.getstr(10, 10, 60).decode(encoding="utf-8")
    name = stdscr.getstr(11, 10, 60).decode(encoding="utf-8")
    dob = stdscr.getstr(12, 10, 60).decode(encoding="utf-8")
    students.append(Student(id, name, dob))

def input_course_info(stdscr, courses):
    id = stdscr.getstr(10, 10, 60).decode(encoding="utf-8")
    name = stdscr.getstr(11, 10, 60).decode(encoding="utf-8")
    credit = int(stdscr.getstr(12, 10, 60).decode(encoding="utf-8"))
    courses.append(Course(id, name, credit))

def input_marks(stdscr, students, course_id, marks):
    for student in students:
        mark = float(stdscr.getstr(10, 10, 60).decode(encoding="utf-8"))
        mark = math.floor(mark * 10) / 10.0  # round down to 1 decimal place
        marks.append(Mark(student.id, course_id, mark))
