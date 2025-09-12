#This is the test file for the OOP assignment

from Hospital import *
from Doctor import *
from Patient import *
from Employee import *
from Nurse import *

if __name__ =="__main__":
    adam = Nurse()
    print (adam.name)
    print(adam.age)
    print(adam.introduce())
    print(adam.department)
    print(adam.assigned_doctor)
    #print("adding a condition")
    #adam.add_condition("arthritis")
    #print(adam.describe_conditions())
    #print(adam.take_medication())
