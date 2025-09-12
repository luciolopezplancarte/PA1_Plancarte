#This is the person class

class Person():
    def __init__(self, name="Neo", age=21):
        self.name = name
        self.age = age
    
    def introduce(self):
        return (f"My name is {self.name} and I am {self.age} years old. ")

