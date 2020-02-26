"""
Method Resolution Order (MRO):

"""

class A:
    def __init__(self):
        self.name='john'
        self.age=23
    def getName(self):
        return self.name
class B:
    def __init__(self):
        self.name='richard'
        self.id='32'
    def getName(self):
        return self.name
class C(B,A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
    def getName(self):
        return self.name

C1=C()
print(C.__mro__)
print(C.mro())          # print MRO for class C
print(C1.getName())
