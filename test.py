#This is the test file for the OOP assignment

from Hospital import *
from Doctor import *
from Patient import *
from Employee import *
from Nurse import *

if __name__ =="__main__":
    #Create Hospital
    central_hospital = Hospital("Central Hospital")

    #Create Doctors
    dr_jones = Doctor("Emily Jones", 45, "D001", "Pulmonology")
    print(dr_jones.introduce())
    print("o"*50)
    dr_smith = Doctor("John Smith", 50, "D002", "Cardiology")
    print(dr_smith.introduce())
    print("~"*50)

    #Create Nurses
    nurse_brown = Nurse("Alice Brown", 35,"N001", "Emergency")
    nurse_davis = Nurse("Bob Davis", 28, "N002", "Cardiology")

    ##Add Employees to the hospital
    print(central_hospital.add_employee(dr_jones))
    print(central_hospital.add_employee(dr_smith))
    print(central_hospital.add_employee(nurse_brown))
    print(central_hospital.add_employee(nurse_davis))
   
   #Assign Nurses to doctors
    print(dr_jones.assign_nurse(nurse_brown))
    print(dr_smith.assign_nurse(nurse_davis))
    print("#"*50)
    print(dr_jones.assign_nurse(nurse_brown))
    print(dr_jones.assign_nurse(nurse_davis))

   #Nurses assist their assigned doctors
    print(nurse_brown.introduce())
    print(nurse_brown.assist_doctor())
    
    print(nurse_davis.introduce())
    print(nurse_davis.assist_doctor())

   #Create Patients
    patient_wilson = Patient("Charlie Wilson", 30, "P001")
    patient_taylor = Patient("Diana Taylor", 55, "P002")
    patient_jones = Patient("Michale Jones", 63, "P003")

    #Assign Patients to Doctors
    print(dr_jones.list_patients())
    print(dr_jones.add_patient(patient_wilson))
    print(dr_jones.add_patient(patient_wilson))
    print(dr_jones.add_patient(patient_taylor))
    print(dr_jones.add_patient(patient_jones))
    print(dr_jones.list_patients())

   #Diagnose and prescribe for patients
    print(dr_jones.diagnose(patient_wilson,"Pneumonia"))
    print(dr_jones.prescribe_medication(patient_wilson,"Pneumonia","Azithromycin"))
    print("@"*50)

    print(dr_smith.diagnose(patient_taylor,"Hypertension"))
    print(dr_smith.prescribe_medication(patient_taylor,"Hypertension","Lisinopril"))

    
    print(dr_smith.diagnose(patient_taylor,"High Cholesterol"))
    print(dr_smith.prescribe_medication(patient_taylor,"High Cholesterol","Atorvastatin"))

    print(dr_smith.prescribe_medication(patient_taylor, "Headaches","Tylenol"))

   #Display patient conditions
    print(patient_wilson.introduce())
    print(patient_wilson.describe_conditions())
    print(patient_wilson.take_medication())
    print("="*50)
    print(patient_taylor.introduce())
    print(patient_taylor.describe_conditions())
    print(patient_taylor.take_medication())
    print("="*50)
    print(patient_jones.introduce())
    print(patient_jones.describe_conditions())
    print(patient_jones.take_medication())
    print("="*50)

    print(nurse_brown.check_vitals(patient_wilson))

    print(f"Doctors who specialize in 'Pulmonology': {central_hospital.find_doctor('Pulmonology')}")
