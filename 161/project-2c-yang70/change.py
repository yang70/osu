# Author: Matthew Yang
# Date: 10/03/2019
# Description: Ask the user for a number of cents under a dollar and print how many of each type of coin would
#              represent that amount using the least number of coins.

# Prompt the user to enter cents less than a dollar, cast to an integer and store in a variable
print("Please enter an amount in cents less than a dollar.")
cents = int(input())

# Determine the number of each type of coin from greatest value to least
# Determine the remainder and reset the variable to this new amount
quarters = cents // 25
cents = cents % 25

dimes = cents // 10
cents = cents % 10

nickels = cents // 5
pennies = cents % 5

# Print out a message and the result of the above calculations
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)
