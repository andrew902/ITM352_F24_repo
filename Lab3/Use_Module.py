# Importing the functions from HandyMath.py
from HandyMath import midpoint, squareroot as handy_sqrt, exponentiation as handy_exp, max, min

def main():
    try:
        # Ask the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform calculations
        mid = midpoint(num1, num2)
        sqrt_sq = handy_sqrt(num1) if num1 >= 0 else "Undefined (negative number)"
        exp_result = handy_exp(num1, num2)
        maximum = max(num1, num2)  # Using HandyMath's max
        minimum = min(num1, num2)  # Using HandyMath's min
        
        # Display results
        print(f"The midpoint of {num1} and {num2} is {mid}.")
        print(f"The square root of {num1} is {sqrt_sq}.")
        print(f"{num1} raised to the power of {num2} is {exp_result}.")
        print(f"The maximum of {num1} and {num2} is {maximum}.")
        print(f"The minimum of {num1} and {num2} is {minimum}.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
