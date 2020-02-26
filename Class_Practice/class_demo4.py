"""
Built-In Class Attributes:
"""

class Person:
    'This is Person class'
    PerCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.PerCount += 1

    def displayCount(self):
        print("Total Employee %d" % Person.PerCount)

    def displayPerson(self):
        print("Name : ", self.name, ", Age: ", self.age)


print("Person.__doc__:", Person.__doc__)            # Return Class documentation string or none, if undefined.
print("Person.__name__:", Person.__name__)          # Return Class name.
print("Person.__module__:", Person.__module__)      # Return Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print("Person.__bases__:", Person.__bases__)        # Return  empty tuple containing the base classes, in the order of their occurrence in the base class list.
print("Person.__dict__:", Person.__dict__)          # Return  dictionary containing the class's namespace.

"""
OUTPUT:
Person.__doc__: This is Person class
Person.__name__: Person
Person.__module__: __main__
Person.__bases__: (<class 'object'>,)
Person.__dict__: {'__module__': '__main__', '__doc__': 'This is Person class', 'PerCount': 0, '__init__': <function Person.__init__ at 0x000001D7DCA9B840>, 'displayCount': <function Person.displayCount at 0x000001D7DCA9BA60>, 'displayPerson': <function Person.displayPerson at 0x000001D7DCA9BD90>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}

"""