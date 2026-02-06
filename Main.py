
import random
import json


class Admin:
    def __init__(self, admin_name):
        self.admin_name = admin_name

    def change_name(self):
        name = input("Enter The Admin Updated Name.")    
        self.admin_name = name
        return f"Admin Updated Name: {self.admin_name}"

class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def role(self):
        print("Enter Your Role ")
        print("Option 1: 1. Administrator")
        print("Option 2: 2. Teacher")
        print("Option 3: 3. Student")
        choose_role = input("")
        user = None
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
        
    def hire_teacher(self, teacher):
        if teacher not in self.students:
            teacher.get_teacher_info_from_input()
            self.teachers.append(teacher)
            print(f"{teacher.teacher_name} Has Been Hired")
            print(teacher.get_info())
        else:
            return "Teacher Already Exists!"


    def fire_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
            return f"{teacher.teacher_name} Has Been Fired!"
        else:
            return "Teacher Couldn't Be Recognized Or Has Already Been Removed"

    

    def add_student(self, student):
        if student not in self.students:
            student.get_student_info_from_input()
            student.get_id()
            self.students.append(student)
            print(f"{student.name} has been added")
            print(student.get_info())
        else:
            return "Student Already Exists!"

    
       

    def remove_student(self, student):
       if student in self.students:
           self.students.remove(student)
           return f"{student.name} Has Been Removed"
       else:
           "Student Couldn't Be Recognized Or Has Already Been Removed"
          


    def search_student(self, student):
        id = input("Enter The Student ID To Find Them ")
        student.id = id
        if student in self.students:
            return student.get_info()
        else:
            return f"{id} Couldn't Be Found. Maybe Incorrect Spelling?"
        

    def show_students(self):
        return self.students
        

    def update_student_info(self, student):
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


    def update_teacher_info(self, teacher):
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
            


class Student:
    def __init__(self, Name, Age: int, Class: int, Grades: list[int], Attendence, average_grade, student_id: set):
        self.name = Name
        self.age = Age
        self.Class = Class
        self.attendence = Attendence
        self.grades = Grades
        self.average_grade = average_grade
        self.id = student_id
        

    def get_id(self):
        # 1-5 For Students
        id = random.randint(1, 5)
        self.id = id

    def get_student_info_from_input(self):
        name = input("Enter The Name Of This Student ").capitalize()
        age = int(input("Enter The Age Of This Student "))
        if age > 18:
            print("Has To Be Under 18")
        else:
            None
        grades = list(map(int, input("Enter Grades (separated by space): ").split()))
        Class = int(input("Enter The Class Of This Student "))
        if Class > 12:
            print(f"{Class} Has To Be From 1-12. Try Again:")
            Class = int(input("Enter The Class Of This Student "))
        else:
            None 

        self.name = name
        self.age = age
        self.grades = grades
        self.Class = Class

    def average(self):
        avg = sum(self.grades) / len(self.grades)
        self.average_grade = avg

    
    

        
        
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Class {self.Class}, Attendence: {self.attendence}, Grades: {self.grades}, Id: {self.id}"
    
    def __str__(self):
        return self.get_info()
    

   

class Teacher:
    def __init__(self, teacher_name, subject, assigned_class, teacher_id=None):
        self.teacher_name = teacher_name
        self.subject = subject
        self.assigned_class = assigned_class
        self.id = teacher_id

    def get_id(self):
        # 6-10 For Teachers
        id = random.randint(6, 10)
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
        return f"Name: {self.teacher_name}, Teaching Subject: {self.subject}, Assigned Class: {self.assigned_class}, Id: {self.id}"  



   
   
   
    

