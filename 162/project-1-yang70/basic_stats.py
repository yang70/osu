# Author: Matthew Yang
# Date: 01/06/2020
# Description: Create a person class with name and age data members. Create a 
#              function called basic_stats that takes a list of person objects 
#              as an argument and returns a 3 value tuple of the mean, meadian
#              and mode of those objects.

from statistics import mean, median, mode

class Person:
    """
    Class representing a person with name and age attributes.
    """
    
    def __init__(self, name, age):
        """
        Initializes the person with name and age attributes.
        """
        self.name = name
        self.age = age
        
def basic_stats(person_list):
    """
    Function that takes a list of person objects and returns a 3 value tuple of
    the mean, median and mode of the person objects given.
    """
    # Create a new list of only the ages of the person objects
    age_list = [person.age for person in person_list]
    
    # Return a tuple of mean, median and mode of the age_list using functions
    # from the Python statistics module
    return (mean(age_list), median(age_list), mode(age_list))
