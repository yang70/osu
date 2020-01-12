# Author: Matthew Yang
# Date: 10/28/2019
# Description: Function that takes a list of first names and returns a list
#              of the names that start with 'K' with ' Kardashian' added

def add_surname(name_list):
    """
    Takes a list of names as an argument and returns the 'K' names with 
    ' Kardashian' concatenated
    """
    
    return [name + ' Kardashian' for name in name_list if name[0] == 'K']
