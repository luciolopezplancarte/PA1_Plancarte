#This is the person class

class Person():
    def __init__(self, name="Neo", age=21):
        self.name = name
        self.age = age
    
    def Introduce(self):
        return (f"Hello my name is {self.name} and I am {self.age}")

