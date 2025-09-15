from Employee import *

'''
Desc: Nurse class that inherits from employee
Args:
    name (str): The nurse's name in First Last format.
    age (int): The nurse's age in years.
    id (str): Unique identification number with 'N' designation
    department (str): Department in which the nurse works

Attributes:
    _department (str): Departent Nurse is assigned
    _assigned_doctor (Doctor): The Doctor a nurse has been assigned
'''

class Nurse(Employee):

    def __init__(self, name="Ratchet",age=35,id="555",department="Bones"):
        super().__init__(id,name,age)

        self._department=department
        self._assigned_doctor = None 

    def introduce(self):
        '''
        Desc:
            Introduces the nurse with a short message.
        Args:
            None
        Returns:
            (str) A short introduction
        '''
        return (f"{super().introduce()}I'm a nurse working in the {self._department} department. I'm assigned to Dr.{self._assigned_doctor._name}.")

    def assist_doctor(self):
        '''
        Desc:
            Assigns a nurse to a doctor if they are unassigned.
        Args:
            None
        Returns:
            (str): A message indicating if the nurse is assigned to a doctor and if so, which one.
        '''
        if self._assigned_doctor is None:
            return "Im not currently assigned to a doctor."
        return (f"Assisting Dr.{self._assigned_doctor._name} in the {self._department} department")

    def check_vitals(self,patient):
        '''
        Desc:
            Simulates the checking of a patient's vitals.
        Args:
            patient (Patient): Patient object that will have their vitals checked
        Returns:
            (str): Message confirming vitals are being checked.
        '''
        return (f"Checking vitals for patient {patient._name}")

            

