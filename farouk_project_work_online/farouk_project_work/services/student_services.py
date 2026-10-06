from repositories.student_repo import StudentRepository
from module.entities import Student
from repositories.enrollment_repo import EnrollmentRepository
from repositories.course_repo import CourseRepository


class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()

    def enroll_student_in_course(self, student_id, course_id):
        enroll_repo = EnrollmentRepository()
        course_repo = CourseRepository()

        # 1. التحقق من وجود الطالب (باستخدام الدالة التي بنيناها سابقاً)
        if not self.student_repo.get_student_by_id(student_id):
            raise Exception("الطالب غير موجود!")

        # 2. التحقق من وجود الكورس
        if not course_repo.get_course_by_id(course_id):
            raise Exception("الكورس غير موجود!")

        # 3. التحقق من عدم تكرار التسجيل
        if enroll_repo.is_enrolled(student_id, course_id):
            raise Exception("الطالب مسجل في هذا الكورس مسبقاً!")

        # 4. إذا نجحت كل الشروط، قم بتسجيله
        enroll_repo.add_enrollment(student_id, course_id)


        # أضف هذه الدالة داخل كلاس StudentService
    def list_all_students(self):
            """جلب جميع الطلاب لعرضهم في الواجهة"""
            return self.student_repo.get_all_students()

    def add_new_student(self, student_id, name):
        """خوارزمية إضافة طالب جديد"""
        # 1. نتحقق أولاً: هل يوجد طالب يحمل نفس الرقم مسبقاً؟
        existing_student = self.student_repo.get_student_by_id(student_id)

        if existing_student:
            # إذا كان موجوداً، نوقف العملية ونرسل خطأ
            raise Exception(f"الطالب صاحب الرقم {student_id} مسجل في النظام مسبقاً!")

        # 2. إذا لم يكن موجوداً، نقوم بإنشاء الكائن (Entity)
        new_student = Student(student_id, name)

        # 3. نرسله للمستودع ليتم حفظه في ملف الوورد
        self.student_repo.add_student(new_student)



        return new_student