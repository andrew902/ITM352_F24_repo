# Input for first name, middle initial, and last name
First = input("Enter your first name: ")
MiddleInitial = input("Enter your middle initial: ")
Last = input("Enter your last name: ")

# Store the names in a list
FullName = [First, MiddleInitial, Last]

# Concatenate and print using format() with unpacking
print("Your full name is {} {} {}".format(*FullName))
