# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:23:27 2024

@author: DELL
"""

month_days = {
    1: 31,    # January
    2: 28,    # February
    3: 31,    # March
    4: 30,    # April
    5: 31,    # May
    6: 30,    # June
    7: 31,    # July
    8: 31,    # August
    9: 30,    # September
    10: 31,   # October
    11: 30,   # November
    12: 31    # December
}

# Ask user for the month and year
month_number = int(input("Enter a month number (1-12): "))
year = int(input("Enter the year: "))

# Adjust the number of days in February for leap years

# Check if the input month is valid
if 1 <= month_number <= 12:
    print(f"The number of days in month {month_number} of {year} is: {month_days[month_number]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
