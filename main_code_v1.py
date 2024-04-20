"""Adding Welcoming v2 into the Main Code"""
import easygui
# Define the title and decoration lines
title = "* Welcome to Bens Burgers *"
decoration_line = "-" * 43

# Main loop to display the options
while True:
    choice = easygui.buttonbox(f"{title}\n"
                               f"{decoration_line}\n"
                               "     * How Can I Help You? *\n"  
                               f"{decoration_line}",
                               title="Bens Burgers",
                               choices=["Menu", "Add Combo", "Exit",
                                        "Find Combo", "Delete Combo"],)

    # Branch based on the user's choice
    if choice == "Menu":
        easygui.msgbox("Menu")
    elif choice == "Add Combo":
        easygui.msgbox("Add Combo")
    elif choice == "Find Combo":
        easygui.msgbox("Find Combo")
    elif choice == "Delete Combo":
        easygui.msgbox("Delete Combo")
    elif choice == "Exit":
        break  # Exit the loop if the user chooses to exit
