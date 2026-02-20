import random


class Student:
    def __init__(
        self,
        Name=None,
        Age=None,
        Class=None,
        Grades=None,
        Attendence=None,
        average_grade=float,
        student_id=None,
    ):
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
        return self.average_grade

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

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (
            self.name == other.name
            and self.age == other.age
            and self.Class == other.Class
            and self.grades == other.grades
        )