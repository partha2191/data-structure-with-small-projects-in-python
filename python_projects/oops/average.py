# Create a student class that takes name & marks of 3 subjects 
# as arguments in constructor. Then create a method to print the average.

# Defining Blueprint of a Student class
class Student:
    # Default constructor - Automatically runs when new object is being created
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(self)

    # Parameterized constructor
    def get_avg(self):
        print(self)
        sum = 0
        for mark in self.marks:
            sum += mark
        print("Hi", self.name, "your avg score is:", sum/3)

# Creating Student Objects by calling the Student class
s1 = Student("Partha", [99, 98, 97]) 
s1.get_avg() 

s1.name = "ironman"
s1.get_avg()



