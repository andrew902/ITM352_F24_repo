# Create a function which takes two numbers, a base and an exponent, and returns the value when you raise the base to the 
# power of the exponent

def exponentiation(num1, num2):
    return((num1**num2))

number1 = input("Enter base value:")
number2 = float(input("Enter exponent value:"))
number1 = float(number1)


exponent = exponentiation(number1, number2)
print("The exponentiation is:", exponent)
