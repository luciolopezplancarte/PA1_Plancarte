#This is an Employee class that inherits from Person
from Person import *

class Employee(Person):

    def __init__(self, name = "Job", id="316"):
        super().__init__(name)
        self.emp_id = id

