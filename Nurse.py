#Nurse class inherits from Person()
from Person import *

class Nurse(Person):
    def __init__(self, name="Ratchet",age=35,id="555",department="Bones"):
        super().__init__(name,age)
        self.nurse_id = id
        self.department=department
        self.assigned_doctor = "Doctor Strange"

    def introduce(self):
        return (f"Hello my name is {self.name} I work in the {self.department} with {self.assigned_doctor}")

        

