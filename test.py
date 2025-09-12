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

    #Create Nurses
    nurse_brown = Nurse("Alice Brown", 35,"N001", "Emergency")
    nurse_davis = Nurse("Bob Davis", 28, "N002", "Cardiology")

    ##Add Employees to the hospital
    print(central_hospital.add_employee(dr_jones))
    print(central_hospital.add_employee(nurse_brown))
    print(central_hospital.add_employee(nurse_davis))
   
   #Assign Nurse to doctors
    
   #Nurses assist their assigned doctors

   #Create Patients
    patient_wilson = Patient("Charlie Wilson", 30, "P001")
    #patient_taylor = Patient("Diana Taylor", 55, "P002")
    #patient_jones = Patient("Michale Jones", 63, "P003")
   #Assign Patients to Doctors
    
   #Diagnose and prescribe for patients
    print(dr_jones.diagnose(patient_wilson,"Pneumonia"))
    print(dr_jones.prescribe_medication(patient_wilson,"Pneumonia","Azithromycin"))
   #Display patient conditions
    #print(patient_wilson.introduce())
    #print(patient_wilson.describe_conditions())
    #print(patient_wilson.take_medication())



