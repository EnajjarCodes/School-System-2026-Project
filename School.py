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


import random

class Student:
    def __init__(self, Name=None, Age=None, Class=None, Grades=None, Attendence=None, average_grade=None, student_id=None):
        self.name = Name
        self.age = Age
        self.Class = Class
        self.attendence = Attendence
        # Use empty list when no grades provided
        self.grades = Grades if Grades is not None else []
        self.average_grade = average_grade
        self.id = student_id
        

    def get_id(self):
        # 1-30 For Students
        id = random.randint(1, 30)
        self.id = id

    def get_student_info_from_input(self):
        name = input("Enter The Name Of This Student ").capitalize()
        age = int(input("Enter The Age Of This Student "))
        while age > 18:
            print("Has To Be Under 18")
            age = int(input("Enter The Age Of This Student "))

        grades = list(map(int, input("Enter Grades (separated by space): ").split()))
        Class = int(input("Enter The Class Of This Student "))
        while Class > 12:
            print(f"{Class} Has To Be From 1-12. Try Again:")
            Class = int(input("Enter The Class Of This Student "))
        
        self.name = name
        self.age = age
        self.grades = grades
        self.Class = Class
        # Return a summary string so callers can print the entered info
        return self.get_info()

    def average(self):
        if not self.grades:
            self.average_grade = None
            return None
        avg = sum(self.grades) / len(self.grades)
        self.average_grade = avg
        return avg
    
    
    def get_academic_status(self):
        if self.average_grade >= 90:
            print("Final Score: A")
        elif self.average_grade >= 80:
            print("Final Score: B")
        elif self.average_grade >= 70:
            print("Final Score: C")
        elif self.average_grade >= 60:
            print("Final Score: D")
        else:
            print("Final Score: F") 


    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Class {self.Class}, Attendence: {self.attendence}, Grades: {self.grades}, Id: {self.id}"
    
    def __str__(self):
        return self.get_info()


class Teacher:
    def __init__(self, teacher_name, subject, assigned_class, teacher_id=set):
        self.teacher_name = teacher_name
        self.subject = subject
        self.assigned_class = assigned_class
        self.id = teacher_id

    def get_id(self):
        # 31, 60  For Teachers
        id = random.randint(31, 60)
        self.id = id

    def get_teacher_info_from_input(self):
        name = input("Enter The Name Of This Teacher ").capitalize()
        Class = int(input("Enter The Class Of This Teacher "))
        if Class > 12:
            print(f"{Class} Has To Be From 1-12. Try Again:")
            Class = int(input("Enter The Class Of This Student"))
        else:
            None 

        self.teacher_name = name
        self.assigned_class = Class
        # Return a summary string so callers can print the entered info
        return self.get_info()

    def change_student_attendance(self, student):
      try:
        sAttendance = int(input("Enter This Student's Attendance % "))
        if sAttendance > 100:
            return "Has To Be Under 100"
        else:
           student.attendence = sAttendance
           return student.get_info()
      except (NameError, TypeError, ValueError):
        return "Enter A Number Next Time"
      
    def change_class(self):
      try:
        teaching_class = int(input("Enter The Class You Would Like To Teach "))
      except Exception:
          return "Invalid Input!"
      while teaching_class > 12:
          return "Invalid Class Chosen! Try Again"
      try:
          teaching_class = int(input("Enter The Class You Would Like To Teach "))
      except Exception:
            print("Invalid Input!")

      self.assigned_class = teaching_class

    def choose_subject(self):
        choose_subject = input("Select The Subject You Would Like To Teach: ").capitalize()
        if choose_subject in ["Maths", "Math", "Mathematics",
                             "English",
                             "Business",
                             "Geography",
                             "History",
                             "Biology", "Chemistry", "Physics", "Science",
                             "ICT", "Computer Science", "Technology"]:

                self.subject = choose_subject
                return f"Teaching Subject Is Now {self.subject}"
        else:
            return f"{choose_subject} Couldn't Be Found. Maybe Spelling Is Incorrect"

    def get_info(self):
        return f"Name: Mr.{self.teacher_name}, Teaching Subject: {self.subject}, Assigned Class: {self.assigned_class}, Id: {self.id}"


class Admin(School):
    def __init__(self, admin_name):
        self.admin_name = admin_name

    def change_name(self):
        name = input("Enter The Admin Name ")    
        self.admin_name = name
        return f"Admin Name: {self.admin_name}"


class Menu:

    def role(self):
        print("Enter Your Role ")
        print("Option 1: 1. Administrator")
        print("Option 2: 2. Teacher")
        print("Option 3: 3. Student")
        choose_role = input("")

        if choose_role == "1":
            user = Admin(admin_name="Unknown")
            print(user.change_name())
        elif choose_role == "2":
            user = Teacher(teacher_name="Unknown", subject="Unknown", assigned_class="Unknown", teacher_id="Unknown")
            print(user.get_teacher_info_from_input())
            print(user.get_info())
        elif choose_role == "3":
            user = Student(Name="Unknown", Age="Unknown", Class="Unknown", Grades="Unknown", Attendence="Unknown", average_grade="Unknown", student_id="Unknown")
            print(user.get_student_info_from_input())
            print(user.get_info())
        else:
            return f"Invalid Number Chosen"
    
        while isinstance(user, Admin):
            print(f"Welcome Mr.{user.admin_name}. What Would You Like To Do")
            print("Option 1: Hire Teacher")
            print("Option 2: Fire Teacher")
            print("Option 3: Add Student")
            print("Option 4: Expel Student")
            print("Option 5: Update Teacher Info")
            print("Option 6: Update Student Info")
            print("Option 7: Exit")
            admin_choose = input("")

            if admin_choose == "1":
                print(user.hire_teacher())
            elif admin_choose == "2":
                print(user.fire_teacher())
            elif admin_choose == "3":
                print(user.add_student())
            elif admin_choose == "4":
                print(user.remove_student())
            elif admin_choose == "5":
                print(user.update_teacher_info())
            elif admin_choose == "6":
                print(user.update_student_info())
            elif admin_choose == "7":
                print(f"Bye Mr.{user.admin_name}")
                break

        while isinstance(user, Teacher):
           print(f"Welcome Mr.{user.teacher_name} What Would You Like To Do")
           print("Option 1: Change/Choose A Class")
           print("Option 2: Change/Choose A Subject")
           print("Option 3: Change Student Attendance")
           print("Option 4: Change Info")
           print("Option 5: Show Info")
           print("Option 6: Exit")
           teacher_choose = input("")

           if teacher_choose == "1":
               print(user.change_class())
           elif teacher_choose == "2":
               print(user.choose_subject())
           elif teacher_choose == "3":
               print(user.change_student_attendance)
           elif teacher_choose == "4":
               print(user.get_teacher_info_from_input())
           elif teacher_choose == "5":
               print(user.get_info())
           elif teacher_choose == "6":
               print(f"Bye Mr.{user.teacher_name}")
               break
           else:
               print("Invalid Number Chosen")

        while isinstance(user, Student):
            print("Hi")
            break

menu = Menu()
menu.role()