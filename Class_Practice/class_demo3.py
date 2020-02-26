"""
Instead of using the normal statements to access attributes, you can use the following functions:

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

P_obj=Person("Piya",20)

print(setattr(P_obj,'name','Riya'))     # Set attribute 'name' at Riya
print(getattr(P_obj,'name'))            # Returns value of 'name' attribute
print(hasattr(P_obj,'name'))            # Returns true if 'name' attribute exists
print(delattr(P_obj,'name'))            # Delete attribute 'name'

