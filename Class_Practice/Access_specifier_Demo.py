""""
An object's attributes may or may not be visible outside the class definition.
You need to name attributes with a double underscore prefix,
and those attributes then are not be directly visible to outsiders
"""

class Employee:
    __count=0;  # private variable throw error AttributeError: 'Employee' object has no attribute '__count'.

    def __init__(self):
        Employee.__count=Employee.__count+1
    def display(self):
        print("The number of employees",Employee.__count)
emp=Employee()
emp2=Employee()
try:
    print(emp.__count)
finally:
    emp.display()