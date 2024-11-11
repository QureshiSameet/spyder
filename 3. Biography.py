# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:05:23 2024

@author: DELL
"""

# INPUT USER DATA 
name = input("Enter your name:")
age_input=  input("Enter your age:")
hometown = input("Enter your hometown:")
try:
    age = int(age_input) 
except ValueError:
    print("INVALID AGE NUMBER. PLEASE ENTER A VALID AGE NUMBER")
    age = None
               
# STORE INFO IN THE DICTIONARY
person_data = {
    "name": name,
    "age": age,
    "hometown": hometown,
    }
# PRINT THE INFO
print("name:", person_data["name"])
print("age:", person_data["age"])
print("hometown:", person_data["hometown"])
# if both first name and last name are asked for name then there is not any issue because the input() function can naturally handle multi-word strings. 