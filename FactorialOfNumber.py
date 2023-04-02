# This simple code will turn out the factorial of a Number.
# Dated 2nd April 2023

Num = int(input("Enter the no and I'll return the factorial:"))

i = 1

list1 = [Num]

for j in range(Num):

    list1.append(Num - i)
    i = i + 1
    if Num == i:
        break

factorial = 1

print("---------------------------------")

for k in range(len(list1)):

    factorial = factorial * (list1[k])

print(f"Factorial of {Num} is {factorial}")
