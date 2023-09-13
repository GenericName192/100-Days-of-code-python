from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


def isValidInput(input, *arg):
    """Function thats takes in a user input and any number of valid answers and 
    returns True if the answer matches a valid input and False if it doesnt"""
    isValid = False
    for validInput in arg:
        if input == validInput:
            isValid = True
    return isValid

running = True

while running:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if isValidInput(choice, "off", "report", "latte", "espresso", "cappuccino"):
        if choice == "off":
            running = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Please pick a valid option")