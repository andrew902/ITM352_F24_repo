# Ask the user to enter a number between 1 and 100. Square the number
# and return the value to the user.
# Name: Andrew Mora
# Date created: 9/4/24

value_entered = input("Please enter a value between 1 and 100: ")

value_entered_int = int(value_entered)
value_sqaured = value_entered_int**2
print ("The value entered= ", value_entered_int)
print ("The value squared= ", value_sqaured)