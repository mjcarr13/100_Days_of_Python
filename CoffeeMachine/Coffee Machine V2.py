MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

# TODO 1: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):”



# TODO 4: Check resources sufficient?

#takes coffee choice and returns True if coffee can be made, else prints reason and returns False


def check_resources(coffee_to_check):
    #rather than using the if else statement, we create a new variable to compare the ingredients vs the resources
    coffee_ingredients = MENU[coffee_to_check]["ingredients"]
    #loop through the coffee ingredients. if the item appears in the resources list, we can access using resources[item]
    for item in coffee_ingredients:
    #initiate for loop to give us the items in the ingredients dictionary. Then specifiy which item you mean:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


# TODO 5: Process coins.


#same deal - function to take coffee choice input

def process_coins():
    print("Please insert coins")
    total_coins = int(input("How many quarters")) * 0.25
    total_coins += int(input("How many nickels")) * 0.10
    total_coins += int(input("How many dimes")) * 0.05
    total_coins += int(input("How many pennies")) * 0.01
    return total_coins

def check_transaction(given_coins, coffee):
    #do I just put the whole take coins function inside this one?
    coins_needed = MENU[coffee]["cost"]
    if given_coins < coins_needed:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif given_coins == coins_needed:
        return True
    elif given_coins > coins_needed:
        change = format(given_coins - coins_needed, '.2f')
        print(f"Here is ${change} dollars in change.")
        return True



def coffee_machine():
    machine_on = True
    while machine_on:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino):")
        if coffee_choice == "off":
            machine_on = False
            exit()
        elif coffee_choice == "report":
            print(f"Water: {resources["water"]}\n"
                  f"Milk: {resources["milk"]}\n"
                  f"Coffee: {resources["coffee"]}\n"
                  f"Money: {resources["money"]}\n")
        else:
            if check_resources(coffee_choice):
                if check_transaction(process_coins(), coffee_choice):
                    for item in MENU[coffee_choice]["ingredients"]:
                        resources[item] -= MENU[coffee_choice]["ingredients"][item]
                    resources["money"] += MENU[coffee_choice]["cost"]
                    print(f"Here is your {coffee_choice}. Enjoy!")

coffee_machine()






