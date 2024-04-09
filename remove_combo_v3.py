import easygui

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


def remove_combo():
    while True:
        # Capitalize the first letter
        remove_item = easygui.enterbox("Enter a Combo name to Remove: ".
                                       capitalize(),
                                       title="Remove Combo")
        if remove_item in combo:
            # Directly remove the combo
            del combo[remove_item]
            easygui.msgbox("Combo Was Removed", title="Success")
            break  # Exit the loop after successful removal
        else:
            retry = easygui.buttonbox("Combo not found in the dictionary. "
                                      "Try again?",
                                      choices=["Yes", "No"], title="Error")
            if retry == "No":
                break  # Exit the loop if the user chooses not to retry


remove_combo()
