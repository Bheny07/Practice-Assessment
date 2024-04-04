"""Making a system for users to add a combo to the menu using dictionaries"""
combo = {}

for i in range(2):
    combo_ID = input("\nEnter Combo: ")
    combo[combo_ID] = {}

    Item_1 = input("Enter Item 1: ")
    combo[combo_ID]['Item 1'] = Item_1

    Item_2 = input("Enter Item 2: ")
    combo[combo_ID]['Item 2'] = Item_2

    Item_3 = input("Enter Item 3: ")
    combo[combo_ID]['Item 3'] = Item_3


for combo_id, combo_info in combo.items():
    print(f"\nHero ID; {combo_id}")

    for key in combo_info:
        print(f"{key}: {combo_info[key]}")