# Problem-02: A program to calculate the summmation and average of two numbers

first_number = float(input("Enter the first number:\n"))
second_number = float(input("Enter second number:\n"))

def sum_and_ave(num1, num2):
    sum = num1 + num2
    average = sum / 2

    return f"The sum of {num1} and {num2} is {sum} and the average is {average}"

result = sum_and_ave(first_number, second_number)
print(result)