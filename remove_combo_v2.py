combo = {
    "Value":
        {"Item 1": {"Name": "Beefburger", "Price": 5.69},
         "Item 2": {"Name": "Fries", "Price": 1.00},
         "Item 3": {"Name": "Fizzy Drink", "Price": 1.00},
         "Total": "$7.69"
         },
    "Cheezy":
        {"Item 1": {"Name": "Cheeseburger", "Price": 6.69},
         "Item 2": {"Name": "Fries", "Price": 1.00},
         "Item 3": {"Name": "Fizzy Drink", "Price": 1.00},
         "Total": "$8.69"
         },
    "Super":
        {"Item 1": {"Name": "Cheeseburger", "Price": 6.69},
         "Item 2": {"Name": "Large Fries", "Price": 2.00},
         "Item 3": {"Name": "Smoothie", "Price": 2.00},
         "Total": "$10.69"
         },
}

# Capitalize the first letter
remove_item = input("Enter a Combo name to Remove: ").capitalize()
if remove_item in combo:
    # Directly remove the combo
    del combo[remove_item]
    print("Remaining Combo:")
    for key, value in combo.items():
        print(key, ":", value)
else:
    print("Combo not found in the dictionary.")
