"""Adding remove combo v3 into the main code and making slight
adjustments to the code so, it all works and functions together as it should"""

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


# Function to search for a combo in the dictionary
def search_combo(combos):
    while True:
        combo_search = easygui.enterbox("Enter the name of the combo you "
                                        "want to search for: ",
                                        title="Combo Search")
        if combo_search is None:
            return  # Exit if user cancels

        for combo_name, combo_info in combos.items():
            if combo_search.lower() == combo_name.lower():
                message = f"\nCombo Name: {combo_name}\n"
                for key, value in combo_info.items():
                    if key != "Total":
                        message += f"{key}: {value['Name']} - " \
                                   f"${value['Price']}\n"
                    else:
                        message += f"{key}: {value}\n"
                easygui.msgbox(message, title="Menu Combo")
                return  # Exit the function after displaying the combo

        # If the combo is not found, ask the user to retry or cancel
        retry = easygui.buttonbox("Combo not found in the Menu. "
                                  "Would you like to retry?",
                                  title="Error",
                                  choices=["Retry", "Cancel"])
        if retry == "Cancel":
            return  # Exit if user cancels


# Function to display all combos and their prices
def display_combo_info(combos):
    message = "Combo Information:\n\n"
    for combo_id, combo_info in combos.items():
        message += f"Combo Name: {combo_id}\n"
        message += "-" * 50 + "\n"
        total_price = 0
        for key, item_info in combo_info.items():
            if key != "Total" and isinstance(item_info, dict):
                price = float(item_info['Price'])
                total_price += price
                message += f"* {key}: {item_info['Name']} (${price:.2f})\n"
        message += f"Total Price: ${total_price:.2f}\n\n"

    easygui.msgbox(message, title="Menu", ok_button="Close")


# Function to validate price inputs
def get_valid_price_input(prompt, field_name):
    while True:
        try:
            price = float(prompt)
            if price < 0:
                easygui.msgbox(f"Price for {field_name} cannot be negative. "
                               "Please enter a valid number.")
            else:
                return round(price, 2)
        except ValueError:
            prompt = easygui.enterbox(f"Invalid input for {field_name}. "
                                      f"Please enter a valid number:",
                                      title="Error")
            if prompt is None:
                return None


# Function to add a new combo to the dictionary
def add_combo_item():
    combo_ID = easygui.enterbox("\nEnter Combo: ", title="Enter Combo")
    if combo_ID is None:
        return  # Exit if combo_ID is None

    combo[combo_ID] = {}

    item_fields = ["Item 1", "Item 2", "Item 3"]
    field_values = easygui.multenterbox("Enter Items:", "Combo Items",
                                        item_fields)

    if field_values is None:
        return  # Exit if field_values is None

    for i, field in enumerate(item_fields):
        combo[combo_ID][field] = {"Name": field_values[i]}

    price_fields = ["Item 1 Price", "Item 2 Price", "Item 3 Price"]
    price_values = easygui.multenterbox("Enter Prices:", "Combo Prices",
                                        price_fields)

    if price_values is None:
        return  # Exit if price_values is None

    for i, field in enumerate(item_fields):
        price = get_valid_price_input(price_values[i], field)
        if price is None:  # Check if "Exit" button is pressed
            return  # Exit if price is None

        combo[combo_ID][field]["Price"] = price

    message = f"\nCombo Name: {combo_ID}\n"
    total_price = 0
    for key, value in combo[combo_ID].items():
        if "Price" in key:
            continue
        item_price = combo[combo_ID][key]["Price"]
        total_price += item_price
        message += f"{key}: {value['Name']} - Price: {item_price}\n"

    message += f"Total Price: {round(total_price, 2)}"
    easygui.msgbox(message, title="Combo Added")


# Function to remove a combo from the dictionary
def remove_combo():
    while True:
        remove_item = easygui.enterbox("Enter a Combo name to Remove: "
                                       .capitalize(),
                                       title="Remove Combo")
        if remove_item in combo:
            del combo[remove_item]
            easygui.msgbox("Combo Was Removed", title="Success")
            break
        else:
            retry = easygui.buttonbox("Combo not found in the dictionary. "
                                      "Try again?",
                                      choices=["Yes", "No"], title="Error")
            if retry == "No":
                break


# Define the title and decoration lines for the main loop
title = "* Welcome to Bens Burgers *"
decoration_line = "-" * 43

# Main loop to display the options
while True:
    choice = easygui.buttonbox(f"{title}\n"
                               f"{decoration_line}\n"
                               "     * How Can I Help You? *\n"  
                               f"{decoration_line}",
                               title="Bens Burgers",
                               choices=["Menu", "Add Combo", "Find Combo",
                                        "Delete Combo", "Exit"])

    # Branch based on the user's choice

    if choice == "Menu":
        display_combo_info(combo)
    elif choice == "Add Combo":
        add_combo_item()
    elif choice == "Find Combo":
        search_combo(combo)
    elif choice == "Delete Combo":
        remove_combo()
    elif choice == "Exit":
        break
    # Exit the loop if the user chooses to exit
