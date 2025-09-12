#setting up super() introduce
from Nurse import *
from Doctor import *

if __name__ =="__main__":
    nurse_brown = Nurse("Alice Brown", 35, "N001", "Emergency")

    dr_jones = Doctor("Emily Jones", 45, "D001", "Pulmonology")


    print(nurse_brown.introduce())
    print(dr_jones.introduce())


