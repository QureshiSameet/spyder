# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:54:24 2024

@author: DELL
"""

# correct password
correct_password = "00000"

# maximum number of attempts
max_attempts = 5

# Loop for password attempts
for attempts in range(max_attempts):
    entered_password = input("Please enter the password: ")

    if entered_password == correct_password:
        print("Password correct! Access granted.")
        break
    else:
        remaining_attempts = max_attempts - (attempts + 1)
        if remaining_attempts > 0:
            print(f"Incorrect password. {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. Authorities have been alerted.")
