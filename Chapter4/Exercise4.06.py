'''
*4.6 (Health application: BMI) Revise Listing 4.6, ComputeBMI.py, to let users enter
their weight in pounds and their height in feet and inches. For example, if a person
is 5 feet and 10 inches, you will enter 5 for feet and 10 for inches.
'''
import math

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in feet and inches
height_in_feet = eval(input("Enter feet: "))
height_in_inches = eval(input("Enter inches: "))

# Constants
KILOGRAMS_PER_POUND = 0.45359237 # Constant
METERS_PER_INCH = 0.0254         # Constant
METERS_PER_FEET = 0.3048         # Constant

# Compute BMI
weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height_in_inches * METERS_PER_INCH + height_in_feet * METERS_PER_FEET
bmi = weightInKilograms / (heightInMeters * heightInMeters)

# Display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")