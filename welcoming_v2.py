"""Adding on from Version 1 but giving the user options on where to go next"""
import easygui
easygui.buttonbox("Welcome to Bens Burgers\n How Can I Help You?",
                  choices=["Menu", "Order", "Exit", "Help"])
