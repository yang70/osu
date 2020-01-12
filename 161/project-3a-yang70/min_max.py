# Author: Matthew Yang
# Date: 10/07/2019
# Description: Ask the user how many integers they would like to enter. Prompt the user to enter that many integers.
#              After they have all been entered, display the smallest and largest integers.  Assume input will be
#              integers >= 1

# Prompt the user for input and set it to a variable
print("How many integers would you like to enter?")
count = int(input())
print("Please enter", count, "integers.")

# Create a range and iterate that many times to receive the integers from the user.
for current in range(0, count):
    # Set the user input to a variable
    num = int(input())

    # If the value of current is 0, it is the first integer and initialize min and max with that value
    if current == 0:
        min = num
        max = num
    # If current is not 0 check the input to see if it is less than the minimum and more than the maximum.
    # If either is true set that value to the current number
    else:
        if num < min:
            min = num

        if num > max:
            max = num

# Print out the results
print("min:", min)
print("max:", max)
