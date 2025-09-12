#Doctor class inherits from Employee
from Employee import *

class Doctor(Employee):
    def __init__(self, name="Mario", age=45,id="444", speciality="Mushrooms"):
        super().__init__(name,age)
        self.doctor_id = id
        self.speciality= speciality
        self.patients =[]
        self.assigned_nurse = None #nurse object

    def introduce(self):
        return (f"Hello my name is {self.name} my speciality is {self.speciality}")

    def diagnose(self, patient, condition):
        patient.add_condition(condition)
        return (f"Dr. {self.name} have diagnosed {patient.name} with {condition}")

    def prescribe_medication(self,patient, condition, medication):
        if condition not in patient.conditions:
            return "Medication not given"
        
        patient.add_condition(condition,medication)
        return (f"Dr. {self.name} have prescribed {medication} for {patient.name}'s condition:  {condition}")
    
    def add_patient(patient):
        return ""

    def list_patients():
        return ""

    def get_nurse(Nurse):
        return ""
    
