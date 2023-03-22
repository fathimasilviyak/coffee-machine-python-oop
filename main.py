# import the classes
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create object for each classes
menu = Menu()
espresso = MenuItem("espresso", 50, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
if user_input == "report":
    report = CoffeeMaker()
    print(report)