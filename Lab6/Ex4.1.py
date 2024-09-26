age = int(input("Enter your age: "))
day = input("What day of the week is the ticket for: ").strip().lower()  # Normalize input to lowercase
is_matinee = input("Is it a matinee (yes/no): ").strip().lower() == "yes"  # Convert to boolean

# Determine the ticket price
if age >= 65:
    price = 8 if is_matinee else 5  # Senior pricing for matinee
elif day == "tuesday":
    price = 10  # Discounted Tuesday price
elif is_matinee:
    price = 8  # Regular matinee price
else:
    price = 14  # Normal price

# Print out the results
print(f"Age: {age}")
print(f"Day: {day.capitalize()}")
print(f"Matinee: {'Yes' if is_matinee else 'No'}")
print(f"Final movie ticket price: ${price}")
