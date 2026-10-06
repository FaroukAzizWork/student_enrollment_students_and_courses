# core/exception.py

class UserNotFoundError(Exception):
    """خطأ يظهر عندما يحاول المستخدم تسجيل الدخول ببيانات غير موجودة"""
    pass

class StudentAlreadyEnrolledError(Exception):
    """خطأ يظهر عندما نحاول تسجيل طالب في كورس هو مسجل فيه مسبقاً"""
    pass

class DataStoreError(Exception):
    """خطأ يظهر في حال حدوث مشكلة أثناء القراءة أو الكتابة في ملف الوورد"""
    pass