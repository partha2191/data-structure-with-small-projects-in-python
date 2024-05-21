class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "70000")

    def showDetailsFromEngi(self):
        print("Name:", self.name)
        print("Role:", self.age)
        self.showDetails()

    
engg1 = Engineer("Partha", 32)
engg1.showDetailsFromEngi()
