# Author: Matthew Yang
# Date: 10/03/2019
# Description: Asks the user for a temperature in Celsius and prints out the equivalent in Fehrenheit

# Prompt user for a Celsius temperature, cast it to a float and store it in a variable
print("Please enter a Celsius temperature.")
temp_celsius = float(input())

# Convert the Celsius temperature to Fahrenheit and store it in a new variable
temp_fahrenheit = (9.0 / 5.0) * temp_celsius + 32.0

# Print out a message and the Fahrenheit temperature
print("The equivalent Fahrenheit temperature is:")
print(temp_fahrenheit)