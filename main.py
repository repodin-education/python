# Leap Year Checker (Python)

# Task: Write a Python program that determines if a given year is a leap year.

year = int(input().strip())

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
