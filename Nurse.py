#Nurse class inherits from Employee 
from Employee import *

class Nurse(Employee):

    _nurse_id = None
    _department = None
    _assigned_doctor = None

    def __init__(self, name="Ratchet",age=35,id="555",department="Bones"):
        super().__init__(id,name,age)
        self._nurse_id = id
        self._department=department
        self._assigned_doctor = None 

    def introduce(self):
        return (f"{super().introduce()}I'm a nurse working in the {self._department} department. I'm assigned to Dr.{self._assigned_doctor._name}.")

    def assist_doctor(self):
        if self._assigned_doctor is None:
            return "Im not currently assigned to a doctor."
        return (f"Assisting Dr.{self._assigned_doctor._name} in the {self._department} department")

    def check_vitals(self,patient):
        return (f"Checking vitals for patient {patient._name}")

            

