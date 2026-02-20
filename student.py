import random


class Student:
    def __init__(
        self,
        Name=None,
        Age=None,
        Class=None,
        Grades=None,
        Attendence=None,
        student_id=None,
    ):
        self.name = Name
        self.age = Age
        self.Class = Class
        self.attendence = Attendence
        # Use empty list when no grades provided
        self.grades = Grades if Grades is not None else []
        self.id = student_id

    def get_id(self):
        # 1-30 For Students
        id = random.randint(1, 30)
        self.id = id

    def get_student_info_from_input(self):
        name = input("Enter The Name Of This Student ").capitalize()
        try:
            age = int(input("Enter The Age Of This Student "))
        except (ValueError, TypeError, NameError):
            print("Has To Be A Number")
            
        while age > 18:
            print("Has To Be Under 18")

        try:
            age = int(input("Enter The Age Of This Student "))
        except (ValueError, TypeError, NameError):
            print("Has To Be A Number")

        grades = list(map(int, input("Enter Grades (separated by space): ").split()))
        try:
            Class = int(input("Enter The Class Of This Student "))
        except (ValueError, TypeError, NameError):
            print("Has To Be A Number")

        while Class > 12:
            print(f"{Class} Has To Be From 1-12. Try Again:")
        try:
            Class = int(input("Enter The Class Of This Student "))
        except (ValueError, TypeError, NameError):
            print("Has To Be A Number")

        self.name = name
        self.age = age
        self.grades = grades
        self.Class = Class
        

    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Class {self.Class}, Attendence: {self.attendence}, Grades: {self.grades}, Id: {self.id}"

    def __str__(self):
        return self.get_info()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.age == other.age
            and self.Class == other.Class
            and self.grades == other.grades
        )