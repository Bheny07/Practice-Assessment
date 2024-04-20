"""Adding find_combo v2 into the main code and making slight
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
    combo_search = easygui.enterbox("Enter the name of the combo you "
                                    "want to search for: ",
                                    title="Combo Search")
    found = False
    for combo_name, combo_info in combos.items():
        if combo_search.lower() == combo_name.lower():
            found = True
            message = f"\nCombo Name: {combo_name}\n"
            for key, value in combo_info.items():
                if key != "Total":
                    message += f"{key}: {value['Name']} - ${value['Price']}\n"
                else:
                    message += f"{key}: {value}\n"
            easygui.msgbox(message, title="Menu Combo")
            break
    if not found:
        easygui.msgbox("Combo not found in the Menu.", title="Error")


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
def get_valid_price_input(prompt, title):
    while True:
        try:
            price = float(easygui.enterbox(prompt, title=title))
            if price < 0:
                easygui.msgbox("Price cannot be negative. "
                               "Please enter a valid number.")
            else:
                return round(price, 2)
        except ValueError:
            easygui.msgbox("Invalid input. Please enter a valid number.")


# Function to add a new combo to the dictionary
def add_combo_item():
    combo_ID = easygui.enterbox("\nEnter Combo Name: ",
                                title="Enter Combo Name")
    combo[combo_ID] = {}

    for i in range(1, 4):
        item_name = easygui.enterbox(f"Enter Item {i}: ",
                                     title=f"Enter Item {i}")
        combo[combo_ID][f"Item {i}"] = {"Name": item_name}
        item_price = get_valid_price_input(f"Enter Item {i} Price: ",
                                           title=f"Enter Item {i} Price")
        combo[combo_ID][f"Item {i}"]["Price"] = item_price


# Main loop to display the options
while True:
    choice = easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                               choices=["Menu", "Add Combo", "Find Combo",
                                        "Delete Combo", "Exit"],
                               title="Bens Burgers")

    # Branch based on the user's choice
    if choice == "Menu":
        display_combo_info(combo)
    elif choice == "Add Combo":
        add_combo_item()
    elif choice == "Find Combo":
        search_combo(combo)
    elif choice == "Delete Combo":
        pass
    elif choice == "Exit":
        break
