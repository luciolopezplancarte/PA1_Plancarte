#This is the person class

class Person():
    _name = None
    _age = None
    def __init__(self, name="Neo", age=21):
        self._name = name
        self._age = age
    
    def introduce(self):
        return (f"My name is {self._name} and I am {self._age} years old. ")

