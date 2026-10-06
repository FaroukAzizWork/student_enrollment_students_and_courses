from repositories.course_repo import CourseRepository
from module.entities import Course


class CourseService:
    def __init__(self):
        self.course_repo = CourseRepository()

    def add_new_course(self, course_id, name):
        if self.course_repo.get_course_by_id(course_id):
            raise Exception(f"الكورس رقم {course_id} موجود مسبقاً!")

        new_course = Course(course_id, name)
        self.course_repo.add_course(new_course)

    def list_all_courses(self):
        return self.course_repo.get_all_courses()