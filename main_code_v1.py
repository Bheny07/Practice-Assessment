"""Adding Welcoming v2 into the Main Code"""
import easygui

while True:
    choice = easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                               choices=["Menu", "Add Combo", "Find Combo",
                                        "Delete Combo", "Exit"])

    if choice == "Menu":
        pass
    elif choice == "Add Combo":
        pass
    elif choice == "Find Combo":
        pass
    elif choice == "Delete Combo":
        pass
    elif choice == "Exit":
        break
