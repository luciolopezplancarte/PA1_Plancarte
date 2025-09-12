#This is the test file for the OOP assignment

from Hospital import *
from Doctor import *
from Patient import *
from Employee import *
from Nurse import *

if __name__ =="__main__":
    #Create Hospital
    central_hospital = Hospital("Central Hospital")

    #Create Doctor
    dr_jones = Doctor("Emily Jones", 45, "D001", "Pulmonology")
    print(dr_jones.introduce())
    print("o"*50)

    ##Add Employees to the hospital
    print(central_hospital.add_employee(dr_jones))

