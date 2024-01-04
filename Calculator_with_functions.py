def addition(num_1: float, num_2: float) -> str:
    result = num_1 + num_2
    return f"{num_1} + {num_2} = {result}"


def subtraction(num_1: float, num_2: float) -> str:
    result = num_1 - num_2
    return f"{num_1} - {num_2} = {result}"


def multiplication(num_1: float, num_2: float) -> str:
    result = num_1 * num_2
    return f"{num_1} * {num_2} = {result}"


def division(num_1: float, num_2: float) -> float or str:
    if num_2 == 0:
        return "Can;t dived by zero"
    result = num_1 / num_2
    return f"{num_1} / {num_2} = {result :.2f}"


answer = True
while answer:
    print("Menu:")
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Quit
    """"")
    answer = input("Enter your choice (1/2/3/4/5):")
    if answer == '1':
        first_number = float(input("\nEnter the first number:"))
        second_number = float(input("\nEnter the second number"))
        print(addition(first_number, second_number))
    elif answer == '2':
        first_number = float(input("\nEnter the first number:"))
        second_number = float(input("\nEnter the second number"))
        print(subtraction(first_number, second_number))
    elif answer == '3':
        first_number = float(input("\nEnter the first number:"))
        second_number = float(input("\nEnter the second number"))
        print(multiplication(first_number, second_number))
    elif answer == '4':
        first_number = float(input("\nEnter the first number:"))
        second_number = float(input("\nEnter the second number"))
        print(division(first_number, second_number))
    elif answer == '5':
        print("\nGoodbye!")
        break
    else:
        print("\nNot Valid Choice Try Again!")
