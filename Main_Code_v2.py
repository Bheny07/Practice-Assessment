"""Adding Menu v2 into main code"""
# Import the EasyGUI library for GUI interaction
import easygui

# Define the combo dictionary containing menu items and prices
combo = {
    "Value": {"Item 1": {"Name": "Beefburger", "Price": 5.69},
              "Item 2": {"Name": "Fries", "Price": 1.00},
              "Item 3": {"Name": "Fizzy Drink", "Price": 1.00},
              "Total": "$7.69"
              },
    "Cheezy": {"Item 1": {"Name": "Cheeseburger", "Price": 6.69},
               "Item 2": {"Name": "Fries", "Price": 1.00},
               "Item 3": {"Name": "Fizzy Drink", "Price": 1.00},
               "Total": "$8.69"
               },
    "Super": {"Item 1": {"Name": "Cheeseburger", "Price": 6.69},
              "Item 2": {"Name": "Large Fries", "Price": 2.00},
              "Item 3": {"Name": "Smoothie", "Price": 2.00},
              "Total": "$10.69"
              },
}


# Function to display all combos and their prices
def display_combo_info(combos):
    message = "Combo Information:\n\n"
    for combo_id, combo_info in combos.items():
        message += f"Combo Name: {combo_id}\n"
        message += "-" * 50 + "\n"
        for key, item_info in combo_info.items():
            if key != "Total":
                price = float(item_info['Price'])
                message += f"* {key}: {item_info['Name']} (${price:.2f})\n"
        if combo_info['Total'] is not None:
            total_prices = float(combo_info['Total'][1:])
            message += f"Total Price: ${total_prices:.2f}\n"
        message += "\n"
    easygui.msgbox(message, title="Menu", ok_button="Close")


# Main loop to display the options
while True:
    choice = easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                               choices=["Menu", "Add Combo", "Find Combo",
                                        "Delete Combo", "Exit"])

    # Branch based on the user's choice
    if choice == "Menu":
        display_combo_info(combo)
    elif choice == "Add Combo":
        pass
    elif choice == "Find Combo":
        pass
    elif choice == "Delete Combo":
        pass
    elif choice == "Exit":
        break
