import json
import time
import random


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def hire_teacher(self, teacher=None):
        from teacher import Teacher
        # allow calling without a teacher object; create one if omitted
        if teacher is None:
            teacher = Teacher()

        if teacher not in self.teachers:
            # get info (returns a summary) and show it
            print(teacher.get_teacher_info_from_input())
            teacher.get_id()
            self.teachers.append(teacher)
            print(teacher.get_info())

            teach = {
                "id": teacher.id,
                "name": teacher.teacher_name,
                "teaching_class": teacher.assigned_class,
                "teaching_subject": teacher.subject,
            }

            file_path = "output.json"
            with open(file_path, "a") as file:
                json.dump(teach, file, indent=4)
            return "Teacher added to database"
        else:
            return "Teacher Already Exists!"

    def fire_teacher(self, teacher=None):
        from teacher import Teacher
        if teacher is None:
            teacher = Teacher()
            print(teacher.get_teacher_info_from_input())

        if teacher in self.teachers:
            self.teachers.remove(teacher)
            return f"{teacher.teacher_name} Has Been Fired!"
        else:
            return "Teacher Couldn't Be Recognized Or Has Already Been Removed"

    def add_student(self, student=None):
        from student import Student
        # If caller didn't provide a Student, create an empty one
        if student is None:
            student = Student()

        print(student.get_student_info_from_input())
        student.get_id()
        self.students.append(student)
        print(f"{student.name} has been added")
        print(student.get_info())

        pupil = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "grades": student.grades,
            "attendance": student.attendence,
        }

        file_path = "output.json"

        with open(file_path, "a") as file:

            json.dump(pupil, file)

        return "Student added to database"

    def remove_student(self, student=None):
        from student import Student
        if student is None:
            student = Student()
            print(student.get_student_info_from_input())

        if student in self.students:
            self.students.remove(student)
            return f"{student.name} Has Been Removed"
        else:
            return "Student Couldn't Be Recognized Or Has Already Been Removed"

    def show_students(self):
        if self.students is not []:
            for student in self.students:
                print(student.get_info())
        else:
            print("No Students Found In Database")

    def show_teachers(self):
        if self.teachers is not []:
            for teacher in self.teachers:
                print(teacher.get_info())
        else:
            print("No Teachers Found In Database")


    def update_student_info(self, student=None):
        if not self.students:
            print("No Students In Database To Work With")
            return

        print("Which Student Would You Like To Update:")
        for i, student in enumerate(self.students, start=1):
            print(
                f"{i}. Student: Name: {student.name}, Age: {student.age}, ID: {student.id}, Class: {student.Class}"
            )

        try:
            choose_student = int(input("Enter the number of the student: ").strip())
            if 1 <= choose_student <= len(self.students):
                selected_student = self.students[
                    choose_student - 1
                ]  # Subtract 1 for 0-based index
            else:
                print("Invalid number. Please choose a valid option.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        print("Option 1: 1. Update Student Name")
        print("Option 2: 2. Update Student Age")
        print("Option 3: 3. Update Student Grades")
        print("Option 4: 4. Update Student Class")
        print("Option 5: 5. Update Student Attendance")
        choose = input("").strip()

        if choose == "1":
            name = input("Enter Updated Name ").capitalize()
            selected_student.name = name
            print(f"Updated Info: {selected_student.get_info()}")
        elif choose == "2":
            try:
                age = int(input("Enter Updated Age "))
            except ValueError:
                print("Has To Be A Number!")

                while age > 18:
                    print("Has To Be Under 18! Try Again")
                try:
                    age = int(input("Enter Updated Age "))
                except (ValueError, TypeError, NameError):
                    print("Has To Be A Number")
                else:
                    selected_student.age = age
                    print(f"Updated Info: {selected_student.get_info()}")

        elif choose == "3":
            grades = list(
                map(int, input("Enter Updated Grades (separated by space) ").split())
            )
            selected_student.grades = grades
            print(f"Updated Info: {selected_student.get_info()}")
        elif choose == "4":
            try:
                Class = int(input("Enter Updated Class "))
                while Class > 12:
                    print("Class Has To Be 12 Or Under! Try Again")
                try:
                    Class = int(input("Enter Updated Class "))
                except (ValueError, TypeError, NameError):
                    print("Has To Be A Number")
                else:
                    selected_student.Class = Class
                    print(f"Updated Info: {selected_student.get_info()}")
            except ValueError:
                print("Has To Be A Number!")
        elif choose == "5":
            try:
                attendance = int(input("Enter Updated Attendance % "))
                while attendance > 100:
                    print("Has To Be 100% Or Under! Try Again")
                try:
                    attendance = int(input("Enter Updated Attendance % "))
                except (ValueError, TypeError, NameError):
                    print("Has To Be A Number")
                else:
                    selected_student.attendence = attendance
                    print(f"Updated Info: {selected_student.get_info()}")
            except ValueError:
                print("Has To Be A Number!")
        else:
            print("Invalid Number Chosen")

    def update_teacher_info(self, teacher=None):
        from teacher import Teacher
        if teacher is None:
            teacher = Teacher()
            print(teacher.get_teacher_info_from_input())
            self.teachers.append(teacher)

        print("Option 1: 1. Update Teacher Name")
        print("Option 2: 2. Update Teacher Assigned Class")
        print("Option 3: 3. Update Teacher Subject")
        choose = input("").strip()

        if choose == "1":
            name = input("Enter Updated Name ")
            teacher.teacher_name = name
            return f"Updated Info: {teacher.get_info()}"

        elif choose == "2":
            try:
                assigned_class = int(input("Enter Updated Class "))
            except (ValueError, NameError):
                print("Has To Be A Number!")

                while assigned_class > 12:
                    print("Class Has To Be Over 12! Try Again")
                    try:
                        assigned_class = int(input("Enter Updated Class "))
                    except (ValueError, NameError):
                        print("Has To Be A Number!")
                else:
                    teacher.assigned_class = assigned_class
                    return f"Updated Info: {teacher.get_info()}"
            

        elif choose == "3":
            subject = input("Enter Updated Teaching Subject ")
            teacher.subject = subject
            return f"Updated Info: {teacher.get_info()}"

        else:
            return "Invalid Number Chosen!"
