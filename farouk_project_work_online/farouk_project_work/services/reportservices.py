from repositories.grade_repo import GradeRepository
from repositories.enrollment_repo import EnrollmentRepository
from repositories.student_repo import StudentRepository
from module.entities import Grade


class ReportService:
    def __init__(self):
        self.grade_repo = GradeRepository()
        self.enroll_repo = EnrollmentRepository()
        self.student_repo = StudentRepository()

    def add_grade(self, student_id, course_id, grade_value):
        """إضافة درجة مع التأكد من تسجيل الطالب"""
        # المنطق: لا يمكن إعطاء درجة لطالب غير مسجل في الكورس!
        if not self.enroll_repo.is_enrolled(student_id, course_id):
            raise Exception("خطأ: الطالب غير مسجل في هذا الكورس!")

        new_grade = Grade(student_id, course_id, grade_value)
        self.grade_repo.add_grade(new_grade)

    def calculate_average(self, student_id):
        """حساب المعدل"""
        grades = self.grade_repo.get_grades_by_student(student_id)
        if not grades:  # إذا لم يكن لديه درجات
            return 0.0

        # مجموع الدرجات قسمة عددها
        return sum(grades) / len(grades)

    def get_top_student(self):
        """إيجاد الطالب الأول (صاحب أعلى معدل)"""
        all_students = self.student_repo.get_all_students()
        if not all_students:
            raise Exception("لا يوجد طلاب في النظام!")

        top_student = None
        highest_avg = -1.0

        for student in all_students:
            avg = self.calculate_average(student.student_id)
            if avg > highest_avg:
                highest_avg = avg
                top_student = student

        return top_student, highest_avg