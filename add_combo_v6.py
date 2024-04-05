"""Adding on from v5 and making it a definition to add to main code.
I will do this by removing the final print statement but rather make it, so it
will be added straight into the menu of combo items"""
import easygui

combo = {}


def get_valid_price_input(prompt):
    while True:
        try:
            price = float(easygui.enterbox(prompt))
            if price < 0:
                easygui.msgbox("Price cannot be negative. "
                               "Please enter a valid number.")
            else:
                return round(price, 2)
        except ValueError:
            easygui.msgbox("Invalid input. Please enter a valid number.")


def add_combo_item():
    for i in range(1):
        combo_ID = easygui.enterbox("\nEnter Combo: ")
        combo[combo_ID] = {}

        Item_1 = easygui.enterbox("Enter Item 1: ")
        combo[combo_ID]['Item 1'] = Item_1
        Item_1_Price = get_valid_price_input("Enter Item 1 Price: ")
        combo[combo_ID]['Item 1 Price'] = Item_1_Price

        Item_2 = easygui.enterbox("Enter Item 2: ")
        combo[combo_ID]['Item 2'] = Item_2
        Item_2_Price = get_valid_price_input("Enter Item 2 Price: ")
        combo[combo_ID]['Item 2 Price'] = Item_2_Price

        Item_3 = easygui.enterbox("Enter Item 3: ")
        combo[combo_ID]['Item 3'] = Item_3
        Item_3_Price = get_valid_price_input("Enter Item 3 Price: ")
        combo[combo_ID]['Item 3 Price'] = Item_3_Price

    for combo_id, combo_info in combo.items():
        message = f"\nCombo Name: {combo_id}\n"
        total_price = 0
        for key, value in combo_info.items():
            if "Price" in key:
                continue
            item_price_key = key + " Price"
            item_price = combo_info[item_price_key]
            total_price += item_price
            message += f"{key}: {value} - Price: {item_price}\n"

        message += f"Total Price: {round(total_price, 2)}"


add_combo_item(combo)

