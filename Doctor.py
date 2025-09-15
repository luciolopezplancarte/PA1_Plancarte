from Employee import *

'''
Desc: Doctor class that inherits from Employee class
Args:
    name (str): The doctor's name in First Last format.
    age (int): The doctor's age in years
    id (str): Unique identification number with 'D' designation
    speciality (str): The doctor's expertise

Attributes: 
    _speciality (str): The doctor's expertise
    _patients (List[Person]): A list of Patient objects that are 
                                assigned to the doctor.
    _assigned_nurse (Nurse): A Nurse object that is assigned 
                                to the doctor.
    
'''

class Doctor(Employee):

    def __init__(self, name="Mario", age=45,id="444", speciality="Mushrooms"):
        super().__init__(id,name,age)
        
        self._speciality= speciality
        self._patients =[]
        self._assigned_nurse = None #nurse object

    def introduce(self):
        '''
        Desc:
            Introduces the doctor object with their name and speciality.
        Returns:
            (str) A short introduction.
        '''
        return (f"{super().introduce()}My speciality is {self._speciality}")

    def diagnose(self, patient, condition):
        '''
        Desc:
            Diagnoses a patient with a condition
        Args:
            patient (Patient): Patient object that is being diagnosed
            condition (str): The name of the condition that was diagnosed
        Returns:
            (str) A message indicating that the diagnosis was performed
        '''
        patient.add_condition(condition)
        return (f"Dr. {self._name} has diagnosed {patient._name} with {condition}")

    def prescribe_medication(self,patient, condition, medication):
        '''
        Desc:
            Prescribes a medication to a patient only if they have been previously diagnosed.
        Args:
            patient (Patient): The patient object that is being prescribed medication
            condition (str): The name of the condition being treated.
            medication (str): The name of the medication being used to treat the condition.
        Returns:
            (str): Message indicating if the medication was succesfully or unsuccesfully prescribed.
        '''
        if condition not in patient._conditions:
            return (f"The patient {patient._name} has not been"+  
                    "diagnosed with {condition}. Medication:"+ 
                    f"{medication} was not prescribed.")
        
        patient.add_condition(condition,medication)
        return (f"Dr. {self._name} has prescribed {medication} for {patient._name}'s condition: {condition}")
    
    def add_patient(self,patient):
        '''
        Desc:
            Adds Patient objects to the doctor's patient list. 
        Args:
            patient (Patient): The patient to add to the list.
        Returns:
            (str): Message indicating if the patient was able to be added to the list.
        '''
        if patient not in self._patients:
            self._patients.append(patient)
            return (f"Added {patient._name} to Doctor {self._name} patient list.") 
        return (f"{patient._name} is already in Doctor {self._name}'s patient list")

    def list_patients(self):
        '''
        Desc:
            Prints the doctor's patient list.
        Args:
            None
        Returns:
            (str): A string representation of the doctor's patient list.
        '''
        if len(self._patients) == 0:
            return (f"No Patients in Doctor {self._name}'s patient list.")
        return ", ".join(str(patient._name) for patient in self._patients)


    def assign_nurse(self, nurse):
        '''
        Desc:
            Assigns a nurse to the doctor
        Args:
            nurse (Nurse): Nurse object to assign to doctor
        Returns:
            (str) Message indicating success or failure of assigning nurse to doctor
        '''
        if nurse._assigned_doctor is not None:
            if nurse.emp_id == self._assigned_nurse.emp_id:
                return "This nurse is already assigned to this doctor"
            return "This nurse is already assigned to another doctor"
        self._assigned_nurse = nurse
        nurse._assigned_doctor = self
        return (f"{nurse._name} has been assigned to {self._name}")
