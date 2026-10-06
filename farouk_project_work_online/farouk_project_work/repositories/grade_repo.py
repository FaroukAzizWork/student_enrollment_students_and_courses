from data.datastore import WordDatabase
from core.config import GRADES_DB_FILE
from module.entities import Grade

class GradeRepository:
    def __init__(self):
        # الجدول يتكون من 3 أعمدة
        self.db = WordDatabase(GRADES_DB_FILE, ["Student ID", "Course ID", "Grade"])

    def add_grade(self, grade: Grade):
        self.db.add_row([grade.student_id, grade.course_id, grade.value])

    def get_grades_by_student(self, student_id):
        """جلب جميع درجات طالب معين لحساب معدله"""
        grades = []
        for row in self.db.get_all_rows():
            if row[0] == str(student_id):
                grades.append(float(row[2]))  # نحول النص إلى رقم (float)
        return grades