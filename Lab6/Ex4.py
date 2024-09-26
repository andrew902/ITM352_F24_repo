#Determine a movie price. The rules are:
# The normal price is $14
#If someone is 65 or older, they pay $8.
#If it is Tuesday, the price is $10.
# If it is a matinee, the price is $5 for seniors and $8 otherwise
#Print out the values of the variables and the price. The price should always be the lowest one that applies.

age = int(input("Enter your age: "))
day = input("What day of the week is the ticket for: ")
time = input("Is it a matinee: ")
discountDays = ["tues", "Tues", "tuesday", "Tuesday"]


if(age >= 65):
    print("Movie ticket price: $8")

if day in discountDays and age < 65:
    print("Movie ticket price: $10")

if time == [yes, Yes] and age >= 65:
    print("Movie ticket price: $5")

