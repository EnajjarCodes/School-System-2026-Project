import time


class Menu:

    def role(self):
        from school import School
        from student import Student
        from teacher import Teacher
        from principal import Principal
        print("Enter Your Role ")
        print("Option 1: 1. Principal")
        print("Option 2: 2. Teacher")
        print("Option 3: 3. Student")
        choose_role = input("").strip()

        if choose_role == "1":
            user = Principal(principal_name="Unknown")
            print(user.change_name())
        elif choose_role == "2":
            user = Teacher(
                teacher_name="Unknown",
                subject="Unknown",
                assigned_class="Unknown",
                teacher_id="Unknown",
            )
            print(user.get_id())
            print(user.get_teacher_info_from_input())
        elif choose_role == "3":
            user = Student(
                Name="Unknown",
                Age="Unknown",
                Class="Unknown",
                Grades="Unknown",
                Attendence="Unknown",
                average_grade="Unknown",
                student_id="Unknown",
            )
            print(user.get_student_info_from_input())
            user.get_id()
            print(user.get_info())
        else:
            return f"Invalid Number Chosen"

        while isinstance(user, Principal):
            print(f"Welcome Mr.{user.p_name}. What Would You Like To Do")
            print("Option 1: Hire Teacher")
            print("Option 2: Fire Teacher")
            print("Option 3: Add Student")
            print("Option 4: Expel Student")
            print("Option 5: Update Teacher Info")
            print("Option 6: Update Student Info")
            print("Option 7: Show Teachers")
            print("Option 8: Show Students")
            print("Option 9: Exit")
            admin_choose = input("").strip()

            if admin_choose == "1":
                print(user.hire_teacher())
                time.sleep(2)
            elif admin_choose == "2":
                print(user.fire_teacher())
                time.sleep(2)
            elif admin_choose == "3":
                print(user.add_student())
                time.sleep(2)
            elif admin_choose == "4":
                print(user.remove_student())
                time.sleep(2)
            elif admin_choose == "5":
                print(user.update_teacher_info())
                time.sleep(2)
            elif admin_choose == "6":
                print(user.update_student_info())
                time.sleep(2)
            elif admin_choose == "7":
                print(user.show_teachers())
            elif admin_choose == "8":
                print(user.show_students())
            elif admin_choose == "9":
                print(f"Bye Mr.{user.p_name}")
                break
            else:
                print("Invalid Number Chosen!")

        while isinstance(user, Teacher):
            print(f"Welcome Mr.{user.teacher_name} What Would You Like To Do")
            print("Option 1: Change/Choose A Class")
            print("Option 2: Change/Choose A Subject")
            print("Option 3: Change Student Attendance")
            print("Option 4: Change Info")
            print("Option 5: Show Info")
            print("Option 6: Exit")
            teacher_choose = input("").strip()

            if teacher_choose == "1":
                print(user.change_class())
                time.sleep(3)
            elif teacher_choose == "2":
                print(user.choose_subject())
                time.sleep(3)
            elif teacher_choose == "3":
                print(user.change_student_attendance())
                time.sleep(3)
            elif teacher_choose == "4":
                print(user.get_teacher_info_from_input())
                time.sleep(3)
            elif teacher_choose == "5":
                print(user.get_info())
                time.sleep(4)
            elif teacher_choose == "6":
                print(f"Bye Mr.{user.teacher_name}")
                time.sleep(4)
                break
            else:
                print("Invalid Number Chosen")

        while isinstance(user, Student):
            print(f"Welcome {user.name} What Would You Like To Do")
            print("Option 1: Show Student Info")
            print("Option 2: Update Student Info")
            print("Option 3: Exit")
            student_choose = input("").strip()

            if student_choose == "1":
                print(user.get_info())
                time.sleep(5)
            elif student_choose == "2":
                print(user.get_student_info_from_input())
                time.sleep(3)
            elif student_choose == "3":
                print(f"Bye {user.name}")
                time.sleep(1.5)
                break
            else:
                print("Invalid Number Chosen!")