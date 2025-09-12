#Hospital Class

class Hospital():
    def __init__(self, name):
        self.name = name 
        self.employees =[]

    '''
    Method to add an employee to the hospital employee list if they are not already in the list
    Args: employee (Employee) The employee object to add to the hospital
    Returns: str: A message indicating if the employee was added or if they were already an employee
    '''
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            return (f"{employee.name} has been added as an employee at {self.name}")
        else:
            return (f"{employee.name} is already an employee at {self.name}")

    '''
    Method to list the names of all employees curretnly working at the hospital
    Returns: list: A list of employee names(strings)
    '''
    def list_employees(self):
        if len(employees) == 0:
            return "No One is currently employed"
    
        return ", ".join(str(employee.name) for employee in self.employees)
            
    '''
    Method to find from the employees in the hospital all doctors that specialize in a given field.
    Args: speciality (str): The medical speciality to filter doctors by
    Returns: list: A list of names for Doctors who specialize in the specified field
    '''
    def find_doctor(self,speciality):
        ##Use the employee list to look for doctors with a speciality
        ## doctors have a unique identifier, emp_id starts with D
        ##check if the doctor has the speciality
        doctor_list =[]
        for e in self.employees:
            if e.emp_id[0]=='D':
                if e.speciality == speciality:
                    doctor_list.append(str(e.name))
        
        return doctor_list

    

