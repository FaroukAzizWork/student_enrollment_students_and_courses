from data.datastore import WordDatabase
from core.config import STUDENTS_DB_FILE
from module.entities import Student


class StudentRepository:
    def __init__(self):
        # هنا نربط هذا المستودع بملف الوورد الخاص بالطلاب ونحدد الأعمدة
        headers = ["Student ID", "Name"]
        self.db = WordDatabase(STUDENTS_DB_FILE, headers)

    def add_student(self, student: Student):
        """تحويل كائن الطالب إلى صف من البيانات لحفظه في الوورد"""
        row_data = [student.student_id, student.name]
        self.db.add_row(row_data)

    def get_student_by_id(self, student_id):
        """البحث عن طالب معين في الوورد وإرجاعه ككائن Student"""
        all_rows = self.db.get_all_rows()



        for row in all_rows:
            if row[0] == str(student_id):  # العمود الأول هو الـ ID
                return Student(student_id=row[0], name=row[1])

        return None  # إذا لم يجد الطالب


    def get_all_students(self):
        """جلب جميع الطلاب لحساب معدلاتهم أو عرضهم"""
        from module.entities import Student  # تأكد من استدعاء الكيان إذا لم يكن مستدعى في الأعلى

        students = []
        for row in self.db.get_all_rows():
            # row[0] هو رقم الطالب، و row[1] هو اسمه
            students.append(Student(student_id=row[0], name=row[1]))

        return students