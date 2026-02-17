from school import School
from admin import Admin
from student import Student
from teacher import Teacher

class Menu:
    def __init__(self, user):
        self.user = user

    def role(self):
        print("Enter Your Role ")
        print("Option 1: 1. Administrator")
        print("Option 2: 2. Teacher")
        print("Option 3: 3. Student")
        choose_role = input("")
        if choose_role == "1":
            self.user = Admin(admin_name="Unknown")
            print(self.user.change_name())
        elif choose_role == "2":
            self.user = Teacher(teacher_name="Unknown", subject="Unknown", assigned_class="Unknown", teacher_id="Unknown")
            print(self.user.get_teacher_info_from_input())
            print(self.user.get_info())
        elif choose_role == "3":
            self.user = Student(Name="Unknown", Age="Unknown", Class="Unknown", Grades="Unknown", Attendence="Unknown", average_grade="Unknown", student_id="Unknown")
            print(self.user.get_student_info_from_input())
            print(self.user.get_info())
        else:
            return f"Invalid Number Chosen"
    
        while self.user == Admin:
            print(f"Welcome {self.user.admin_name}. What Would You Like To Do")
            print("Option 1: Hire Teacher")
            print("Option 2: Fire Teacher")
            print("Option 3: Add Student")
            print("Option 4: Expel Student")
            print("Option 5: Update Teacher Info")
            print("Option 6: Update Student Info")
            print("Option 7: Exit")
            choose = input("")

            if choose == "1":
                print(self.user.hire_teacher())
            elif choose == "2":
                print(self.user.fire_teacher())
            elif choose == "3":
                print(self.user.add_student())
            elif choose == "4":
                print(self.user.remove_student())
            elif choose == "5":
                print(self.user.update_teacher_info())
            elif choose == "6":
                print(self.user.update_student_info())
            elif choose == "7":
                print(f"Bye Mr.{self.user.admin_name}")
                break

menu = Menu(user="user")
print(menu.role())