from .users import Student, TA
from .courses import Course
from tabulate import tabulate


def addStudent(name):
    Student.add(name)

def addTA(name):
    TA.add(name)

def addCourse(name):
    Course.add(name)

def stReg():
    all_students = [
        ["Student ID", "Student Name"],
        [
            '\n'.join(map(str, [student for student in Student.students])),
            '\n'.join(Student.getNames()),
        ],
    ]

    print(f'''Please Enter the Student ID you want to register a course to.
{tabulate(all_students, tablefmt='grid')}
''')
    cid = int(input('>>> '))
    cst = None
    for id, st in Student.students.items():
        if id == cid:
            cst = st
    cst.regCourse

def taReg():
    all_TAs = [
        ["TA ID", "TA Name"],
        ['\n'.join(map(str, [ta for ta in TA.TAs])), '\n'.join(TA.getNames())],
    ]

    print(f'''Please Enter the TA ID you want to register a course to.
{tabulate(all_TAs, tablefmt='grid')}
''')
    cid = int(input('>>> '))
    cta = None
    for id, ta in TA.TAs.items():
        if id == cid:
            cta = ta
    cta.regCourse

def stUnreg():
    all_students = [
        ["Student ID", "Student Name"],
        [
            '\n'.join(map(str, [student for student in Student.students])),
            '\n'.join(Student.getNames()),
        ],
    ]

    print(f'''Please Enter the Student ID you want to unregister a course to.
{tabulate(all_students, tablefmt='grid')}
''')
    cid = int(input('>>> '))
    cst = None
    for id, st in Student.students.items():
        if id == cid:
            cst = st
    cst.unregCourse

def taUnreg():
    all_TAs = [
        ["TA ID", "TA Name"],
        ['\n'.join(map(str, [ta for ta in TA.TAs])), '\n'.join(TA.getNames())],
    ]

    print(f'''Please Enter the TA ID you want to register a course to.
{tabulate(all_TAs, tablefmt='grid')}
''')
    cid = int(input('>>> '))
    cta = None
    for id, ta in TA.TAs.items():
        if id == cid:
            cta = ta
    cta.unregCourse

def showCourses():
    all_courses = [
        ["Course ID", "Course Name"],
        [
            '\n'.join(map(str, [course for course in Course.courses])),
            '\n'.join(Course.getAll()),
        ],
    ]

    print(tabulate(all_courses, tablefmt='grid'))

def showStudents():
    students = {
            'A': [st.name for id, st in Student.students.items()],
    }
    print(tabulate(students, tablefmt='grid'))

def showTAs():
    TAs = {
            'A': [ta.name for id, ta in TA.TAs.items()],
    }
    print(tabulate(TAs, tablefmt='grid'))

def getCoursePS(obj):
    return [
        Student.getCName(student)
        for course, student in Course.courses_list.getEdges
        if type(student) is Student and course == obj
    ]

def getCoursePT(obj):
    return [
        TA.getCName(ta)
        for course, ta in Course.courses_list.getEdges
        if type(ta) is TA and course == obj
    ]

def showCourseInfo():
    table_students = [
            [course for course in Course.getAll()],
            ['\n'.join(getCoursePS(crs)) for id, crs in Course.courses.items()],
    ]
    table_tas = [
            [course for course in Course.getAll()],
            ['\n'.join(getCoursePT(crs)) for id, crs in Course.courses.items()],
    ]
    print('<<< STUDENTS >>>')
    print(tabulate(table_students, tablefmt='grid'))
    print('<<< TAS >>>')
    print(tabulate(table_tas, tablefmt='grid'))

def showStudentCourses():
    student_c = [
            [st.name for id, st in Student.students.items()],
            ['\n'.join(st.getCourses) for id, st in Student.students.items()],
    ]
    print(tabulate(student_c, tablefmt='grid'))

def showTACourses():
    ta_c = [
            [ta.name for id, ta in TA.TAs.items()],
            ['\n'.join(ta.getCourses) for id, ta in TA.TAs.items()],
        ]
    print(tabulate(ta_c, tablefmt='grid'))

def main():
    print('''

 █████  ██    ██ ████████  ██████      ██████  ███████  ██████  ██ ███████ ████████ ██████   █████  ██████
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██       ██ ██         ██    ██   ██ ██   ██ ██   ██
███████ ██    ██    ██    ██    ██     ██████  █████   ██   ███ ██ ███████    ██    ██████  ███████ ██████
██   ██ ██    ██    ██    ██    ██     ██   ██ ██      ██    ██ ██      ██    ██    ██   ██ ██   ██ ██   ██
██   ██  ██████     ██     ██████      ██   ██ ███████  ██████  ██ ███████    ██    ██   ██ ██   ██ ██   ██


Welcome to Auto-Registrar CLI

Please Select One of The Options Below:

[0] Add a Course
[1] Add a Student
[2] Add a TA
[3] Register a Course for a Student
[4] Register a Course for a TA
[5] Unregister a Course for a Student
[6] Unregister a Course for a TA
[7] Show All Courses
[8] Show All Registered Students
[9] Show All Registered TAs
[10] Show All Courses in Accordance to Students and TAs
[11] Show All Students in Accordance to Registered Courses
[12] Show All TA in Accordance to Registered Courses
[13] Exit''')
    cnd = True
    while cnd:
        user_input = input('\nEnter Command Number,\n(Or Enter 101 to show the list)\n>>> ')
        if int(user_input) == 101:
            print('''[0] Add a Course
[1] Add a Student
[2] Add a TA
[3] Register a Course for a Student
[4] Register a Course for a TA
[5] Unregister a Course for a Student
[6] Unregister a Course for a TA
[7] Show All Courses
[8] Show All Registered Students
[9] Show All Registered TAs
[10] Show All Courses in Accordance to Students and TAs
[11] Show All Students in Accordance to Registered Courses
[12] Show All TA in Accordance to Registered Courses
[13] Exit''')
        elif int(user_input) == 0:
            name = str(input('Enter Course Name >>> '))
            addCourse(name)
        elif int(user_input) == 1:
            name = str(input('Enter Student Name >>> '))
            addStudent(name)
        elif int(user_input) == 2:
            name = str(input('Enter TA Name >>> '))
            addTA(name)
        elif int(user_input) == 3:
            stReg()
        elif int(user_input) == 4:
            taReg()
        elif int(user_input) == 5:
            stUnreg()
        elif int(user_input) == 6:
            taUnreg()
        elif int(user_input) == 7:
            showCourses()
        elif int(user_input) == 8:
            showStudents()
        elif int(user_input) == 9:
            showTAs()
        elif int(user_input) == 10:
            showCourseInfo()
        elif int(user_input) == 11:
            showStudentCourses()
        elif int(user_input) == 12:
            showTACourses()
        elif int(user_input) == 13:
            print('Thanks for using Auto-Registrar CLI...')
            break
        else:
            print('Not in The List!')
        # check_if = input('Another Command? (y/n) >>>> ')
        # if check_if.lower() == 'y':
        #     cnd = True
        # elif check_if.lower() == 'n':
        #     print('Thanks for using Auto-Registrar CLI...')
        #     cnd = False


if __name__ == '__main__':
    main()