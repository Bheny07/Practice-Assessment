"""Making a Menu for users to see Menu Items"""

import easygui

# Dictionary With Combos
combo = {
    "Value":
        {"Item 1": "Beefburger $5.69",
         "Item 2": "Fries $1.00",
         "Item 3": "Fizzy Drink $1.00",
         "Total": "$7.69"
         },
    "Cheezy":
        {"Item 1": "Cheeseburger $6.69",
         "Item 2": "Fries $1.00",
         "Item 3": "Fizzy Drink $1.00",
         "Total": "$8.69"
         },
    "Super":
        {"Item 1": "Cheeseburger $6.69",
         "Item 2": "Large Fries $2.00",
         "Item 3": "Smoothie $2.00",
         "Total": "$10.69"
         },
}

# Main Loop to construct the message
message = "Combo Information:\n\n"
for combo_id, combo_info in combo.items():
    message += f"Combo Name: {combo_id}\n"
    for key in combo_info:
        message += f"{key}: {combo_info[key]}\n"
    message += "\n"

# Display the message box
easygui.msgbox(message, title="Menu", ok_button="Close")
