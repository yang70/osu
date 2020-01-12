# Author: Matthew Yang
# Date: 11/10/2019
# Description: Function takes a list and reverses the order.

def reverse_list(li):
    """
    Reverses the order of the given list
    """
    
    # Reverse slice the list
    rev = li[::-1]
    
    # Replace the original list with reversed list by index
    for index in range(0, len(li)):
        li[index] = rev[index]
