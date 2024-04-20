"""Adding on from v2 but turning it into a def statement and using
easygui to make the interface more aesthetic and easy to use for the user"""
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


# Function to remove a combo from the dictionary
def remove_combo():
    while True:
        # Prompt user to enter a combo name to remove
        remove_item = easygui.enterbox("Enter a Combo name to Remove: ",
                                       title="Remove Combo")

        # Break the loop if cancel is pressed
        if remove_item is None:
            break

        # Capitalize the input
        remove_item = remove_item.capitalize()

        # Check if the combo exists
        if remove_item in combo:
            # Directly remove the combo
            del combo[remove_item]
            easygui.msgbox("Combo Was Removed", title="Success")
            break  # Exit the loop after successful removal
        else:
            # Prompt user to try again or not
            retry = easygui.buttonbox("Combo not found in the dictionary. "
                                      "Try again?",
                                      choices=["Yes", "No"], title="Error")
            if retry == "No":
                break  # Exit the loop if the user chooses not to retry


# Check if the script is run directly
if __name__ == "__main__":
    remove_combo()
