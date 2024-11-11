# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:04:31 2024

@author: DELL
"""

# List of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# input a name to search for
search_name = input("Enter the name you want to search for: ")

# Search for the name
if search_name in names:
    print("its in the list.")
else:
    print("its not in the list.")
