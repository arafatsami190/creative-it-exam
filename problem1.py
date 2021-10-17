# Prbolem-01: A program to calculate the subtraction and division of two numbers

first_number = float(input("Enter first number:\n"))
second_number = float(input("Enter second number:\n"))
operation = input("Enter 's' for subtraction of 'd' for division:\n").lower()

def calculate(num1, num2, operand):
    if operand == "s":
        return num1 - num2
    elif operand == "d":
        return num1 / num2
    else:
        return "Please, enter everything properly"

result = calculate(first_number, second_number, operation)
print(result)