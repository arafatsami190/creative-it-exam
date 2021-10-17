# Problem-03: A program to print all the numbers from 0 to 20 and show their summation at last

sum = 0

for i in range(0, 21):
    print(i, end=" ")
    sum += i

print(f"\nThe sum of the numbers from 0 to 20 is {sum}") 