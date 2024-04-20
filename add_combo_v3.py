"""Adding on from v2 but making this version when it prints the statements,
to print the prices with the items, not separately."""
combo = {}

# Loop to get details of one combo
for i in range(1):
    combo_ID = input("\nEnter Combo: ")
    combo[combo_ID] = {}

    # Prompt user for Item 1 and its price, add to combo
    Item_1 = input("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1
    Item_1_Price = float(input("Enter Item 1 Price: "))
    combo[combo_ID]['Item 1 Price'] = Item_1_Price

    # Prompt user for Item 2 and its price, add to combo
    Item_2 = input("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2
    Item_2_Price = float(input("Enter Item 2 Price: "))
    combo[combo_ID]['Item 2 Price'] = Item_2_Price

    # Prompt user for Item 3 and its price, add to combo
    Item_3 = input("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3
    Item_3_Price = float(input("Enter Item 3 Price: "))
    combo[combo_ID]['Item 3 Price'] = Item_3_Price

    # Calculate final price and add to combo
    combo[combo_ID]['Final Price'] = Item_1_Price + Item_2_Price + Item_3_Price

# Main loop to display combo names, items, and their prices
for combo_id, combo_info in combo.items():
    print(f"\nCombo Name: {combo_id}")

    for key, value in combo_info.items():
        # Skip printing prices
        if "Price" in key:
            continue
        # Get price of the item and print
        item_price_key = key + " Price"
        item_price = combo_info[item_price_key]
        print(f"{key}: {value} - Price: {item_price}")

    # Print final price for the combo
    print(f"Final Price: {combo_info['Final Price']}")
