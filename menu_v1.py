"""Using a dictionary to printing out a Menu for users to
see items available for purchase"""

# Dictionary of Combo Items
combo = {
    "Value":
        {"Item 1": "Beefburger $5.69",
         "Item 2": "Fries $1.00",
         "Item 3": "Fizzy Drink $1.00",
         },
    "Cheezy":
        {"Item 1": "Cheeseburger $6.69",
         "Item 2": "Fries $1.00",
         "Item 3": "Fizzy Drink $1.00",
         },
    "Super":
        {"Item 1": "Cheeseburger $6.69",
         "Item 2": "Large Fries $2.00",
         "Item 3": "Smoothie $2.00",
         },
}
# Main Loop
for combo_id, combo_info in combo.items():
    print(f"\nCombo Name: {combo_id}")

    for key in combo_info:
        print(f"{key}: {combo_info[key]}")
