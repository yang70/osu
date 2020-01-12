# Author: Matthew Yang
# Date: 10/27/2019
# Description: find_median function that takes a list of numbers and returns the
#              median.

def find_median(num_list):
    """
    Takes a list of numbers as an argument and returns the median
    """
    
    # Find the length of the list
    num_list_length = len(num_list)
    
    # Handle lengths of 0 and 1
    if num_list_length == 0:
        return
    elif num_list_length == 1:
        return num_list[0]
    
    # Sort the list
    num_list.sort()
    
    # Find the middle index
    mid = num_list_length // 2
    
    # Return median value depending if the list length is even or odd
    if num_list_length % 2 == 0:
        return (num_list[mid - 1] + num_list[mid]) / 2
    else:
        return num_list[mid]
