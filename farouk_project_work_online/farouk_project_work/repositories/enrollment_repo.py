from data.datastore import WordDatabase
from core.config import ENROLLMENTS_DB_FILE

class EnrollmentRepository:
    def __init__(self):
        # جدول وسيط يربط الطالب بالكورس
        self.db = WordDatabase(ENROLLMENTS_DB_FILE, ["Student ID", "Course ID"])

    def add_enrollment(self, student_id, course_id):
        self.db.add_row([student_id, course_id])

    def is_enrolled(self, student_id, course_id):
        """التحقق مما إذا كان الطالب مسجلاً مسبقاً في هذا الكورس"""
        for row in self.db.get_all_rows():
            if row[0] == str(student_id) and row[1] == str(course_id):
                return True
        return False