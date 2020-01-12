# Author: Matthew Yang
# Date: 11/13/2019
# Description: Function that takes a string and returns a dictionary of how many
#              times that letter appears in that string.

def count_letters(str):
    """
    Function that takes a string and returns a dictionary with how many of each
    letter appears in the string
    """
    # Set of upper case alphabet
    letters = { 
        'A', 'B', 'C', 'D', 'E', 'F', 
        'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z'
    }
    
    # Initialize an empty dictionary for the results
    result = {}
    
    # Iterate the string and check if the character is in the letter dictionary.
    # If so initialize or iterate the count for that letter.
    for char in str.upper():
        if char in letters:
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1
                
    return result
