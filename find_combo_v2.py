"""Adding on from v1 but using easygui to make the interface more aesthetic and
easy to use for the user"""
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


# Function to search for a combo using EasyGui
def search_combo():
    combo_search = easygui.enterbox("Enter the name of the combo you "
                                    "want to search for: ",
                                    title="Combo Search")
    if combo_search is None:
        exit()

    found = False
    for combo_name, combo_info in combo.items():
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

# Call function to search for combo
search_combo()
