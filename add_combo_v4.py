"""Adding on from v3 but making sure the user inputs a valid number when
entering the price. Doing this by making a definition to get a valid price
input"""
combo = {}


# Function to get valid price input
def get_valid_price_input(price):
    while True:
        try:
            price = float(input(price))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return round(price, 2)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Loop to get details of one combo
for i in range(1):
    combo_ID = input("\nEnter Combo: ")
    combo[combo_ID] = {}

    # Prompt user for Item 1 and its price, add to combo
    Item_1 = input("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1
    Item_1_Price = get_valid_price_input("Enter Item 1 Price: ")
    combo[combo_ID]['Item 1 Price'] = Item_1_Price

    # Prompt user for Item 2 and its price, add to combo
    Item_2 = input("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2
    Item_2_Price = get_valid_price_input("Enter Item 2 Price: ")
    combo[combo_ID]['Item 2 Price'] = Item_2_Price

    # Prompt user for Item 3 and its price, add to combo
    Item_3 = input("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3
    Item_3_Price = get_valid_price_input("Enter Item 3 Price: ")
    combo[combo_ID]['Item 3 Price'] = Item_3_Price

# Main loop to display combo names, items, and their total price
for combo_id, combo_info in combo.items():
    print(f"\nCombo Name: {combo_id}")

    total_price = 0
    for key, value in combo_info.items():
        if "Price" in key:
            continue
        item_price_key = key + " Price"
        item_price = combo_info[item_price_key]
        total_price += item_price
        print(f"{key}: {value} - Price: {item_price}")

    # Print total price for the combo
    print(f"Total Price: {round(total_price, 2)}")
