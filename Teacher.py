import random

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