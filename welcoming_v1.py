"""Making a system for users to choose options on what they would like to do"""

import easygui

while True:
    choice = easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                               choices=["Menu", "Add Combo", "Exit",
                                        "Find Combo", "Delete Combo"])

    if choice == "Menu":
        easygui.msgbox("Menu")
    elif choice == "Add Combo":
        easygui.msgbox("Add Combo")
    elif choice == "Find Combo":
        easygui.msgbox("Find Combo")
    elif choice == "Delete Combo":
        easygui.msgbox("Delete Combo")
    elif choice == "Exit":
        break
