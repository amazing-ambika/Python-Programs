# Python program to demonstrate OOP Inheritance
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


# Driver code
emp = Person("Tina", 2)  # An Object of Person
emp.Display()

# child class
class Emp(Person):

    def Print(self):
        print("Parent Class Emp class called")


Emp_details = Emp("Sarah", 12)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()