#Nurse class inherits from Employee 
from Employee import *

class Nurse(Employee):
    def __init__(self, name="Ratchet",age=35,id="555",department="Bones"):
        super().__init__(name,age)
        self.nurse_id = id
        self.department=department
        self.assigned_doctor = None 

    def introduce(self):
        return (f"Hello my name is {self.name} I am {self.age} years old. I'm a nurse working in the {self.department} department. I'm assigned to Dr.{self.assigned_doctor}.")

    def assist_doctor(self):
        if self.assigned_doctor is None:
            return "Im not currently assigned to a doctor."
        return (f"Assisting Dr.{self.assigned_doctor.name} in the {self.department}")

    def check_vitals(self,patient):
        return (f"Checking vitals for patient {patient.name}")

            

