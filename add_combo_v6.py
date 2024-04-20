"""Adding on from v5 and making it a more simple version for the user by
 using multi enter boxes instead of getting the user to type out each item
 individually"""
import easygui

combo = {}


# Function to get valid price input for a field
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
            # Retry with valid input
            prompt = easygui.enterbox(f"Invalid input for {field_name}. "
                                      f"Please enter a valid number:")
            if prompt is None:
                return None  # Return None if user cancels input


# Function to add items to combo
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

    # Display added combo details
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


# Call function to add combo items
add_combo_item()
