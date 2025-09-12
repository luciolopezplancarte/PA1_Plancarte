#Doctor class inherits from Employee
from Employee import *

class Doctor(Employee):
    def __init__(self, name="Mario", age=45,id="444", speciality="Mushrooms"):
        super().__init__(id,name,age)
        self.doctor_id = id
        self.speciality= speciality
        self.patients =[]
        self.assigned_nurse = None #nurse object

    def introduce(self):
        return (f"{super().introduce()}My speciality is {self.speciality}")

    def diagnose(self, patient, condition):
        patient.add_condition(condition)
        return (f"Dr. {self.name} have diagnosed {patient.name} with {condition}")

    def prescribe_medication(self,patient, condition, medication):
        if condition not in patient.conditions:
            return "Medication not given"
        
        patient.add_condition(condition,medication)
        return (f"Dr. {self.name} have prescribed {medication} for {patient.name}'s condition: {condition}")
    
    def add_patient(self,patient):
        if patient not in self.patients:
            self.patients.append(patient)
            return (f"Added {patient.name} to Doctor {self.name} patient list.") 
        return (f"{patient.name} is already in Doctor {self.name}'s patient list")

    def list_patients(self):
        if len(self.patients) == 0:
            return (f"No Patients in Doctor {self.name}'s patient list.")
        return ", ".join(str(patient.name) for patient in self.patients)


    def assign_nurse(self, nurse):
        if nurse.assigned_doctor is not None:
            if nurse.nurse_id == self.assigned_nurse.nurse_id:
                return "This nurse is already assigned to this doctor"
        self.assigned_nurse = nurse
        return (f"{nurse.name} has been assigned to {self.name}")
