#we import the necessary modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


"""we create three objects which we will use throughout our code
money_machine, which inports all of the money machine functionality
coffee_machine, ditto
menu, ditto

the coffee machine is capable of printing a report, checking resources
and also making cofee

the money machine can also print a report, 
take payment and check if payment is sufficient 

the menu can return the names of the menu items (already baked in)
and also the find_drink method which can give a variable the attributes of 
one of the menu items 

again, 
import modules
create fresh objects from the classes in those modules
"""
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#more tradiiotnal part of the code begins now. Initiate while loop
is_on = True

while is_on:
#creates a variable which automatically draws from the menu using the get_items method
#remember, menu is an object with the capability of the original class blueprint
#therefore menu.get_items() will do that job for us
    options = menu.get_items()
#this allows us to input it into an f string and always get the menu
    choice = input(f"What would you like: ({options})?")
#as before, if input is 'off' the code ends
    if choice == "off":
        is_on = False
#but this time if choice is report, we print the reports
    elif choice == "report":
#we do this by asking our objects to perform the report method
#that's a good way to think about this. We ask the object to do the method.
        coffee_maker.report()
        money_machine.report()
#so with that in mind, we move on.
    else:
#to make our code simpler, we assign a variable to drink as follows
# we ask the menu to find the drink and return it as an object with menu attributes
#we do this by inputting the user's choice. if it's in there, drink will now be a MenuItem object
        drink = menu.find_drink(choice)
#having done this, we ask the coffee maker to check if resources are sufficient by passing in the MenuItem object
        if coffee_maker.is_resource_sufficient(drink):
#if resources are sufficient, we move on. we ask the money mmachine to run the payment code
#having done this, it checks the new input amount against the cost attribute of the drink MenuItem
            if money_machine.make_payment(drink.cost):
#and if this too works, we ask the coffee maker to make the drink
                coffee_maker.make_coffee(drink)
