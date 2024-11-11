# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:17:10 2024

@author: DELL
"""

#determine if the number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Main function to interact with the user
def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    result = check_even_or_odd(user_input)
    
    # Print the result
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
