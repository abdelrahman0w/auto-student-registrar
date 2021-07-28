from .algorithms.graph import di


class Course:
    courses = dict()
    next_id = 0
    courses_list = di()

    def __init__(self, Course_id, name):
        self.id = Course_id
        self.name = name
        Course.courses_list.addNode(self)

    def __hash__(self):
        return self.id

    @staticmethod
    def add(name):
        cur_Course = Course(Course.next_id, name)
        Course.courses[Course.next_id] = cur_Course
        Course.next_id += 1
        return cur_Course

    @staticmethod
    def getAll():
        return [course.name for id, course in Course.courses.items()]
    
    @staticmethod
    def getCName(course_obj):
        for id, course in Course.courses.items():
            if course_obj == course:
                return course.name
