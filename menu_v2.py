"""Modifying v1 so that it is in easygui
format and is easier for users to read."""

import easygui

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
message = ""
for combo_id, combo_info in combo.items():
    message += f"\nCombo Name: {combo_id}\n"
    for key in combo_info:
        message += f"{key}: {combo_info[key]}\n"

easygui.msgbox(message, title="Menu")
