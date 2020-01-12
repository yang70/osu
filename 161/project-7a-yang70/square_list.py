# Author: Matthew Yang
# Date: 11/10/2019
# Description: Function that takes a list and replaces each value with the
#              square of that value.

def square_list(num_list):
    """
    Takes a list of numbers as an arguments and mutates the list by replacing
    each value with the square of that value
    """
    
    # Iterate the list replacing value with it's square
    for index, value in enumerate(num_list):
        num_list[index] = value**2
