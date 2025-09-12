#Patient class inherits from Person
from Person import *

class Patient(Person):
    def __init__(self, name = "Patient 0", age=30, id= "000"):
        super().__init__(name, age)
        self.patient_id = id
        self.conditions = {}

    def add_condition(self, condition ="ailment", medication= None):
        self.conditions[condition] = medication
        if medication is not None:
            return (f"{str(self.conditions[condition])} has been added to {self.name}'s record")
        return (f"{str(self.conditions[condition])} has been added to {self.name}'s record and is being treated by {medication}")
        

    def describe_conditions(self):
        if len(self.conditions) == 0:
            return "I have no diagnosed conditions"
        return "I have "+", ".join(str(condition) for condition in self.conditions)

    def take_medication(self):
        if len(self.conditions) == 0:
            return "No medications prescribed"
        return "I am taking "+", ".join(str(self.conditions[condition]) for condition in self.conditions)

    
