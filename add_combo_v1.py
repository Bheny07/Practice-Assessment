"""A system for users to enter a new combo into the menu"""
import easygui

combo = {}


def add_combo():
    new_combo_ID = easygui.enterbox("Enter Combo Name: ", title="Combo")
    combo[new_combo_ID] = {}

    item_1 = easygui.enterbox("Enter Item 1: ", title="Item 1")
    combo[new_combo_ID]['Item 1'] = item_1

    item_1_price = easygui.enterbox("Enter Item 1 Price: ",
                                    title="Item 1 Price")
    combo[new_combo_ID]['Item 1 Price'] = item_1_price

    item_2 = easygui.enterbox("Enter Item 2: ", title="Item 2")
    combo[new_combo_ID]['Item 2'] = item_2

    item_2_price = easygui.enterbox("Enter Item 2 Price: ",
                                    title="Item 2 Price")
    combo[new_combo_ID]['Item 2 Price'] = item_2_price

    item_3 = easygui.enterbox("Enter Item 3: ", title="Item 3")
    combo[new_combo_ID]['Item 3'] = item_3

    item_3_price = easygui.enterbox("Enter Item 3 Price: ",
                                    title="Item 3 Price")
    combo[new_combo_ID]['Item 3 Price'] = item_3_price


add_combo()
