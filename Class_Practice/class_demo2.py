class Employee:

    empCount = 0
    def __init__(self,name,age):
        self.name= name
        self.age=age
        Employee.empCount += 1

    def display_empCount(self):
        print("Total Employee Count:",Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name, "Age:",self.age)

#Creating Instance Objects:

emp1=Employee("Amit",25)   #This would create first object of Employee class
emp2=Employee("Raj",30)    #This would create second object of Employee class

#Accessing Attributes:
emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" % Employee.empCount)

"""
OUTPUT:
Name: Amit Age: 25
Name: Raj Age: 30
Total Employee 2
"""
