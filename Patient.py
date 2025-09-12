#Patient class inherits from Person
from Person import *

class Patient(Person):
    def __init__(self, name = "Patient 0", age=30, id= "000"):
        super().__init__(name, age)
        self.patient_id = id
        self.conditions = {}

    def add_condition(self, condition ="ailment", medication= ""):
        self.conditions[condition] = medication

    def describe_condition(self):
        return "I have "+", ".join(str(condition) for condition in self.conditions)

    def take_medications(self):
        return "I am taking "+", ".join(str(self.conditions[condition]) for condition in self.conditions)

    
