from data.datastore import WordDatabase
from core.config import COURSES_DB_FILE
from module.entities import Course

class CourseRepository:
    def __init__(self):
        self.db = WordDatabase(COURSES_DB_FILE, ["Course ID", "Name"])

    def add_course(self, course: Course):
        self.db.add_row([course.course_id, course.name])

    def get_course_by_id(self, course_id):
        for row in self.db.get_all_rows():
            if row[0] == str(course_id):
                return Course(course_id=row[0], name=row[1])
        return None

    def get_all_courses(self):
        """جلب جميع الكورسات لعرضها"""
        courses = []
        for row in self.db.get_all_rows():
            courses.append(Course(course_id=row[0], name=row[1]))
        return courses