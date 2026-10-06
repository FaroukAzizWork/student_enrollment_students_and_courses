


# class User:
#     def __init__(self, usr_mame, usr_id):
#         self.username = usr_mame
#         assert isinstance(usr_id, object)
#         self.userid = usr_id
#
#
#
#
#
# class Student:
#     def __init__(self, stdname, stdid):
#         self.student_name = stdname
#         self.student_id = stdid
#
#
# class Course:
#     def __init__(self, crs_name, hours):
#         self.name = crs_name
#         self.hours = hours
#
#
#
# class registry:
#     def __init__(self, rsg_name, hours):
#         self.name = crs_name
#         self.hours = hours

class User:

    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

class Course:

    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class Grade:

    def __init__(self, student_id, course_id, value):
        self.student_id = student_id
        self.course_id = course_id
        self.value = value
#


