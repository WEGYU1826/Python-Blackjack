from art import logo
from replit import clear


# Add
def add(n1, n2):
    return n1 + n2


# Substructure
def sub(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next numer? "))
        calculating_function = operations[operation_symbol]
        answer = calculating_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cont = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
        )
        if cont == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


# print(logo)
calculator()
