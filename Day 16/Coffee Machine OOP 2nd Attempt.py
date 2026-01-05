from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#let's create some objects from our imported modules

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

#let's start our loop

is_on = True

while is_on:
    #need to get the user input
    drinks = menu.get_items()
    choice = input(f"What would you like: ({drinks})?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)







