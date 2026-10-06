# cli/menu.py

def show_main_menu():

    #print("\n" + "=" * 40)
    print("      نظام إدارة الطلاب (Student System)      ")
   # print("=" * 40)
    print("1) Register      2) Login       3) Students")
    print("4) Add student   5) Courses     6) Add course")
    print("7) Enroll        8) Add grade   9) Average")
    print("10) Top          11) Logout     12) show courses degres")
    print("0) Exit")
    #print("=" * 40)

    choice = input("> ")
    return choice