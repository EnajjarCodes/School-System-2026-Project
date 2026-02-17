from school import School

class Admin(School):
    def __init__(self, admin_name):
        self.admin_name = admin_name

    def change_name(self):
        name = input("Enter The Admin Updated Name.")    
        self.admin_name = name
        return f"Admin Updated Name: {self.admin_name}"