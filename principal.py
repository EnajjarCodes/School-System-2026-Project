from school import School


class Principal(School):
    def __init__(self, principal_name):
        self.p_name = principal_name
        self.students = []
        self.teachers = []

    def change_name(self):
        name = input("Enter The Principal Name ")
        self.p_name = name
        return f"Principal Name: {self.p_name}"