"""Making a system for users to add a combo to the menu using dictionaries"""
combo = {}

# Loop to get details of two combos
for i in range(2):
    combo_ID = input("\nEnter Combo: ")
    combo[combo_ID] = {}

    # Prompt user for Item 1 and add to combo
    Item_1 = input("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1

    # Prompt user for Item 2 and add to combo
    Item_2 = input("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2

    # Prompt user for Item 3 and add to combo
    Item_3 = input("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3

# Display combos and their items
for combo_id, combo_info in combo.items():
    print(f"\nCombo ID: {combo_id}")

    for key in combo_info:
        print(f"{key}: {combo_info[key]}")
