import calculator_logo


def add(n1, n2):
    '''Adds two numbers'''
    return n1 + n2


def sub(n1, n2):
    '''Subtracts two numbers'''
    return n1 - n2


def multi(n1, n2):
    '''Multiples two numbers'''
    return n1 * n2


def div(n1, n2):
    '''Divide two numbers'''
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}


def calculator():
    print(calculator_logo.logo)

    n1 = float(input("Enter the first number?"))

    for i in operations:
        print(i)

    rep = True

    while rep == True:
        operation_symbol = input("Pick an operation from above: ")
        n2 = float(input("Enter the second number:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        repeat = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")

        if repeat == 'y':
            n1 = answer
        elif repeat == 'n':
            calculator()
        elif repeat == 'n':
            rep = False
        else:
            print("Invalid Input")


calculator()

# def calc1():
#   n1 = int(input("Enter the first number?"))


# def calc2():
#   op = (input("""Choose the operation that you want to perform:
#   +
#   -
#   *
#   /
#   """))
#   n2 = int(input("Enter the second number:"))
#   if op =='+':
#     add(n1, n2)
#   elifif op =='-':
#     sub(n1, n2)
#   elif op =='+':
#     multi(n1, n2)
#   elif op =='+':
#     div(n1, n2)
#   else:
#     print('Invalid Option')


# no = 0

# calc1()
# calc2()

# while no == 0:
#   repeat = input(f"Type y to continue calculating with {n1} or type 'n' to start a new calculation")

#   if repeat == 'y':
#     calc()
#   elif repeat == 'n':


