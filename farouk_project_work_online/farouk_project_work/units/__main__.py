# units/__main__.py

from cli.menu import show_main_menu
from services.authservices import AuthService
from services.student_services import StudentService
from core.exception import UserNotFoundError

from services.courservices import CourseService
course_service = CourseService()

from services.reportservices import ReportService
report_service = ReportService()


def main():
    # 1. تجهيز الخدمات (Services) لتكون جاهزة للاستخدام
    auth_service = AuthService()
    student_service = StudentService()

    # 2. متغير لمعرفة من هو المستخدم الحالي (للتأكد من تسجيل الدخول)
    current_user = None





    # 3. حلقة تكرارية لكي يستمر النظام بالعمل حتى يختار المستخدم "0"
    while True:
        choice = show_main_menu()

        protected_choices = ['3', '4', '5', '6', '7', '8', '9', '10', '11']

        if choice in protected_choices and current_user is None:
            print("\n⛔ عذراً، يجب عليك تسجيل الدخول أولاً للوصول إلى هذه الصلاحيات!")
            continue


        # --- خيار الخروج ---
        if choice == '0':
            print("تم الخروج من النظام. وداعاً!")
            break


            # --- خيار 1: تسجيل حساب جديد (Register) ---
        elif choice == '1':
            print("\n--- إنشاء حساب مستخدم جديد ---")
            user_id = input("أدخل رقم المستخدم الجديد: ")
            name = input("أدخل اسمك: ")
            password = input("أدخل كلمة المرور: ")

            try:
                # نرسل البيانات لل (AuthService) ليطبق الشروط ويحفظ
                auth_service.register(user_id, name, password)
                print(f"تم إنشاء الحساب بنجاح يا {name}! يمكنك الآن اختيار (2) لتسجيل الدخول.")
            except Exception as e:
                print(e)


        # --- خيار تسجيل الدخول ---
        elif choice == '2':
            print("\n--- تسجيل الدخول ---")
            user_id = input("أدخل رقم المستخدم: ")
            password = input("أدخل كلمة المرور: ")

            try:
                # نرسل البيانات للعقل المفكر (AuthService) ليتأكد منها
                current_user = auth_service.login(user_id, password)
                print(f"أهلاً بك يا {current_user.name}! تم تسجيل الدخول بنجاح.")
            except UserNotFoundError as e:
                # إذا فشل الدخول، نطبع الخطأ الأنيق الذي جهزناه
                print(e)

        # --- خيار إضافة طالب ---

                # --- خيار 3: عرض جميع الطلاب ---

        elif choice == '3':
                print("\n--- قائمة الطلاب المسجلين ---")

                # نطلب من الـ Service جلب القائمة
                students = student_service.list_all_students()

                if not students:
                    print("لا يوجد أي طالب مسجل في النظام حالياً.")
                else:
                    for s in students:
                        print(f"رقم الطالب: {s.student_id} | اسم الطالب: {s.name}")



        elif choice == '4':
            print("\n--- إضافة طالب جديد ---")
            student_id = input("أدخل رقم الطالب: ")
            name = input("أدخل اسم الطالب: ")

            try:
                # نرسل البيانات للعقل المفكر (StudentService) ليطبق الشروط ويحفظها
                student_service.add_new_student(student_id, name)
                print("تمت إضافة الطالب وحفظه في ملف الوورد بنجاح!")
            except Exception as e:
                print(e)



                # --- خيار 5: عرض الكورسات (للتأكيد فقط) ---

        elif choice == '5':

            print("\n--- قائمة الكورسات ---")

            courses = course_service.list_all_courses()

            if not courses:

                print("لا توجد كورسات مضافة بعد.")

            else:

                for c in courses:
                    print(f"رقم الكورس: {c.course_id} | اسم الكورس: {c.name}")

            # --- خيار 6: إضافة كورس (Add Course) ---

        elif choice == '6':

            print("\n--- إضافة كورس جديد ---")

            course_id = input("أدخل رقم الكورس: ")

            name = input("أدخل اسم الكورس: ")

            try:

                course_service.add_new_course(course_id, name)

                print(f"تمت إضافة الكورس '{name}' بنجاح!")

            except Exception as e:

                print(e)


        elif choice == '7':
            print("\n--- تسجيل طالب في كورس ---")
            student_id = input("أدخل رقم الطالب: ")
            course_id = input("أدخل رقم الكورس: ")
            try:
                student_service.enroll_student_in_course(student_id, course_id)
                print("تم تسجيل الطالب في الكورس بنجاح!")
            except Exception as e:
                print(e)


        elif choice == '8':
            print("\n--- إضافة درجة لطالب ---")
            student_id = input("أدخل رقم الطالب: ")
            course_id = input("أدخل رقم الكورس: ")
            grade_value = input("أدخل الدرجة: ")
            try:
                report_service.add_grade(student_id, course_id, grade_value)
                print("تم حفظ الدرجة بنجاح!")
            except Exception as e:
                print(e)

        elif choice == '9':
            print("\n--- كشف المعدل ---")
            student_id = input("أدخل رقم الطالب: ")
            avg = report_service.calculate_average(student_id)
            print(f"معدل الطالب هو: {avg}%")


        elif choice == '10':
            print("\n--- الطالب الأول على النظام ---")
            try:
                top_student, highest_avg = report_service.get_top_student()
                print(f"الطالب الأول هو: {top_student.name}")
                print(f"بمعدل: {highest_avg}%")
            except Exception as e:
                print(e)


                # --- خيار 11: تسجيل الخروج (Logout) ---
        elif choice == '11':
                if current_user is None:
                    print("\nأنت لم تسجل الدخول أصلاً!")
                else:
                    print(f"\nإلى اللقاء يا {current_user.name}! تم تسجيل خروجك بنجاح.")
                    # هنا السر: نقوم بمسح بيانات المستخدم من الذاكرة الحالية (الجلسة)
                    current_user = None

        # elif choice == '12':
        #     print("\n--- كشف المعدل ---")
        #     student_id = input("أدخل رقم الطالب: ")
        #     avg = report_service.calculate_average(student_id)
        #     print(f"معدل الطالب هو: {avg}%")


        # --- باقي الخيارات ---
        else:
            print("هذا الخيار قيد التطوير (سنقوم بتعبئة ملفاته لاحقاً) 🚧")


if __name__ == "__main__":
    main()