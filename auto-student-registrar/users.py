from .algorithms.graph import di
from .courses import Course


class Student:
    students = dict()
    next_id = 0
    course_list = di()

    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        Student.course_list.addNode(self)

    def __hash__(self):
        return self.id

    @staticmethod
    def add(name):
        cur_student = Student(Student.next_id, name)
        Student.students[Student.next_id] = cur_student
        Student.next_id += 1
        return cur_student

    @property
    def regCourse(self):
        print('<< LIST OF COURSES >>')
        for course in range(len(Course.getAll())):
            print(f'[{course}]', Course.getAll()[course])
        course_id = int(input('Which to register >>> '))
        for id, course in Course.courses.items():
            if (
                self,
                course,
            ) not in Student.course_list.getEdges and course.id == course_id:
                Student.course_list.addEdge(self, course)
                Course.courses_list.addEdge(course, self)

    # @property
    # def unregCourse(self):
    #     reg_crs = []
    #     st = []
    #     for st, course in Student.course_list.getEdges:
    #         if st == self:
    #             reg_crs.append(Course.getCName(course))
    #     print('<< LIST OF REGISTERED COURSES >>')
    #     for course in range(len(reg_crs)):
    #         print(f'[{course}]', reg_crs[course])
    #     course_id = int(input('Which to unregister >>> '))
    #     for st, course in Student.course_list.getEdges:
    #         if course.name == reg_crs[course_id]:
    #             Student.course_list.removeEdge(self, course)
    #             Course.courses_list.removeEdge(course, self)

    @property
    def unregCourse(self):
        st = []
        reg_crs = [
            Course.getCName(course)
            for st, course in Student.course_list.getEdges
            if st == self
        ]

        print('<< LIST OF REGISTERED COURSES >>')
        for course in range(len(reg_crs)):
            print(f'[{course}]', reg_crs[course])
        course_id = int(input('Which to unregister >>> '))
        for st, course in Student.course_list.getEdges:
            if course.name == reg_crs[course_id]:
                Student.course_list.removeEdge(self, course)
                Course.courses_list.removeEdge(course, self)

    @property
    def getCourses(self) -> list:
        return [
            Course.getCName(course)
            for student, course in Student.course_list.getEdges
            if student == self
        ]

    @staticmethod
    def getNames():
        return [student.name for id, student in Student.students.items()]
    
    @staticmethod
    def getCName(obj):
        for id, student in Student.students.items():
            if obj == student:
                return student.name


class TA:
    TAs = dict()
    next_id = 0
    course_list = di()

    def __init__(self, ta_id, name):
        self.id = ta_id
        self.name = name
        TA.course_list.addNode(self)

    def __hash__(self):
        return self.id

    @staticmethod
    def add(name):
        cur_ta = TA(TA.next_id, name)
        TA.TAs[TA.next_id] = cur_ta
        TA.next_id += 1
        return cur_ta

    @property
    def regCourse(self):
        print('<< LIST OF COURSES >>')
        for course in range(len(Course.getAll())):
            print(f'[{course}]', Course.getAll()[course])
        course_id = int(input('Which to register >>> '))
        for id, course in Course.courses.items():
            if (
                self,
                course,
            ) not in TA.course_list.getEdges and course.id == course_id:
                TA.course_list.addEdge(self, course)
                Course.courses_list.addEdge(course, self)
    
    @property
    def unregCourse(self):
        reg_crs = [
            Course.getCName(course)
            for ta, course in TA.course_list.getEdges
            if ta == self
        ]

        print('<< LIST OF REGISTERED COURSES >>')
        for course in range(len(reg_crs)):
            print(f'[{course}]', reg_crs[course])
        course_id = int(input('Which to unregister >>> '))
        for ta, course in TA.course_list.getEdges:
            if course.name == reg_crs[course_id]:
                TA.course_list.removeEdge(self, course)
                Course.courses_list.removeEdge(course, self)

    @property
    def getCourses(self) -> list:
        return [
            Course.getCName(course)
            for ta, course in TA.course_list.getEdges
            if ta == self
        ]

    @staticmethod
    def getNames():
        return [ta.name for id, ta in TA.TAs.items()]
    
    @staticmethod
    def getCName(obj):
        for id, ta in TA.TAs.items():
            if obj == ta:
                return ta.name
