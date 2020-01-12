# Author: Matthew Yang
# Date: 11/13/2019
# Description: Employee class with public data members and a function that takes
#              four lists of employee attributes and returns a dictionary of
#              employee objects created from those attributes with the id number
#              attribute as the dictionary key.

class Employee:
    """
    Class representing an employee with name, ID_number, salary and
    email_address public data members
    """
    # Initialize method for setting employee data members
    def __init__(self, name, ID_number, salary, email_address):
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address
        
def make_employee_dict(name_list, id_list, salary_list, email_list):
    """
    Takes lists of employee attributes and returns a dictionary of employee
    objects created from those objects with the id as the key
    """
    # Initilize the result dictionary
    result = {}
    
    # For the length of our ID list, for each index create an employee object
    # using the corresponding data and set in dictionary with the ID_number as
    # the dictionary key
    for index in range(len(id_list)):
        result[id_list[index]] = Employee(
            name_list[index], 
            id_list[index], 
            salary_list[index], 
            email_list[index]
        )
        
    return result
