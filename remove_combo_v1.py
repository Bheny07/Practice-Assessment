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

if "Super" in combo:
    popped_item = combo.pop("Super")
    print("Remaining Combo:")
    for key, value in combo.items():
        print(key, ":", value)
    print("\nPopped Item:")
    print(popped_item)
else:
    print("Key 'Super' not found in the dictionary.")
