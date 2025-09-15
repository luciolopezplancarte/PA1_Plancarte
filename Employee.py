from Person import *

'''
Desc: Employee class that inherits from Person class.

Args:
    id (str): Unique identification number for an employee
    name (str): An employee's name in First Last format
    age (int): An employee's age in years

Attributes:
    emp_id (str): Unique identification number for an employee
'''
class Employee(Person):

    def __init__(self, id="316", name = "Job", age=24):
        super().__init__(name,age)

        self.emp_id = id

