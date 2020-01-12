# Author: Matthew Yang
# Date: 11/13/2019
# Description: Function that takes two strings and returns a set of the words
#              contained in both strings regardless of case.

def words_in_both(str_1, str_2):
    """
    Function that takes two strings and returns a set containing the words in
    that appear in both strings regardless of case
    """
    
    # Use a set comprehension to analyze both strings given after changing to
    # lower case and splitting on spaces
    return {word for word in str_1.lower().split() if word in str_2.lower().split()}
