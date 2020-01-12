# Author: Matthew Yang
# Date: 10/15/2019
# Description: A function that takes a positive integer and uses the 'hailstorm sequence'
#              and returns the number of steps it takes to reach the first value of 1.

def hailstone(num):
    """
    Takes a positive integer and uses the hailstorm sequence to return the number of
    steps it takes to reach the first value of 1
    """
    # Initialize steps to 0
    step_count = 0

    # Loop and continue calculating and iterating the step count until the current
    # value equals one
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1

        step_count += 1

    # Return the step count when the value equals 1
    return step_count
