"""Adding on from v1 but adding a price system for the users
to add a price to the items"""
combo = {}

# Loop to get details of one combo
for i in range(1):
    combo_ID = input("\nEnter Combo: ")
    combo[combo_ID] = {}

    # Prompt user for Item 1 and its price, add to combo
    Item_1 = input("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1
    Item_1_Price = input("Enter Item 1 Price: ")
    combo[combo_ID]['Item 1 Price'] = Item_1_Price

    # Prompt user for Item 2 and its price, add to combo
    Item_2 = input("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2
    Item_2_Price = input("Enter Item 2 Price: ")
    combo[combo_ID]['Item 2 Price'] = Item_2_Price

    # Prompt user for Item 3 and its price, add to combo
    Item_3 = input("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3
    Item_3_Price = input("Enter Item 3 Price: ")
    combo[combo_ID]['Item 3 Price'] = Item_3_Price

# Display combo names, items, and their prices
for combo_id, combo_info in combo.items():
    print(f"\nCombo Name: {combo_id}")

    for key in combo_info:
        print(f"{key}: {combo_info[key]}")
