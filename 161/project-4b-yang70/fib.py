# Author: Matthew Yang
# Date: 10/15/2019
# Description: Function that takes a positive integer and returns the number at that
#              position of the Fibonacci sequence.

def fib(position):
    """Takes a positive integer as an argument and returns the Fibonacci value at that position."""
    # Initialize the sequence
    previous = 0
    current = 1

    # Iterate starting with one up to but not including the position desired times
    # Store the current value, calculate the new current and then set the previous
    # to the stored value
    for num in range(1, position):
        store = current
        current += previous
        previous = store

    # Return current after all iterations complete
    return current
