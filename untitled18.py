# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:27:23 2025

@author: DELL
"""

def display_menu():
    print("Welcome to the Vending Machine!")
    print("Here are the available items:\n")
    print("1. Coke - $1.50")
    print("2. Pepsi - $1.50")
    print("3. Chips - $1.00")
    print("4. Candy - $0.75")
    print("5. Hot Chocolate - $2.00")
    print("")  # New line for separation

def process_transaction():
    display_menu()

    # input for item selection
    try:
        item_choice = int(input("Enter the number of the item you want to buy: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # choose valid item
    if item_choice == 1:
        item_name = "Coke"
        price = 1.50
    elif item_choice == 2:
        item_name = "Pepsi"
        price = 1.50
    elif item_choice == 3:
        item_name = "Chips"
        price = 1.00
    elif item_choice == 4:
        item_name = "Candy"
        price = 0.75
    elif item_choice == 5:
        item_name = "Hot Chocolate"
        price = 2.00
    else:
        print("Invalid item number! Please select a valid item.")
        return

    print(f"You selected: {item_name} - ${price}")

    # payment
    try:
        money_inserted = float(input("Enter the amount of money you have: $"))
    except ValueError:
        print("Invalid input! Please enter a valid numeric amount.")
        return

    # Check money
    if money_inserted < price:
        print("You don't have enough money for this item.")
        return

    # Calculate change
    change = round(money_inserted - price, 2)
    print(f"Thank you for your purchase! Your change is: ${change}")

    # Ask if the user wants to buy another item
    another = input("Would you like to buy another item? (yes/no): ").lower()
    if another == "yes":
        process_transaction()
    else:
        print("Thank you for using the vending machine!")

# Start the transaction
if __name__ == "__main__":
    process_transaction()
