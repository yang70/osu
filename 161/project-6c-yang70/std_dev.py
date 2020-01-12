# Author: Matthew Yang
# Date: 10/30/2019
# Description: Person class with name and age data members. Also a std_dev
#              function that takes a list of Person objects and calculates the
#              standard deviation of the ages.

class Person:
    """
    Represents a person with name and age data members
    """
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
def std_dev(person_list):
    """
    Function that finds the standard deviation of ages from a list of person
    objects
    """
    # Guard agains emtpy person list
    if len(person_list) == 0:
        return
    
    # Create a list of ages only and find the mean
    age_list = [person.age for person in person_list]
    mean = list_mean(age_list)
        
    # For each age subtract the mean and square the result
    age_list = [(age - mean)**2 for age in age_list]
    
    # Find the mean of the new age list (variance)
    variance = list_mean(age_list)
    
    # Return the square root of the variance
    return variance**(1/2)
    
def list_mean(num_list):
    """
    Returns the mean from a list of numbers
    """
    sum = 0
    
    for num in num_list:
        sum += num
        
    return sum / len(num_list)
