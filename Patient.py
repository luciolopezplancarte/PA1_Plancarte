#Patient class inherits from Person
from Person import *

class Patient(Person):
    
    _patient_id = None
    _conditions = None

    def __init__(self, name = "Patient 0", age=30, id= "000"):
        super().__init__(name, age)
        self._patient_id = id
        self._conditions = {}

    def add_condition(self, condition ="ailment", medication= None):
        self._conditions[condition] = medication
        if medication is not None:
            return (f"{str(self._conditions[condition])} has been added to {self._name}'s record")
        return (f"{str(self._conditions[condition])} has been added to {self._name}'s record and is being treated by {medication}")
        

    def describe_conditions(self):
        if len(self._conditions) == 0:
            return "I have no diagnosed conditions"
        return "I have "+", ".join(str(condition) for condition in self._conditions)

    def take_medication(self):
        if len(self._conditions) == 0:
            return "No medications prescribed"
        return "I am taking "+", ".join(str(self._conditions[condition]) for condition in self._conditions)

    
