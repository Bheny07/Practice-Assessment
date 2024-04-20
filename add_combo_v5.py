"""Adding on from v4 but adding easygui instead of print statements."""
import easygui

combo = {}


# Function to get valid price input using EasyGui
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


# Loop to get details of one combo
for i in range(1):
    combo_ID = easygui.enterbox("\nEnter Combo: ")
    combo[combo_ID] = {}

    # Prompt user for Item 1 and its price, add to combo
    Item_1 = easygui.enterbox("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1
    Item_1_Price = get_valid_price_input("Enter Item 1 Price: ")
    combo[combo_ID]['Item 1 Price'] = Item_1_Price

    # Prompt user for Item 2 and its price, add to combo
    Item_2 = easygui.enterbox("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2
    Item_2_Price = get_valid_price_input("Enter Item 2 Price: ")
    combo[combo_ID]['Item 2 Price'] = Item_2_Price

    # Prompt user for Item 3 and its price, add to combo
    Item_3 = easygui.enterbox("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3
    Item_3_Price = get_valid_price_input("Enter Item 3 Price: ")
    combo[combo_ID]['Item 3 Price'] = Item_3_Price

# Main loop to display combo names, items, and their total price
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

    # Print total price for the combo
    message += f"Total Price: {round(total_price, 2)}"
    easygui.msgbox(message)
