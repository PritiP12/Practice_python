"""
Private \ Protected Variable :
"""

class Robot:
    def __init__(self,name,name2):
        self.__name=name    #private
        self._name=name2    #protected

    def say_hi(self):
        print("Hi, i am "+self.__name)

class PhysicianRobot(Robot):

    def say_hi(self):
        super().say_hi()
        print(self._name +"take care of you")   #name variable not accessible here
        print("and i am a physician")

y=PhysicianRobot("James","Bond")
y.say_hi()