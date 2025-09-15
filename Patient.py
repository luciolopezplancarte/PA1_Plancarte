from Person import *

'''
Desc: Patient class that inherits from Person
Args:
    name (str): The name of the patient in First Last format.
    age (int): The age of the patient in years
    id (str): Unique identifier number with a 'P' designation

Attributes:
    _patient_id (str): Unique identifier number with a 'P' designation
    _conditions (Dict): Dictionary of diagnosed conditions and their correspoding medications if any.

'''

class Patient(Person):
    
    def __init__(self, name = "Patient 0", age=30, id= "000"):
        super().__init__(name, age)

        self._patient_id = id
        self._conditions = {}

    def add_condition(self, condition ="ailment", medication= None):
        '''
        Desc:
            Adds condition to a patient _conditions Dictionary
        Args:
            condition (str): condition being added
            medication (str): medication used to treat condition
        Returns:
            (str): Message indicating if condition was added and if medication was prescribed.
        
        '''
        self._conditions[condition] = medication
        if medication is not None:
            return (f"{str(self._conditions[condition])} has been added to {self._name}'s record")
        return (f"{str(self._conditions[condition])} has been added to {self._name}'s record and is being treated by {medication}")
        

    def describe_conditions(self):
        '''
        Desc:
            Describes the conditions currently in the _conditions Dictionary
        Args:
            None
        Returns:
            (str): Returns a formatted string message with _conditions Dictionary keys listing diagnosed conditions
        '''
        if len(self._conditions) == 0:
            return "I have no diagnosed conditions"
        return "I have "+", ".join(str(condition) for condition in self._conditions)

    def take_medication(self):
        '''
        Desc:
            Self-Adminstration of medication by patient
        Args:
            None
        Returns:
            (str): Confirmation message of medication taken.

        '''
        if len(self._conditions) == 0:
            return "No medications prescribed"
        return "I am taking "+", ".join(str(self._conditions[condition]) for condition in self._conditions)

    
