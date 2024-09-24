# Ask the user to enter a floating point number between 1 and 100. Square the number
# and return the value to the user.
# Name: Andrew Mora
# Date created: 9/6/24

value_entered = input("Please enter a floating point number between 1 and 100: ")

value_entered = float(value_entered)
value_sqaured = value_entered**2
print ("The value squared= ", round(value_sqaured,1))