import random
from student import Student
from school import School


class Teacher:
    def __init__(
        self, teacher_name=None, subject=None, assigned_class=None, teacher_id=None
    ):
        self.teacher_name = teacher_name
        self.subject = subject
        self.assigned_class = assigned_class
        self.id = teacher_id

    def get_id(self):
        # 31, 60  For Teachers
        id = random.randint(31, 60)
        self.id = id

    def get_teacher_info_from_input(self):
      try:
        Class = int(input("Enter The Class Of This Teacher "))
        name = input("Enter The Name Of This Teacher ").capitalize()
      except (ValueError, NameError, TypeError):
        print("Has To Be A Number")

        while Class > 12:
            print(f"{Class} Has To Be From 1-12. Try Again:")
        try:
            Class = int(input("Enter The Class Of This Student"))
        except (ValueError, NameError, TypeError):
            print("Has To Be A Number")

        self.teacher_name = name
        self.assigned_class = Class

    def change_student_attendance(self, student=None):
        if student is None:
            student = Student()
            print(student.get_student_info_from_input())
            

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
      except (ValueError, TypeError, NameError):
        print("Has To Be A Number")

        while teaching_class > 12:
            print("Class Has To Be 12 Or Under! Try Again")
      try:
            teaching_class = int(input("Enter The Class You Would Like To Teach "))
      except (ValueError, TypeError, NameError):
        print("Has To Be A Number")

      else:
          self.assigned_class = teaching_class
          print(f"Teaching Class Is Now {self.assigned_class}")

    def choose_subject(self):
        choose_subject = input(
            "Select The Subject You Would Like To Teach: "
        ).capitalize()
        if choose_subject in [
            "Maths".capitalize(),
            "Math".capitalize(),
            "Mathematics".capitalize(),
            "English".capitalize(),
            "Business".capitalize(),
            "Geography".capitalize(),
            "History".capitalize(),
            "Biology".capitalize(),
            "Chemistry".capitalize(),
            "Physics".capitalize(),
            "Science".capitalize(),
            "ICT".upper(),
            "Computer Science".capitalize(),
            "Technology".capitalize(),
        ]:
            self.subject = choose_subject
            return f"Teaching Subject Is Now {self.subject}"
        else:
            return f"{choose_subject} Couldn't Be Found. Maybe Spelling Is Incorrect"

    def get_info(self):
        return f"Name: Mr.{self.teacher_name}, Teaching Subject: {self.subject}, Assigned Class: {self.assigned_class}, Id: {self.id}"

    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return False
        return (
            self.teacher_name == other.teacher_name
            and self.assigned_class == other.assigned_class
        )