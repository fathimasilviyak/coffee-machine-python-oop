# import the classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create object for each classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    user_input = input(f"What would you like? : {menu.get_items()}").lower()
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
 


