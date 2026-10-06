from repositories.user_repo import UserRepository
from core.exception import UserNotFoundError


class AuthService:
    def __init__(self):
        # نستدعي المستودع الخاص بالمستخدمين للبحث عنهم
        self.user_repo = UserRepository()

    def login(self, user_id, password):
        """خوارزمية تسجيل الدخول"""
        # 1. نطلب من المستودع البحث عن المستخدم برقم الـ id
        user = self.user_repo.get_user_by_id(user_id)

        # 2. نتحقق: هل المستخدم غير موجود؟ أو كلمة المرور خاطئة؟
        if user is None or user.password != password:
            # هنا نستخدم الخطأ المخصص الذي أنشأناه سابقاً
            raise UserNotFoundError("خطأ: رقم المستخدم أو كلمة المرور غير صحيحة!")

        # 3. إذا كان كل شيء صحيحاً، نرجع كائن المستخدم للواجهة لتعرف من الذي سجل دخوله
        return user

    def register(self, user_id, name, password):
        """خوارزمية إنشاء حساب مستخدم جديد (Register)"""
        # 1. نتحقق أولاً: هل رقم المستخدم مسجل مسبقاً في النظام؟
        existing_user = self.user_repo.get_user_by_id(user_id)

        if existing_user:
            # إذا كان موجوداً، نرفض العملية
            raise Exception("خطأ: رقم المستخدم هذا مسجل مسبقاً! جرب تسجيل الدخول.")

        # 2. إذا لم يكن موجوداً، نستدعي كلاس المستخدم وننشئ كائناً جديداً
        from module.entities import User
        new_user = User(user_id, name, password)

        # 3. نرسله للمستودع ليتم حفظه في ملف وورد الخاص بالمستخدمين
        self.user_repo.add_user(new_user)
        return new_user