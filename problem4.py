
# Problem-04: A program to display the square and squrae root of given number

import math

given_number = float(input("Enter a number:\n"))

def square_and_squareroot(num):
    square = num**2
    if num < 0:
        return f"The square of {num} is {square} and the square root of negative number can't be calculated"

    
    square_root = round(math.sqrt(num), 2)

    return f"The square of {num} is {square} and square root is {square_root}"

result = square_and_squareroot(given_number)
print(result)
