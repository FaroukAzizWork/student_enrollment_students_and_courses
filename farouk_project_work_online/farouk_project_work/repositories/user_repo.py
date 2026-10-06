from data.datastore import WordDatabase
from core.config import USERS_DB_FILE
from module.entities import User


class UserRepository:
    def __init__(self):
        # إعداد ملف الوورد الخاص بالمستخدمين
        headers = ["User ID", "Name", "Password"]
        self.db = WordDatabase(USERS_DB_FILE, headers)

    def add_user(self, user: User):
        row_data = [user.user_id, user.name, user.password]
        self.db.add_row(row_data)

    def get_user_by_id(self, user_id):
        all_rows = self.db.get_all_rows()

        for row in all_rows:
            if row[0] == str(user_id):
                return User(user_id=row[0], name=row[1], password=row[2])

        return None