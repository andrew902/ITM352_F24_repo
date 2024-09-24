# Library of Handy reusable math functions

# Given two numbers, returns the midpoint between them
def midpoint(num1, num2):
    return(num1 + num2)/2


# Create a function called squareroot that takes a number and 
# and returns the square root of that number .

def squareroot(num1):
    return(num1**0.5)


# Create a function which takes two numbers, a base and an exponent, and returns the value when you raise the base to the 
# power of the exponent

def exponentiation(num1, num2):
    return((num1**num2))



# Function that takes two numbers as inputs and returns the value of the larger one

def max(num1, num2):
    if num1 > num2:
        return(num1)
    else:
        return(num2)


# Function that takes two numbers as inputs and returns the value of the smaller one

def min(num1, num2):
    if num1 < num2:
        return(num1)
    else:
        return(num2)
