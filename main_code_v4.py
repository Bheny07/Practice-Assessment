"""Adding find_combo v2 into the main code and making slight
adjustments to the code so, it all works and functions together as it should"""

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


def get_valid_price_input(price):
    while True:
        try:
            price = float(easygui.enterbox(price))
            if price < 0:
                easygui.msgbox("Price cannot be negative. "
                               "Please enter a valid number.")
            else:
                return round(price, 2)
        except ValueError:
            easygui.msgbox("Invalid input. Please enter a valid number.")


def add_combo_item():
    combo_ID = easygui.enterbox("\nEnter Combo: ", title="Enter Combo Name")
    combo[combo_ID] = {}

    Item_1 = easygui.enterbox("Enter Item 1: ", title="Enter Item")
    combo[combo_ID]['Item 1'] = {"Name": Item_1}
    Item_1_Price = get_valid_price_input("Enter Item 1 Price: ",
                                         title="Enter Item Price")
    combo[combo_ID]['Item 1']['Price'] = Item_1_Price

    Item_2 = easygui.enterbox("Enter Item 2: ", title="Enter Item")
    combo[combo_ID]['Item 2'] = {"Name": Item_2}
    Item_2_Price = get_valid_price_input("Enter Item 2 Price: ",
                                         title="Enter Item Price")
    combo[combo_ID]['Item 2']['Price'] = Item_2_Price

    Item_3 = easygui.enterbox("Enter Item 3: ", title="Enter Item")
    combo[combo_ID]['Item 3'] = {"Name": Item_3}
    Item_3_Price = get_valid_price_input("Enter Item 3 Price: ",
                                         title="Enter Item Price")
    combo[combo_ID]['Item 3']['Price'] = Item_3_Price


while True:
    choice = easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                               choices=["Menu", "Add Combo", "Find Combo",
                                        "Delete Combo", "Exit"],
                               title="Bens Burgers")

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
