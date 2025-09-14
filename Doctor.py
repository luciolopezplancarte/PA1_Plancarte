#Doctor class inherits from Employee
from Employee import *

class Doctor(Employee):

    def __init__(self, name="Mario", age=45,id="444", speciality="Mushrooms"):
        super().__init__(id,name,age)
        self._doctor_id = id
        self._speciality= speciality
        self._patients =[]
        self._assigned_nurse = None #nurse object

    def introduce(self):
        return (f"{super().introduce()}My speciality is {self._speciality}")

    def diagnose(self, patient, condition):
        patient.add_condition(condition)
        return (f"Dr. {self._name} have diagnosed {patient._name} with {condition}")

    def prescribe_medication(self,patient, condition, medication):
        if condition not in patient._conditions:
            return "Medication not given"
        
        patient.add_condition(condition,medication)
        return (f"Dr. {self._name} have prescribed {medication} for {patient._name}'s condition: {condition}")
    
    def add_patient(self,patient):
        if patient not in self._patients:
            self._patients.append(patient)
            return (f"Added {patient._name} to Doctor {self._name} patient list.") 
        return (f"{patient._name} is already in Doctor {self._name}'s patient list")

    def list_patients(self):
        if len(self._patients) == 0:
            return (f"No Patients in Doctor {self._name}'s patient list.")
        return ", ".join(str(patient._name) for patient in self._patients)


    def assign_nurse(self, nurse):
        if nurse._assigned_doctor is not None:
            if nurse._nurse_id == self._assigned_nurse._nurse_id:
                return "This nurse is already assigned to this doctor"
            return "This nurse is already assigned to another doctor"
        self._assigned_nurse = nurse
        nurse._assigned_doctor = self
        return (f"{nurse._name} has been assigned to {self._name}")
