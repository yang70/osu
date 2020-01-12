# Author: Matthew Yang
# Date: 10/03/2019
# Description: Asks the user for 5 numbers and then prints the average of the numbers.

# Prompt user for 5 numbers, cast them to a float and then aggregate as they are entered
print("Please enter five numbers.")
sum = float(input())
sum += float(input())
sum += float(input())
sum += float(input())
sum += float(input())

# Print out the sum of the 5 numbers devided by 5.0
print("The average of those numbers is:")
print(sum / 5.0)
