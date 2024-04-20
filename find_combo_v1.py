"""Making a system for users to find a combo based on the combos ID to
the menu using dictionaries."""

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


# Function to search for a combo
def search_combo():
    combo_search = input("Enter the name of the combo you "
                         "want to search for: ")

    found = False
    for combo_name, combo_info in combo.items():
        if combo_search.lower() == combo_name.lower():
            found = True
            print(f"\nCombo Name: {combo_name}")
            for key, value in combo_info.items():
                print(f"{key}: {value}")
            break
    if not found:
        print("Combo not found in the Menu.")


# Call function to search for combo
search_combo()
