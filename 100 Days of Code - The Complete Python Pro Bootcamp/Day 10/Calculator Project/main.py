def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

import art

def calculator():
    print(art.logo)
    n1 = int(input("What's the first number?: "))
    print("+ \n- \n/ \n* \n")
    operator = input("Pick an operation:")
    n2 = int(input("What's the second number?: "))
    answer = operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")
    check_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
    while check_continue == "y":
        n1 = answer
        operator = input("Pick an operation:")
        n2 = int(input("What's the next number?: "))
        answer = operations[operator](n1, n2)
        print(f"{n1} {operator} {n2} = {answer}")
        check_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
    else:
        print("\n" * 100)
        calculator()

calculator()






