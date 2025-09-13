#Hospital Class

class Hospital():

    _name = None
    _employees = None

    def __init__(self, name):
        self._name = name 
        self._employees =[]

    '''
    Method to add an employee to the hospital employee list if they are not already in the list
    Args: employee (Employee) The employee object to add to the hospital
    Returns: str: A message indicating if the employee was added or if they were already an employee
    '''
    def add_employee(self, employee):
        if employee not in self._employees:
            self._employees.append(employee)
            return (f"{employee._name} has been added as an employee at {self._name}")
        else:
            return (f"{employee._name} is already an employee at {self._name}")

    '''
    Method to list the names of all employees curretnly working at the hospital
    Returns: list: A list of employee names(strings)
    '''
    def list_employees(self):
        if len(self._employees) == 0:
            return "No One is currently employed"
    
        return ", ".join(str(employee._name) for employee in self._employees)
            
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
        for doctor in self._employees:
            if doctor.emp_id[0]=='D':
                if doctor._speciality == speciality:
                    doctor_list.append(str(doctor._name))
        
        return doctor_list

    

