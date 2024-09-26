#A leap year is a year that consists of 366 (not 365) days. It occurs roughly every four years. More specifically, a year is 
#considered leap if it is either divisible by 4 but not by 100 or it is divisible by 400.
#Write a program that asks the user for a year and replies with either "leap year" or "not a leap year".

year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


