from student import Student
from admin import Admin
from teacher import Teacher
import json

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    
        
    def hire_teacher(self, teacher=None):
        # allow calling without a teacher object; create one if omitted
        if teacher is None:
            teacher = Teacher()

        if teacher not in self.teachers:
            # get info (returns a summary) and show it
            print(teacher.get_teacher_info_from_input())
            self.teachers.append(teacher)
            print(f"{teacher.teacher_name} Has Been Hired")
            print(teacher.get_info())
        else:
            return "Teacher Already Exists!"


    def fire_teacher(self, teacher=None):
        if teacher is None:
            teacher = Teacher()

        if teacher in self.teachers:
            self.teachers.remove(teacher)
            return f"{teacher.teacher_name} Has Been Fired!"
        else:
            return "Teacher Couldn't Be Recognized Or Has Already Been Removed"

    

    def add_student(self, student=None):
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
            "attendance": student.attendence
        }

        file_path = "output.json"
        with open(file_path, "a") as file:
            json.dump(pupil, file)
        return "Student added to database"
        
        

    def remove_student(self, student=None):
       if student is None:
           student = Student()

       if student in self.students:
           self.students.remove(student)
           return f"{student.name} Has Been Removed"
       else:
           "Student Couldn't Be Recognized Or Has Already Been Removed"
        

    def show_students(self):
        return self.students

    def update_student_info(self, student=None):
        if student is None:
            student = Student()
            
        print("Option 1: 1. Update Student Name")
        print("Option 2: 2. Update Student Age")
        print("Option 3: 3. Update Student Grades")
        print("Option 4: 4. Update Student Class")
        print("Option 5: 5. Update Student Attendence")
        choose = input("")

        if choose == "1":
            name = input("Enter Updated Name ")
            student.name = name
            return f"Updated Info: {student.get_info()}"
            
        elif choose == "2":
          try:
            age = int(input("Enter Updated Age "))
            if age > 18:
                return "Has To Be Under 18"
            else:
                student.age = age
                return f"Updated Info: {student.get_info()}"
          except (ValueError, NameError):
              return "Next Time Enter An Age"
            
        elif choose == "3":
            grades = list(map(int, input("Enter Updated Grades (separated by space) ").split()))
            student.grades = grades
            return f"Updated Info: {student.get_info()}"   

        elif choose == "4":
          try:
            Class = int(input("Enter Updated Class "))
            if Class >= 13:
                return f"Class {Class} Is Not Real"
            else:
                student.Class = Class
                return f"Updated Info: {student.get_info()}"
          except (ValueError, NameError):
              return "Next Time Enter A Class From 1-12"

        elif choose == "5":
            attendence = input("Enter Updated Attendence % ")
            student.attendence = attendence
            return f"Updated Info: {student.get_info()}"
        
        else:
            return "Invalid Number Chosen"


    def update_teacher_info(self, teacher=None):
        if teacher is None:
            teacher = Teacher()

        print("Option 1: 1. Update Teacher Name")
        print("Option 2: 2. Update Teacher Assigned Class")
        print("Option 3: 3. Update Teacher Subject")
        choose = input("")

        if choose == "1":
            name = input("Enter Updated Name ")
            teacher.teacher_name = name
            return f"Updated Info: {teacher.get_info()}"
            
        elif choose == "2":
          try:
            assigned_class = int(input("Enter Updated Class "))
            if assigned_class >= 13:
                return f"Class {assigned_class} Is Not Real"
            else:
                teacher.assigned_class = assigned_class
                return f"Updated Info: {teacher.get_info()}"
          except (ValueError, NameError):
              return "Next Time Enter A Class From 1-12"

        elif choose == "3":
            subject = input("Enter Updated Teaching Subject ")
            teacher.subject = subject
            return f"Updated Info: {teacher.get_info()}"
            
        else:
            return "Invalid Number Chosen!"
