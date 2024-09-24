def min(num1, num2):
    if num1 < num2:
        return(num1)
    else:
        return(num2)

number1 = float(input("Please enter first value: "))
number2 = float(input("Please enter second value: "))

min = min(number1,number2)
print("The minimum number is: ", min)