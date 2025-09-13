#This is an Employee class that inherits from Person
from Person import *

class Employee(Person):

    emp_id = None

    def __init__(self, id="316", name = "Job", age=24):
        super().__init__(name,age)
        self.emp_id = id

